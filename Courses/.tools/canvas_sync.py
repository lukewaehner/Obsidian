#!/usr/bin/env python3
"""Report what changed on Canvas since the last sync, for the active-term courses.

The script owns the mechanical half of a Canvas sync: discover the current
term's courses, pull every readable endpoint, and diff each object field by
field against a stored snapshot. It deliberately does NOT write notes -- it
emits a report for the agent to turn into prose.

Usage:
    canvas_sync.py <courses_dir>                 report changes since last sync
    canvas_sync.py <courses_dir> --full          report everything, ignore snapshot
    canvas_sync.py <courses_dir> --course CS4530 limit to one course
    canvas_sync.py <courses_dir> --commit        record current state as the new baseline

Auth: $CANVAS_TOKEN, else ~/.config/canvas/token. Never read from source.

Exit codes: 0 ok · 1 usage/auth/network error · 2 vault mapping problem.
"""

import argparse
import datetime as dt
import hashlib
import html
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request

BASE = os.environ.get("CANVAS_BASE_URL", "https://northeastern.instructure.com")
STATE_NAME = "canvas-sync-state.json"


# --------------------------------------------------------------------------
# term + auth


def term_codes_for(date):
    """Banner term codes current on `date`.

    Fall YYYY is coded (YYYY+1)10, spring YYYY as YYYY30, and the summer
    sessions as YYYY40/50/60 -- read off real course codes such as
    FINA4335.19002.202710 (Fall 2026) and STRT4501.51173.202650 (Summer 2026).
    """
    y, m = date.year, date.month
    if m >= 9:
        return [f"{y + 1}10"]
    if m <= 4:
        return [f"{y}30"]
    return [f"{y}40", f"{y}50", f"{y}60"]


def read_token():
    tok = os.environ.get("CANVAS_TOKEN")
    if tok:
        return tok.strip()
    path = pathlib.Path.home() / ".config" / "canvas" / "token"
    if path.exists():
        return path.read_text().strip()
    sys.exit("no Canvas token: set $CANVAS_TOKEN or create ~/.config/canvas/token")


def is_current_term(course, term_codes):
    """The enrollment term name is authoritative; instructors rename course_code."""
    term_name = (course.get("term") or {}).get("name", "")
    suffix = (course.get("course_code") or "").split(".")[-1]
    return any(term_name.startswith(t) or suffix == t for t in term_codes)


def short_code(course_code):
    """'FINA4335.19002.202710' and 'ORGB3201_S02_09_Fall 2026_Liao' -> 'FINA4335'."""
    head = re.split(r"[._]", course_code)[0]
    m = re.match(r"^([A-Za-z]+)\s*(\d+)", head)
    return f"{m.group(1).upper()}{m.group(2)}" if m else head.upper()


# --------------------------------------------------------------------------
# http


def fetch(path, token):
    """GET a Canvas path following rel=next. Returns (data, error_string)."""
    url = f"{BASE}{path}{'&' if '?' in path else '?'}per_page=100"
    out, first = [], True
    while url:
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                body = json.load(r)
                link = r.headers.get("link", "")
        except urllib.error.HTTPError as e:
            if e.code == 401:
                sys.exit("Canvas rejected the token (401) -- it is likely expired.")
            return (None if first else out), f"HTTP {e.code}"
        except Exception as e:  # noqa: BLE001 - surfaced in the report, never swallowed
            return (None if first else out), str(e)
        if isinstance(body, dict):
            return body, None
        out.extend(body)
        first = False
        m = re.search(r'<([^>]+)>;\s*rel="next"', link)
        url = m.group(1) if m else None
    return out, None


# --------------------------------------------------------------------------
# vault mapping


def map_courses_to_folders(courses, courses_dir):
    """Match each Canvas course to its vault folder by course number in the notes."""
    folders = [p for p in sorted(courses_dir.iterdir()) if p.is_dir() and not p.name.startswith(".")]
    # Read each folder's notes once; every course then tests against the text.
    text = {f: "\n".join(md.read_text(errors="ignore") for md in f.rglob("*.md")) for f in folders}
    mapping, problems = {}, []
    for c in courses:
        code = short_code(c["course_code"])
        m = re.match(r"^([A-Z]+)(\d+)$", code)
        if not m:
            problems.append((code, c["name"], []))
            continue
        subject, number = m.groups()
        pattern = re.compile(rf"\b{subject} ?{number}\b", re.I)
        hits = [f for f in folders if pattern.search(text[f])]
        if len(hits) == 1:
            mapping[code] = hits[0]
        else:
            problems.append((code, c["name"], [h.name for h in hits]))
    return mapping, problems


# --------------------------------------------------------------------------
# snapshot + diff

ENDPOINTS = [
    ("assignments", "/api/v1/courses/{id}/assignments?include[]=submission&include[]=all_dates"),
    ("quizzes", "/api/v1/courses/{id}/quizzes"),
    ("announcements", "/api/v1/courses/{id}/discussion_topics?only_announcements=true"),
    ("discussions", "/api/v1/courses/{id}/discussion_topics"),
    ("modules", "/api/v1/courses/{id}/modules?include[]=items"),
    ("pages", "/api/v1/courses/{id}/pages"),
    ("files", "/api/v1/courses/{id}/files"),
    ("assignment_groups", "/api/v1/courses/{id}/assignment_groups?include[]=assignments"),
]

# Fields whose change is worth a human's attention, per object kind.
TRACKED = {
    "assignments": ["name", "due_at", "unlock_at", "lock_at", "points_possible", "published",
                    "submission_types", "allowed_extensions", "omit_from_final_grade"],
    "quizzes": ["title", "due_at", "unlock_at", "lock_at", "points_possible", "question_count",
                "time_limit", "allowed_attempts", "published", "require_lockdown_browser"],
    "announcements": ["title", "posted_at"],
    "discussions": ["title", "posted_at", "locked"],
    "modules": ["name", "published", "items_count"],
    "pages": ["title", "published"],
    "files": ["display_name", "size", "folder_id"],
    "assignment_groups": ["name", "group_weight"],
}

BODY_FIELD = {
    "assignments": "description", "quizzes": "description", "announcements": "message",
    "discussions": "message", "pages": "body",
}


def digest(text):
    return hashlib.sha256((text or "").encode()).hexdigest()[:16] if text else None


def fingerprint(kind, obj):
    """The comparable shape of one Canvas object."""
    fp = {f: obj.get(f) for f in TRACKED.get(kind, ["name"])}
    if kind in BODY_FIELD:
        fp["_body"] = digest(obj.get(BODY_FIELD[kind]))
    sub = obj.get("submission") or {}
    if sub:
        fp["_score"] = sub.get("score")
        fp["_state"] = sub.get("workflow_state")
    return fp


def plain(markup, limit=3000):
    """HTML -> readable plain text, so the agent can write from the report alone."""
    if not markup:
        return ""
    t = re.sub(r"<br\s*/?>", "\n", markup)
    t = re.sub(r"</(p|div|li|h\d|tr|table|ul|ol)>", "\n", t)
    t = re.sub(r"<li[^>]*>", "  - ", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    t = "\n".join(line.rstrip() for line in t.splitlines())
    t = re.sub(r"\n{3,}", "\n\n", t).strip()
    return t if len(t) <= limit else t[:limit] + "\n  [...truncated]"


def et(iso):
    """UTC ISO -> 'YYYY-MM-DD HH:MM ET', the form the notes are written in."""
    if not iso:
        return "none"
    try:
        d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        return iso
    # US Eastern: EDT (-4) Mar..Oct, EST (-5) otherwise. Good enough for a semester.
    offset = -4 if 3 <= d.month <= 10 else -5
    return (d + dt.timedelta(hours=offset)).strftime("%Y-%m-%d %H:%M") + " ET"


def describe(kind, obj):
    """One-line label for an object."""
    return (obj.get("name") or obj.get("title") or obj.get("display_name")
            or obj.get("url") or str(obj.get("id")))


# --------------------------------------------------------------------------
# report


SINGULAR = {"assignments": "assignment", "quizzes": "quiz", "announcements": "announcement",
            "discussions": "discussion", "modules": "module", "pages": "page",
            "files": "file", "assignment_groups": "assignment group"}


def render_object(kind, obj, change, old_fp, out, groups=None):
    label = describe(kind, obj)
    out.append(f"[{change:<7}] {SINGULAR.get(kind, kind)} · {label}")

    # Points only mean a grade in the context of the group's weight: a 14-point
    # item in a 0%-weight group is practice. Say so on the assignment itself.
    grp = (groups or {}).get(obj.get("assignment_group_id"))
    if grp:
        weight = grp.get("group_weight")
        note = "  <-- UNGRADED, group is 0% of the final grade" if weight == 0 else ""
        out.append(f"            group: \"{grp.get('name')}\" ({weight}% of final grade){note}")

    if change == "CHANGED" and old_fp:
        new_fp = fingerprint(kind, obj)
        for field in sorted(set(old_fp) | set(new_fp)):
            a, b = old_fp.get(field), new_fp.get(field)
            if a == b:
                continue
            if field == "_body":
                out.append("            body text changed -- full text below")
            elif field == "_score":
                out.append(f"            GRADE: {a} -> {b}")
            elif field.endswith("_at"):
                out.append(f"            {field}: {et(a)} -> {et(b)}")
            else:
                out.append(f"            {field}: {a!r} -> {b!r}")

    facts = []
    if obj.get("due_at") is not None or kind in ("assignments", "quizzes"):
        facts.append(f"due {et(obj.get('due_at'))}")
    for f, lab in (("unlock_at", "opens"), ("lock_at", "closes")):
        if obj.get(f):
            facts.append(f"{lab} {et(obj[f])}")
    if obj.get("points_possible") is not None:
        facts.append(f"{obj['points_possible']} pts")
    for f, lab in (("question_count", "questions"), ("time_limit", "min limit")):
        if obj.get(f) is not None:
            facts.append(f"{obj[f]} {lab}")
    attempts = obj.get("allowed_attempts")
    if attempts is not None and attempts != -1:  # -1 is Canvas for unlimited
        facts.append(f"{attempts} attempt(s)")
    if obj.get("require_lockdown_browser"):
        facts.append("REQUIRES LOCKDOWN BROWSER")
    if obj.get("group_weight") is not None:
        facts.append(f"{obj['group_weight']}% of final grade")
    if obj.get("published") is False:
        facts.append("UNPUBLISHED")
    if obj.get("posted_at"):
        facts.append(f"posted {et(obj['posted_at'])}")
    if facts:
        out.append("            " + " · ".join(facts))

    sub = obj.get("submission") or {}
    if sub and (sub.get("score") is not None or sub.get("workflow_state")):
        out.append(f"            submission: {sub.get('workflow_state')} "
                   f"score={sub.get('score')} submitted={et(sub.get('submitted_at'))}"
                   f"{' LATE' if sub.get('late') else ''}")
    for f in ("html_url", "url"):
        if obj.get(f) and kind != "pages":
            out.append(f"            {obj[f].split('?')[0]}")
            break

    body = plain(obj.get(BODY_FIELD.get(kind, "")))
    if body and change in ("NEW", "CHANGED"):
        out.append("            --- text ---")
        out.extend("            " + ln for ln in body.splitlines())
    out.append("")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("courses_dir", help="path to the vault's Courses/ directory")
    ap.add_argument("--full", action="store_true", help="report everything, ignore the snapshot")
    ap.add_argument("--course", help="limit to one short code, e.g. CS4530")
    ap.add_argument("--commit", action="store_true",
                    help="record the current Canvas state as the new baseline")
    ap.add_argument("--term", help="override term autodetection, e.g. 202710")
    ap.add_argument("--show", metavar="KIND:ID",
                    help="print one object's full untruncated text, e.g. assignments:3489293")
    args = ap.parse_args()

    if args.show:
        kind, _, oid = args.show.partition(":")
        if not oid:
            sys.exit("--show wants KIND:ID, e.g. assignments:3489293")
        token = read_token()
        courses, err = fetch("/api/v1/courses?enrollment_state=active&include[]=term", token)
        if courses is None:
            sys.exit(f"could not list courses: {err}")
        for c in courses:
            obj, _ = fetch(f"/api/v1/courses/{c['id']}/{kind}/{oid}", token)
            if isinstance(obj, dict) and obj.get("id"):
                print(f"{describe(kind, obj)}  ({c['course_code']})\n{'-' * 70}")
                print(plain(obj.get(BODY_FIELD.get(kind, "description")), limit=10**9))
                return
        sys.exit(f"no {kind} {oid} in any active course")

    courses_dir = pathlib.Path(args.courses_dir).expanduser().resolve()
    if not courses_dir.is_dir():
        sys.exit(f"not a directory: {courses_dir}")
    state_path = courses_dir / ".tools" / STATE_NAME
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    snapshots = state.get("snapshots", {})

    token = read_token()
    now = dt.datetime.now(dt.timezone.utc)
    term_codes = [args.term] if args.term else term_codes_for(now)

    enrolled, err = fetch("/api/v1/courses?enrollment_state=active&include[]=term", token)
    if enrolled is None:
        sys.exit(f"could not list courses: {err}")
    active = [c for c in enrolled if is_current_term(c, term_codes)]
    if not active:
        sys.exit(f"no active courses in term(s) {', '.join(term_codes)}")

    mapping, problems = map_courses_to_folders(active, courses_dir)
    out = []
    out.append(f"Canvas sync · term {', '.join(term_codes)} · {len(active)} active course(s)")
    out.append(f"Last sync: {state.get('last_sync', 'never')}")
    out.append("")
    if problems:
        out.append("UNMAPPED COURSES -- no single vault folder names these:")
        for code, name, hits in problems:
            out.append(f"  {code} ({name}) matched {hits or 'nothing'}")
        out.append("  A new course needs its folder scaffolded before it can sync.")
        out.append("")

    new_snapshots, changed_total = {}, 0
    for course in sorted(active, key=lambda c: short_code(c["course_code"])):
        code = short_code(course["course_code"])
        if args.course and code != args.course.upper():
            new_snapshots[code] = snapshots.get(code, {})
            continue
        folder = mapping.get(code)
        prev = {} if args.full else snapshots.get(code, {})
        seen, lines, skipped = {}, [], []
        gdata, _ = fetch(f"/api/v1/courses/{course['id']}/assignment_groups", token)
        groups = {g['id']: g for g in gdata} if gdata else {}

        for kind, tmpl in ENDPOINTS:
            data, err = fetch(tmpl.format(id=course["id"]), token)
            if data is None:
                # 404 = tab disabled, 403 = tab restricted to staff. Both are
                # steady states for a course, not news -- note them without
                # letting them register as a change.
                skipped.append(f"{kind} ({err})")
                continue
            for obj in data:
                if not isinstance(obj, dict):
                    continue
                key = f"{kind}:{obj.get('id') or obj.get('url')}"
                fp = fingerprint(kind, obj)
                seen[key] = fp
                old = prev.get(key)
                if old is None:
                    render_object(kind, obj, "NEW", None, lines, groups)
                elif old != fp:
                    render_object(kind, obj, "CHANGED", old, lines, groups)

        gone = [k for k in prev if k not in seen]
        for k in gone:
            lines.append(f"[REMOVED] {k}  (was: {prev[k].get('name') or prev[k].get('title')})")
            lines.append("")

        new_snapshots[code] = seen
        header = f"{'=' * 78}\n{code} · {folder.name if folder else 'UNMAPPED'} · Canvas {course['id']}"
        count = len([l for l in lines if l.startswith("[")])
        note = f"\n  not readable: {', '.join(skipped)}" if skipped else ""
        if not count:
            out.append(header + "\n  no changes" + note + "\n")
        else:
            changed_total += 1
            out.append(header + f"\n  {count} change(s)" + note + "\n")
            out.extend(lines)

    out.append("=" * 78)
    out.append(f"{changed_total} of {len(active)} course(s) have changes.")
    if args.commit:
        state_path.parent.mkdir(parents=True, exist_ok=True)
        state_path.write_text(json.dumps(
            {"last_sync": now.isoformat(timespec="seconds"),
             "folders": {k: v.name for k, v in mapping.items()},
             "snapshots": new_snapshots}, indent=1, sort_keys=True))
        out.append(f"Baseline recorded: {state_path}")
    else:
        out.append("Baseline NOT recorded. Re-run with --commit once the notes are written.")
    print("\n".join(out))


if __name__ == "__main__":
    main()

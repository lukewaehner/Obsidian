#!/usr/bin/env python3
"""Report the week's classes, deadlines, and assigned material from the vault.

The script owns the mechanical half of a weekly review: walk the course
folders, pull every dated fact out of the notes, and lay it out day by day.
It deliberately does NOT judge, prioritise, or write notes -- it emits a
report for the agent to turn into a plan.

The window is literal. By default it runs from today through Sunday of the
current Mon-Sun week, so a Wednesday run covers Wed-Sun and a Sunday run
covers Sunday alone. Use --next for the week ahead rather than having the
tool guess which week you meant.

Usage:
    week_report.py <courses_dir>                    today -> Sunday 23:59
    week_report.py <courses_dir> --next             the following Mon-Sun week
    week_report.py <courses_dir> --week 2026-10-08  the Mon-Sun week around it
    week_report.py <courses_dir> --from D --to D    an explicit date range
    week_report.py <courses_dir> --course FINA4335  limit to one course
    week_report.py <courses_dir> --today 2026-09-23 pretend it is another day

Exit codes: 0 ok · 1 usage error · 2 vault layout problem.
"""

import argparse
import datetime as dt
import pathlib
import re
import sys
from collections import namedtuple

MONTHS = {m: i for i, m in enumerate(
    "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}
WEEKDAYS = {d: i for i, d in enumerate("Mon Tue Wed Thu Fri Sat Sun".split())}

DELIVERABLE_TYPES = {"assignment", "exam", "activity"}
STATE_NAME = "canvas-sync-state.json"
STALE_AFTER_DAYS = 7
MAX_OVERDUE = 20

Meeting = namedtuple("Meeting", "date label weekday_ok")
Task = namedtuple("Task", "done text due")
Course = namedtuple("Course", "folder name code semester_start meets")
Item = namedtuple("Item", "date kind course title detail path extra")


# --------------------------------------------------------------------------
# window


def week_bounds(d):
    """Monday and Sunday of the Mon-Sun week containing `d`."""
    monday = d - dt.timedelta(days=d.weekday())
    return monday, monday + dt.timedelta(days=6)


def resolve_window(today, *, next_week=False, week=None, frm=None, to=None):
    """Inclusive start and end dates of the reporting window.

    Raises ValueError on a half-specified or inverted explicit range.
    """
    if frm or to:
        if not (frm and to):
            raise ValueError("--from and --to must be given together")
        if frm > to:
            raise ValueError(f"--from {frm} is after --to {to}")
        return frm, to
    if week:
        return week_bounds(week)
    monday, sunday = week_bounds(today)
    if next_week:
        return monday + dt.timedelta(days=7), sunday + dt.timedelta(days=7)
    return today, sunday


# --------------------------------------------------------------------------
# note parsing

FM_SCALAR = re.compile(r"^([A-Za-z_][\w-]*):[ \t]*(\S.*?)[ \t]*$")
HEADING = re.compile(r"^#{2,}\s+(.*?)\s*$")
ISO_DATE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
TASK_LINE = re.compile(r"^\s*[-*]\s+\[([ xX])\]\s+(.*)$")
TASK_DUE = re.compile(r"📅\s*(\d{4}-\d{2}-\d{2})")
CALLOUT_OPEN = re.compile(r"^>\s*\[!(\w+)\]\s*(.*)$")
COURSE_NUMBER = re.compile(r"\*\*Course Number\*\*:\s*([A-Z]{2,4})\s*(\d{4})")

MEETING_LINE = re.compile(
    r"^-\s+\*\*(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s+"
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{1,2})\*\*"
    r"(?:\s*[—–-]\s*(.*))?$")


def as_date(value):
    """The ISO date leading `value`, or None. Tolerates a trailing time."""
    if not value:
        return None
    m = ISO_DATE.match(str(value).strip())
    return dt.date(*map(int, m.groups())) if m else None


def parse_frontmatter(text):
    """Scalar keys from a leading YAML block.

    List values (`tags:`) are skipped rather than parsed -- nothing here
    needs them, and a real YAML dependency is not worth one field.
    """
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    out = {}
    for line in text[3:end].splitlines():
        m = FM_SCALAR.match(line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip("\"'")
    return out


def sections(text):
    """Body lines grouped under the `##` heading that introduces them."""
    out, current = {}, None
    for line in text.splitlines():
        m = HEADING.match(line)
        if m:
            current = m.group(1)
            out.setdefault(current, [])
        elif current is not None:
            out[current].append(line)
    return out


def parse_meeting(line, semester_start):
    """A `- **Tue Sep 22** — label` bullet, or None.

    The shape is matched strictly rather than trusting the `## Meetings`
    boundary: several topic notes carry freeform bullets under later
    headings that a section-scoped parser would read as meeting dates.

    Notes write no year. It comes from the semester, rolling forward when
    the month precedes the semester's start month -- a fall course meeting
    in January meets the following calendar year.
    """
    m = MEETING_LINE.match(line.strip())
    if not m:
        return None
    weekday, month_name, day, label = m.groups()
    month = MONTHS[month_name]
    year = semester_start.year + (1 if month < semester_start.month else 0)
    try:
        date = dt.date(year, month, int(day))
    except ValueError:
        return None
    return Meeting(date, (label or "").strip(),
                   date.weekday() == WEEKDAYS[weekday])


def parse_task(line):
    """A Tasks-plugin checkbox line, or None."""
    m = TASK_LINE.match(line)
    if not m:
        return None
    body = m.group(2).strip()
    found = TASK_DUE.search(body)
    due = as_date(found.group(1)) if found else None
    text = TASK_DUE.sub("", body).strip() if found else body
    return Task(m.group(1).lower() == "x", text.rstrip(" ·-—"), due)


def callouts(text, kinds=("danger", "warning")):
    """The first callout of each requested kind, wrapped lines joined.

    Assignment notes put the due time, submission channel, and grade weight
    here, which is exactly the context a bare date loses. Both kinds are
    read because they carry different halves of it: a practice quiz states
    its 0% weight in a `[!warning]` and its real hazard in a `[!danger]`,
    and dropping either one misprices the work.
    """
    found, parts, kind = {}, [], None

    def flush():
        if kind and kind not in found:
            joined = " ".join(p for p in parts if p)
            if joined:
                found[kind] = joined

    for line in text.splitlines():
        m = CALLOUT_OPEN.match(line)
        if m:
            flush()
            kind = m.group(1).lower() if m.group(1).lower() in kinds else None
            parts = [m.group(2).strip()] if kind else []
        elif kind:
            if line.startswith(">"):
                parts.append(line.lstrip("> ").strip())
            else:
                flush()
                kind, parts = None, []
    flush()
    return [found[k] for k in kinds if k in found]


def bullets(lines):
    """Non-empty bullet text under a section, checkbox markers stripped."""
    out = []
    for line in lines:
        task = parse_task(line)
        if task:
            if not task.done:
                out.append(task.text)
        elif line.strip().startswith(("-", "*")):
            out.append(line.strip().lstrip("-* ").strip())
    return out


# --------------------------------------------------------------------------
# vault layout


def meeting_times(courses_dir):
    """Course code -> "Mon / Wed / Thu 10:30-11:35 AM", from the calendar.

    Decoration, not a fact the report depends on: if the calendar note is
    missing or its table is reshaped, times are simply omitted.
    """
    out = {}
    for note in sorted(courses_dir.glob("*Calendar.md")):
        found = sections(note.read_text(encoding="utf-8"))
        for line in found.get("Weekly Meeting Pattern", []):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 3 or cells[0].startswith(("---", "Course")):
                continue
            code = cells[0].replace(" ", "")
            if re.fullmatch(r"[A-Z]{2,4}\d{4}", code):
                out[code] = f"{cells[1]} {cells[2]}".strip()
    return out


def discover_courses(courses_dir):
    """Every course folder, with its code and semester start.

    The code comes from the `.base` tracker's filename, falling back to the
    MOC's Course Number line; a folder with neither is reported as a layout
    problem rather than silently skipped.
    """
    courses, unmapped = [], []
    times = meeting_times(courses_dir)
    for folder in sorted(p for p in courses_dir.iterdir()
                         if p.is_dir() and not p.name.startswith(".")):
        moc = folder / f"{folder.name}.md"
        text = moc.read_text(encoding="utf-8") if moc.exists() else ""
        code = None
        for base in sorted(folder.glob("*.base")):
            head = base.stem.split()[0]
            if re.fullmatch(r"[A-Z]{2,4}\d{4}", head):
                code = head
                break
        if not code:
            m = COURSE_NUMBER.search(text)
            code = m.group(1) + m.group(2) if m else None
        if not code:
            unmapped.append(folder.name)
            continue
        start = as_date(parse_frontmatter(text).get("semester_start"))
        courses.append(Course(folder, folder.name, code,
                              start or dt.date.today(), times.get(code, "")))
    return courses, unmapped


def canvas_baseline(courses_dir):
    """Age in days of the recorded Canvas sync baseline, or None."""
    state = courses_dir / ".tools" / STATE_NAME
    if not state.exists():
        return None
    stamp = dt.date.fromtimestamp(state.stat().st_mtime)
    return (dt.date.today() - stamp).days


# --------------------------------------------------------------------------
# collection


def is_open(fm, text, title):
    """Whether a deliverable is still outstanding.

    A note is done when its frontmatter says so or when the checkbox that
    mirrors its own title is ticked; a graded score alone does not count,
    since notes record those without closing the box.
    """
    if fm.get("status", "").lower() == "done":
        return False
    for line in text.splitlines():
        task = parse_task(line)
        if task and task.done and task.text.lower().startswith(title.lower()[:24]):
            return False
    return True


def collect(course, vault):
    """Every dated fact in one course folder.

    Returns (deliverables, tasks, meetings, undated, warnings).
    """
    deliverables, tasks, meetings, undated, warnings = [], [], [], [], []
    has_meetings = False

    for note in sorted(course.folder.rglob("*.md")):
        text = note.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        kind = fm.get("type", "")
        title = note.stem
        rel = note.relative_to(vault).as_posix()
        found = sections(text)

        if kind in DELIVERABLE_TYPES:
            due = as_date(fm.get("due"))
            if due is None:
                undated.append(title)
            elif is_open(fm, text, title):
                deliverables.append(Item(due, "DUE", course, title,
                                         callouts(text), rel, kind))

        for line in text.splitlines():
            task = parse_task(line)
            if not task or task.done or not task.due:
                continue
            # The self-named checkbox restates the frontmatter due date; the
            # interesting tasks are the setup steps that have no note.
            if task.text.lower().startswith(title.lower()[:24]):
                continue
            tasks.append(Item(task.due, "TASK", course, task.text,
                              None, rel, title))

        if kind != "lecture":
            continue
        for line in found.get("Meetings", []):
            meeting = parse_meeting(line, course.semester_start)
            if not meeting:
                continue
            has_meetings = True
            if not meeting.weekday_ok:
                warnings.append(
                    f"{course.code}: {rel} says '{line.strip()}' but "
                    f"{meeting.date} is a "
                    f"{meeting.date.strftime('%a')} -- date not trusted")
            extra = {
                "assigned": bullets(found.get("Assigned Material", [])),
                "due_this": bullets(found.get("Due This Session", [])),
                "note": rel,
            }
            meetings.append(Item(meeting.date, "CLASS", course, title,
                                 meeting.label, rel, extra))

    if not has_meetings:
        warnings.append(
            f"{course.code}: no topic note carries a '## Meetings' section, "
            f"so no class days are reported for it")
    return deliverables, tasks, meetings, undated, warnings


# --------------------------------------------------------------------------
# rendering


def fmt_item(item, prepped):
    """Render one item. `prepped` maps a topic note to the day its assigned
    material was already listed, so a course that meets three times in a
    week states the week's readings once instead of three times."""
    lines = []
    if item.kind == "CLASS":
        when = f"  {item.course.meets}" if item.course.meets else ""
        label = f"  -- {item.detail}" if item.detail else ""
        lines.append(f"CLASS  {item.course.code:9}{when}")
        lines.append(f"       {item.title}{label}")
        first = prepped.setdefault(item.extra["note"], item.date)
        if first == item.date:
            for reading in item.extra["assigned"]:
                lines.append(f"         [ ] assigned: {reading}")
            for deliverable in item.extra["due_this"]:
                lines.append(f"         !  in class: {deliverable}")
        elif item.extra["assigned"] or item.extra["due_this"]:
            lines.append(f"         (same unit as {first:%a %b %-d} — "
                         f"assigned material listed there)")
        lines.append(f"       note: {item.extra['note']}")
    elif item.kind == "DUE":
        tag = f"  [{item.extra}]" if item.extra != "assignment" else ""
        lines.append(f"DUE    {item.course.code:9}  {item.title}{tag}")
        for detail in item.detail:
            lines.append(f"       {detail}")
        lines.append(f"       note: {item.path}")
    else:
        lines.append(f"TASK   {item.course.code:9}  {item.title}")
        lines.append(f"       from: {item.path}")
    return lines


def render(start, end, items, overdue, undated, warnings, baseline, out):
    span = "one day" if start == end else f"{(end - start).days + 1} days"
    out.append(f"WEEK  {start:%a %Y-%m-%d}  ->  {end:%a %Y-%m-%d} 23:59 ET  ({span})")
    if baseline is None:
        out.append("Canvas baseline: never recorded -- run /courses:sync")
    else:
        stale = "  STALE, run /courses:sync" if baseline > STALE_AFTER_DAYS else ""
        out.append(f"Canvas baseline: {baseline} day(s) old{stale}")
    out.append("")

    order = {"CLASS": 0, "DUE": 1, "TASK": 2}
    day, empty, prepped = start, True, {}
    while day <= end:
        today = sorted((i for i in items if i.date == day),
                       key=lambda i: (order[i.kind], i.course.code))
        if today:
            empty = False
            out.append(f"== {day:%a %Y-%m-%d} " + "=" * 40)
            for item in today:
                out.extend(fmt_item(item, prepped))
                out.append("")
        day += dt.timedelta(days=1)
    if empty:
        out.append("Nothing scheduled or due in this window.")
        out.append("")

    out.append(f"== OVERDUE (open, dated before {start}) " + "=" * 20)
    if not overdue:
        out.append("  none")
    for item in overdue[:MAX_OVERDUE]:
        out.append(f"  {item.date}  {item.course.code:9} {item.title}")
    if len(overdue) > MAX_OVERDUE:
        out.append(f"  ... and {len(overdue) - MAX_OVERDUE} more")
    out.append("")

    out.append("== NO DUE DATE " + "=" * 45)
    if not undated:
        out.append("  none")
    for code, titles in sorted(undated.items()):
        out.append(f"  {code}: {len(titles)} deliverable(s) -- "
                   f"{', '.join(sorted(titles))}")
    out.append("")

    if warnings:
        out.append("== WARNINGS " + "=" * 48)
        for warning in warnings:
            out.append(f"  {warning}")
        out.append("")
    return out


# --------------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("courses_dir", help="path to the vault's Courses/ directory")
    ap.add_argument("--next", dest="next_week", action="store_true",
                    help="the following Mon-Sun week instead of this one")
    ap.add_argument("--week", type=dt.date.fromisoformat, metavar="YYYY-MM-DD",
                    help="the full Mon-Sun week containing this date")
    ap.add_argument("--from", dest="frm", type=dt.date.fromisoformat,
                    metavar="YYYY-MM-DD", help="explicit range start")
    ap.add_argument("--to", type=dt.date.fromisoformat, metavar="YYYY-MM-DD",
                    help="explicit range end")
    ap.add_argument("--course", help="limit to one short code, e.g. FINA4335")
    ap.add_argument("--today", type=dt.date.fromisoformat, metavar="YYYY-MM-DD",
                    help="override today, for checking another week's output")
    args = ap.parse_args()

    courses_dir = pathlib.Path(args.courses_dir).resolve()
    if not courses_dir.is_dir():
        sys.exit(f"not a directory: {courses_dir}")
    vault = courses_dir.parent

    try:
        start, end = resolve_window(args.today or dt.date.today(),
                                    next_week=args.next_week, week=args.week,
                                    frm=args.frm, to=args.to)
    except ValueError as err:
        sys.exit(f"bad window: {err}")

    courses, unmapped = discover_courses(courses_dir)
    if args.course:
        wanted = args.course.upper()
        known = ", ".join(c.code for c in courses) or "none"
        courses = [c for c in courses if c.code == wanted]
        if not courses:
            sys.exit(f"no course with code {wanted}; known codes: {known}")

    items, overdue, undated, warnings = [], [], {}, []
    for course in courses:
        deliverables, tasks, meetings, no_date, course_warnings = collect(
            course, vault)
        warnings.extend(course_warnings)
        if no_date:
            undated[course.code] = no_date
        for item in deliverables + tasks + meetings:
            if start <= item.date <= end:
                items.append(item)
            elif item.date < start and item.kind in ("DUE", "TASK"):
                overdue.append(item)
    overdue.sort(key=lambda i: i.date)

    for folder in unmapped:
        warnings.append(f"UNMAPPED: '{folder}' has no course code -- add a "
                        f"`CODE Assignments.base` or a Course Number line")

    out = render(start, end, items, overdue, undated, warnings,
                 canvas_baseline(courses_dir), [])
    print("\n".join(out))


if __name__ == "__main__":
    main()

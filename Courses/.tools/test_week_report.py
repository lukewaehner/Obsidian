#!/usr/bin/env python3
"""Unit tests for week_report's pure functions.

Run from the vault root:  python3 -m unittest discover -s Courses/.tools
"""

import datetime as dt
import unittest

import week_report as wr

FALL = dt.date(2026, 9, 7)


class WeekBounds(unittest.TestCase):
    def test_midweek_date_bounds_span_monday_to_sunday(self):
        # arrange
        wednesday = dt.date(2026, 9, 23)

        # act
        monday, sunday = wr.week_bounds(wednesday)

        # assert
        self.assertEqual((monday, sunday),
                         (dt.date(2026, 9, 21), dt.date(2026, 9, 27)))

    def test_sunday_is_the_last_day_of_its_own_week(self):
        # arrange
        sunday = dt.date(2026, 9, 20)

        # act
        monday, end = wr.week_bounds(sunday)

        # assert
        self.assertEqual((monday, end),
                         (dt.date(2026, 9, 14), dt.date(2026, 9, 20)))


class ResolveWindow(unittest.TestCase):
    def test_default_runs_from_today_to_sunday(self):
        # arrange
        today = dt.date(2026, 9, 23)

        # act
        start, end = wr.resolve_window(today)

        # assert
        self.assertEqual((start, end), (today, dt.date(2026, 9, 27)))

    def test_default_on_sunday_reports_that_sunday_alone(self):
        # arrange
        sunday = dt.date(2026, 9, 20)

        # act
        start, end = wr.resolve_window(sunday)

        # assert
        self.assertEqual((start, end), (sunday, sunday))

    def test_next_week_covers_the_whole_following_monday_to_sunday(self):
        # arrange
        sunday = dt.date(2026, 9, 20)

        # act
        start, end = wr.resolve_window(sunday, next_week=True)

        # assert
        self.assertEqual((start, end),
                         (dt.date(2026, 9, 21), dt.date(2026, 9, 27)))

    def test_explicit_week_covers_the_full_week_not_just_its_remainder(self):
        # arrange
        today = dt.date(2026, 9, 20)
        anchor = dt.date(2026, 10, 8)  # a Thursday

        # act
        start, end = wr.resolve_window(today, week=anchor)

        # assert
        self.assertEqual((start, end),
                         (dt.date(2026, 10, 5), dt.date(2026, 10, 11)))

    def test_explicit_range_is_used_verbatim(self):
        # arrange
        frm, to = dt.date(2026, 10, 1), dt.date(2026, 10, 3)

        # act
        start, end = wr.resolve_window(dt.date(2026, 9, 20), frm=frm, to=to)

        # assert
        self.assertEqual((start, end), (frm, to))

    def test_inverted_range_is_rejected(self):
        # arrange
        frm, to = dt.date(2026, 10, 5), dt.date(2026, 10, 1)

        # act / assert
        with self.assertRaises(ValueError):
            wr.resolve_window(dt.date(2026, 9, 20), frm=frm, to=to)

    def test_half_a_range_is_rejected(self):
        # act / assert
        with self.assertRaises(ValueError):
            wr.resolve_window(dt.date(2026, 9, 20), frm=dt.date(2026, 10, 1))


class ParseMeeting(unittest.TestCase):
    def test_bare_bullet_yields_the_dated_meeting(self):
        # act
        meeting = wr.parse_meeting("- **Tue Sep 22**", FALL)

        # assert
        self.assertEqual(meeting.date, dt.date(2026, 9, 22))

    def test_trailing_description_becomes_the_label(self):
        # act
        meeting = wr.parse_meeting("- **Mon Sep 21** — Lecture — Genre", FALL)

        # assert
        self.assertEqual(meeting.label, "Lecture — Genre")

    def test_freeform_bullet_is_not_a_meeting(self):
        # arrange -- Session 03's notes carry bullets like this under a
        # later heading; a section-boundary parser would swallow them.
        line = "- Most friends lived next door"

        # act / assert
        self.assertIsNone(wr.parse_meeting(line, FALL))

    def test_bolded_non_date_is_not_a_meeting(self):
        # act / assert
        self.assertIsNone(wr.parse_meeting("- **Week 3** of the course", FALL))

    def test_month_before_the_semester_start_rolls_into_the_next_year(self):
        # arrange -- a fall course meeting in January meets in 2027

        # act
        meeting = wr.parse_meeting("- **Mon Jan 11**", FALL)

        # assert
        self.assertEqual(meeting.date, dt.date(2027, 1, 11))

    def test_weekday_that_contradicts_the_date_is_flagged_not_dropped(self):
        # arrange -- Sep 22 2026 is a Tuesday, so "Wed" is wrong
        # act
        meeting = wr.parse_meeting("- **Wed Sep 22**", FALL)

        # assert
        self.assertFalse(meeting.weekday_ok)

    def test_impossible_date_is_rejected(self):
        # act / assert
        self.assertIsNone(wr.parse_meeting("- **Tue Feb 30**", FALL))


class ParseFrontmatter(unittest.TestCase):
    def test_scalar_keys_are_read(self):
        # arrange
        text = "---\ntype: assignment\ndue: 2026-11-22\n---\n# HW3\n"

        # act
        fm = wr.parse_frontmatter(text)

        # assert
        self.assertEqual(fm, {"type": "assignment", "due": "2026-11-22"})

    def test_list_values_are_skipped_rather_than_mangled(self):
        # arrange
        text = "---\ntags:\n  - assignment\n  - finance\ntype: assignment\n---\n"

        # act
        fm = wr.parse_frontmatter(text)

        # assert
        self.assertEqual(fm, {"type": "assignment"})

    def test_quoted_wikilink_value_is_unwrapped(self):
        # arrange
        text = '---\ncourse: "[[Computational Methods in Finance]]"\n---\n'

        # act
        fm = wr.parse_frontmatter(text)

        # assert
        self.assertEqual(fm["course"], "[[Computational Methods in Finance]]")

    def test_note_without_frontmatter_yields_nothing(self):
        # act / assert
        self.assertEqual(wr.parse_frontmatter("# Just a heading\n"), {})


class ParseTask(unittest.TestCase):
    def test_unchecked_task_with_a_date(self):
        # act
        task = wr.parse_task("- [ ] HW3 📅 2026-11-22")

        # assert
        self.assertEqual((task.done, task.text, task.due),
                         (False, "HW3", dt.date(2026, 11, 22)))

    def test_checked_task_is_marked_done(self):
        # act
        task = wr.parse_task("- [x] Install LockDown Browser 📅 2026-09-24")

        # assert
        self.assertTrue(task.done)

    def test_undated_task_has_no_due(self):
        # act
        task = wr.parse_task("- [ ] † Case: SMA Micro-Electronic Products (A)")

        # assert
        self.assertIsNone(task.due)

    def test_plain_bullet_is_not_a_task(self):
        # act / assert
        self.assertIsNone(wr.parse_task("- Education"))

    def test_completion_stamp_is_stripped_from_the_text(self):
        # arrange -- a ticked box keeps its ✅ date; leaving it in stops the
        # text matching the note, which read Activity 01 as overdue.
        line = "- [x] Submit Activity 01 - User Stories 📅 2026-09-14 ✅ 2026-09-17"

        # act
        task = wr.parse_task(line)

        # assert
        self.assertEqual(task.text, "Submit Activity 01 - User Stories")

    def test_priority_marker_is_stripped_from_the_text(self):
        # act
        task = wr.parse_task("- [ ] Finish HW2 ⏫ 📅 2026-11-01")

        # assert
        self.assertEqual(task.text, "Finish HW2")


class IsSelfTask(unittest.TestCase):
    def test_action_verb_before_the_title_still_counts_as_the_same_item(self):
        # arrange -- the box says "Submit X", the note is titled "X"
        # act / assert
        self.assertTrue(wr.is_self_task(
            "Submit Activity 03 - Mutation Testing with Stryker",
            "Activity 03 - Mutation Testing with Stryker"))

    def test_bare_title_counts_as_the_same_item(self):
        # act / assert
        self.assertTrue(wr.is_self_task("HW3", "HW3"))

    def test_em_dash_in_the_body_matches_the_hyphen_in_the_filename(self):
        # act / assert
        self.assertTrue(wr.is_self_task(
            "Group Case Report 1 — Cynthia Carroll at Anglo American",
            "Group Case Report 1 - Cynthia Carroll at Anglo American"))

    def test_setup_task_merely_mentioning_the_deliverable_is_kept(self):
        # arrange -- the LockDown install is the reason to read the report;
        # a containment test would hide it behind Quiz 1.
        # act / assert
        self.assertFalse(wr.is_self_task(
            "Install and test Respondus LockDown Browser via [[Quiz 1 Prep]]",
            "Quiz 1"))


class IsOpen(unittest.TestCase):
    def test_submitted_activity_is_not_open(self):
        # arrange -- status stays "raw" on graded notes, so the ticked box
        # is the only signal that the work is done
        text = ("# Activity 01 - User Stories\n"
                "- [x] Submit Activity 01 - User Stories 📅 2026-09-14 "
                "✅ 2026-09-17\n")

        # act / assert
        self.assertFalse(wr.is_open({"status": "raw"}, text,
                                    "Activity 01 - User Stories"))

    def test_unticked_activity_is_open(self):
        # arrange
        text = ("# Activity 03 - Mutation Testing\n"
                "- [ ] Submit Activity 03 - Mutation Testing 📅 2026-09-21\n")

        # act / assert
        self.assertTrue(wr.is_open({"status": "raw"}, text,
                                   "Activity 03 - Mutation Testing"))

    def test_frontmatter_status_done_closes_the_item(self):
        # act / assert
        self.assertFalse(wr.is_open({"status": "done"}, "# HW1\n", "HW1"))


class Callouts(unittest.TestCase):
    def test_single_line_danger_callout_is_returned(self):
        # arrange
        text = ("# HW3\n\n> [!danger] Due Sun Nov 22, 11:59pm ET · CodeGrade\n"
                "\nBody text.\n")

        # act / assert
        self.assertEqual(wr.callouts(text),
                         ["Due Sun Nov 22, 11:59pm ET · CodeGrade"])

    def test_wrapped_callout_lines_are_joined(self):
        # arrange
        text = ("> [!danger] Important date\n"
                "> [[Individual Project 1]] due **Wednesday Sep 23, 5:00pm ET**\n")

        # act / assert
        self.assertEqual(
            wr.callouts(text),
            ["Important date [[Individual Project 1]] due "
             "**Wednesday Sep 23, 5:00pm ET**"])

    def test_weight_in_a_warning_survives_alongside_the_danger(self):
        # arrange -- Quiz 1 Prep states its 0% weight in the warning and its
        # real hazard in the danger; keeping only one misprices the work.
        text = ("> [!warning] Practice quiz — **0% of the grade**\n"
                "\n> [!danger] It is the LockDown Browser check.\n")

        # act
        found = wr.callouts(text)

        # assert
        self.assertEqual(found, ["It is the LockDown Browser check.",
                                 "Practice quiz — **0% of the grade**"])

    def test_only_the_first_callout_of_each_kind_is_kept(self):
        # arrange
        text = ("> [!danger] First hazard\n\n> [!danger] Second hazard\n")

        # act / assert
        self.assertEqual(wr.callouts(text), ["First hazard"])

    def test_unrequested_callout_kinds_are_ignored(self):
        # act / assert
        self.assertEqual(wr.callouts("> [!info] Source\n> A syllabus.\n"), [])

    def test_success_callout_does_not_leak_into_a_danger(self):
        # arrange -- a finished assignment opens with [!success]; its body
        # must not be attributed to the danger that follows it.
        text = ("> [!success] Done — graded 100/100\n"
                "> Submitted early.\n\n> [!danger] Extended to Sep 24\n")

        # act / assert
        self.assertEqual(wr.callouts(text), ["Extended to Sep 24"])


class Sections(unittest.TestCase):
    def test_body_lines_are_grouped_under_their_heading(self):
        # arrange
        text = ("# Title\n\n## Meetings\n\n- **Tue Sep 22**\n\n"
                "## Assigned Material\n\n- [ ] Read chapter 4\n")

        # act
        found = wr.sections(text)

        # assert
        self.assertEqual([l for l in found["Assigned Material"] if l.strip()],
                         ["- [ ] Read chapter 4"])

    def test_a_later_heading_closes_the_previous_section(self):
        # arrange
        text = "## Meetings\n- **Tue Sep 22**\n## Notes\n- Education\n"

        # act
        found = wr.sections(text)

        # assert
        self.assertEqual([l for l in found["Meetings"] if l.strip()],
                         ["- **Tue Sep 22**"])


if __name__ == "__main__":
    unittest.main()

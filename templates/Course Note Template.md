<%*
/* Course Note Template — auto-applied to anything created under Courses/.
 *
 * The only thing you type is the filename. Everything else is derived:
 *   course + backlink : the folder name (folder names match course MOC names)
 *   course tags       : inherited from the course MOC's frontmatter
 *   topic tag         : slugified from the filename
 *   module number     : the digits in the filename
 *   week              : semester_start on the course MOC vs. today
 *   skeleton          : the filename prefix (Module / Activity / Tutorial / ...)
 *
 * Filename conventions this reads:
 *   Module 03 - Design Patterns      → lecture
 *   Activity 03 - Refactoring        → in-class activity
 *   Tutorial - Vitest                → tutorial
 *   Individual Project 2             → assignment
 *   <anything else>                  → plain note
 */

const fence = "```";

/* --- guard -------------------------------------------------------------
 * Templater fires on every file creation, including notes syncing down from
 * another device. Never overwrite a file that already has content. */
const preexisting = tp.file.content.trim().length > 0;

/* --- derive the course from the folder path ---------------------------- */
const segments = tp.file.folder(true).split("/");
const course   = segments[segments.indexOf("Courses") + 1] ?? "";
const isFolderNote = course && tp.file.title === course;

/* --- read the course MOC's frontmatter --------------------------------- */
let mocTags = [];
let semesterStart = null;
if (course && !isFolderNote && !preexisting) {
  const mocFile = app.metadataCache.getFirstLinkpathDest(course, tp.file.path(true));
  const moc = mocFile ? (app.metadataCache.getFileCache(mocFile)?.frontmatter ?? {}) : {};
  mocTags = [].concat(moc.tags ?? []).filter(t => !["hub", "moc", "index"].includes(t));
  semesterStart = moc.semester_start ?? null;
}

/* --- week number, blank before the semester starts --------------------- */
const start = semesterStart ? moment(semesterStart, "YYYY-MM-DD") : null;
/* Week 0 is the pre-semester stretch: syllabus is out, nothing has started.
 * Blank (no key at all) only when the course MOC has no semester_start. */
const week = !start || !start.isValid()               ? ""
  : moment().isSameOrAfter(start, "day")              ? Math.floor(moment().diff(start, "days") / 7) + 1
  :                                                     0;

/* --- classify from the filename ---------------------------------------- */
const title = tp.file.title;
const kind =
  /^(module|lecture|week|session)\b/i.test(title) ? "lecture" :
  /^topic\s+\d+\s*[-—:]/i.test(title)   ? "lecture"    :
  /^activity\b/i.test(title)          ? "activity"   :
  /^tutorial\b/i.test(title)          ? "tutorial"   :
  /\b(project|assignment|homework|ip\d)\b/i.test(title) ? "assignment" :
  /\b(exam|midterm|final|study guide)\b/i.test(title)   ? "exam"       :
                                        "note";

const numbered    = /^(?:module|lecture|activity|week|topic|session)\s+(\d+)/i;
const moduleNumber = ["lecture", "activity"].includes(kind) ? ((title.match(numbered) ?? [])[1] ?? "") : "";
const topic = title.replace(/^(?:module|lecture|activity|tutorial|week|topic|session)\s*\d*\s*[-—:]\s*/i, "").trim();
const slug  = topic.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

/* --- headings use an em dash; filenames can't ------------------------- */
const heading = title.replace(/\s+-\s+/, " — ");

/* --- assemble frontmatter ---------------------------------------------- */
const hasRealTopic = ["lecture", "activity", "tutorial"].includes(kind) && topic !== title;
const tags = [...new Set([kind, ...mocTags, hasRealTopic ? slug : ""].filter(Boolean))];
const fm = ["---", "tags:", ...tags.map(t => `  - ${t}`), `type: ${kind}`];
if (course)       fm.push(`course: "[[${course}]]"`);
if (moduleNumber) fm.push(`module: ${Number(moduleNumber)}`);
if (week !== "")  fm.push(`week: ${week}`);
if (["assignment", "exam"].includes(kind)) fm.push("due:");
fm.push(`date: ${tp.date.now("YYYY-MM-DD")}`, "status: raw", "---");

/* --- the folder note for a course is a MOC, not a course note ---------- */
const mocSkeleton = `---
tags:
  - ${course.toLowerCase().replace(/[^a-z0-9]+/g, "-")}
  - hub
type: moc
semester_start: ${tp.date.now("YYYY-MM-DD")}
---
# ${course}

${tp.file.cursor(1)}

%% Waypoint %%
`;

/* --- skeletons ---------------------------------------------------------- */
const context = course ? `${kind === "lecture" ? "Lecture" : "Note"} for [[${course}]].` : "";

const bodies = {
  lecture: `# ${heading}

${context} ${tp.file.cursor(1)}

## Learning Objectives

After this lecture you will be able to:

- ${tp.file.cursor(2)}

## Notes

${tp.file.cursor(3)}

> [!note] Definition
> **Term** — what it means, in your own words.

## Examples

### Worked Example

**Setup.** What the problem is.

${fence}
${tp.file.cursor(4)}
${fence}

**Why it works.** The reasoning, not just the answer.

## Key Takeaways

- ${tp.file.cursor(5)}

## Homework

- [ ] ${tp.file.cursor(6)}

## Open Questions

- 

## Resources

- Slides: 

## Related

- `,

  activity: `# ${heading}

In-class activity${course ? ` for [[${course}]]` : ""}. ${tp.file.cursor(1)}

## Scenario

${tp.file.cursor(2)}

## Requirements

1. ${tp.file.cursor(3)}

## My Work

${tp.file.cursor(4)}

## Takeaways

- 

## Related

- `,

  tutorial: `# ${heading}

Tutorial${course ? ` for [[${course}]]` : ""}. ${tp.file.cursor(1)}

## Setup

${fence}bash
${tp.file.cursor(2)}
${fence}

## Steps

1. ${tp.file.cursor(3)}

## Reference

${tp.file.cursor(4)}

## Gotchas

- 

## Related

- `,

  assignment: `# ${heading}

Assignment${course ? ` for [[${course}]]` : ""}. ${tp.file.cursor(1)}

**Due:** ${tp.file.cursor(2)}

- [ ] ${heading} 📅 ${tp.file.cursor(3)}

## Requirements

- [ ] ${tp.file.cursor(3)}

## Approach

${tp.file.cursor(4)}

## Notes While Working

- 

## Submission

- [ ] Submitted

## Related

- `,

  exam: `# ${heading}

${context} ${tp.file.cursor(1)}

**Format:** ${tp.file.cursor(2)}

## Topics Covered

- ${tp.file.cursor(3)}

## Weak Spots

- 

## Practice Questions

- 

## Related

- `,

  note: `# ${heading}

${context} ${tp.file.cursor(1)}

## Notes

${tp.file.cursor(2)}

## Related

- `,
};

/* --- single exit: pre-existing content wins, then folder notes, then skeletons */
tR = preexisting  ? tp.file.content
   : isFolderNote ? mocSkeleton
   :                fm.join("\n") + "\n" + bodies[kind];
%>

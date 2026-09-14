<%*
/* MOC Template — a manually applied hub note.
 *
 * The tag is slugified from the filename; nothing is typed twice. Folder notes
 * under Code/ and Courses/ get their MOC skeleton automatically from the
 * folder templates, so this one is for hubs that live outside those trees.
 */

/* Assembled at runtime: the Waypoint plugin scans the whole vault, and a bare
 * flag literal in this file would make it treat the template itself as a
 * waypoint host and overwrite it. */
const waypoint = `%% ${"Waypoint"} %%`;
const title = tp.config.target_file.basename;
const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

tR = `---
tags:
  - ${slug}
type: moc
---
# ${title}

${waypoint}
`;
%>

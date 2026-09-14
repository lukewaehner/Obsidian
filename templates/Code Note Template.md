<%*
/* Code Note Template — auto-applied to anything created under Code/.
 *
 * Replaces the eight near-identical per-language templates (Java, JavaScript,
 * Rust, Ruby, Rails, React, SQL, Swift). Those differed only in a tag, a fence
 * language, and a backlink — all three are derivable from the folder, so one
 * template covers every area under Code/, including the ones that never had
 * one (Algorithms, Computer Systems, TypeScript, OOD, Neovim, Zsh, Lazygit).
 *
 * The only thing you type is the filename. Everything else is derived:
 *   tags     : inherited from the nearest ancestor folder note that has them,
 *              falling back to the slugified area name (the folder directly
 *              under Code/)
 *   related  : the parent folder note — the most specific context the note sits in
 *   date     : today
 *
 * A note whose name matches its folder is a folder note, and gets a MOC
 * skeleton instead of a note skeleton.
 *
 * No tp.file.* and no cursor placeholders: the file is read through
 * tp.config.target_file, so nothing has to be tabbed through after creation.
 */

/* Assembled at runtime: the Waypoint plugin scans the whole vault, and a bare
 * flag literal in this file would make it treat the template itself as a
 * waypoint host and overwrite it. */
const waypoint = `%% ${"Waypoint"} %%`;
const ROOT = "Code";
const target = tp.config.target_file;

const slug = s => s.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

/* --- guard -------------------------------------------------------------
 * Templater fires on every file creation, including notes syncing down from
 * another device. Never overwrite a file that already has content. */
let existing = "";
try { existing = await app.vault.read(target); } catch (e) { existing = ""; }
const preexisting = existing.trim().length > 0;

/* --- walk the folder chain from the note up to (but not into) Code/ ----- */
const folder = target.parent;
const chain = [];
for (let d = folder; d && (d.path === ROOT || d.path.startsWith(`${ROOT}/`)); d = d.parent) {
  chain.push(d);
}

/* A folder note names itself after its folder, so its own folder note is the
 * file being created — start inheriting from the folder above it. */
const isFolderNote = folder.name === target.basename;
const inheritFrom = chain.slice(isFolderNote ? 1 : 0).filter(d => d.path !== ROOT);

/* The area is the folder directly under Code/ — the language or domain. */
const area = folder.path.split("/")[1] ?? "";

/* --- a folder's note lives inside it and shares its name --------------- */
const folderNote = d => {
  const f = d && app.vault.getAbstractFileByPath(`${d.path}/${d.name}.md`);
  return f && f.extension === "md" ? f : null;
};

/* --- tags: nearest ancestor folder note that declares any --------------- */
const STRUCTURAL = ["hub", "moc", "index"];
let tags = [];
for (const d of inheritFrom) {
  const note = folderNote(d);
  if (!note) continue;
  const fm = app.metadataCache.getFileCache(note)?.frontmatter ?? {};
  const inherited = [].concat(fm.tags ?? []).filter(t => t && !STRUCTURAL.includes(t));
  if (inherited.length) { tags = inherited; break; }
}
/* Nothing upstream declared tags (several area MOCs have no frontmatter yet),
 * so fall back to the area itself. */
if (!tags.length) tags = [slug(area || ROOT)];

/* --- related: the most specific context the note sits in ---------------
 * Nearest ancestor that actually has a folder note — some subfolders
 * (Code/Rust/HFT-Ledger) have none, so link past them rather than nothing. */
let related = "";
for (const d of chain.slice(isFolderNote ? 1 : 0)) {
  const note = folderNote(d);
  if (note) { related = note.basename; break; }
}

/* --- skeletons ---------------------------------------------------------- */
const note = `---
tags:
${tags.map(t => `  - ${t}`).join("\n")}
type: note
${related ? `related:\n  - "[[${related}]]"\n` : ""}date: ${moment().format("YYYY-MM-DD")}
---
# ${target.basename}

`;

const moc = `---
tags:
  - ${slug(target.basename)}
type: moc
${related ? `related:\n  - "[[${related}]]"\n` : ""}---
# ${target.basename}

${waypoint}
`;

/* --- single exit: pre-existing content wins, then folder notes ---------- */
tR = preexisting ? existing : isFolderNote ? moc : note;
%>


---
Cheat Sheet:
### Movement

| Keys                | Action                         |
| ------------------- | ------------------------------ |
| `h` / `l`           | Left / Right                   |
| `j` / `k`           | Down / Up                      |
| `w` / `e`           | Start / End of next word       |
| `b` / `ge`          | Start / End of previous word   |
| `{` / `}`           | Paragraph up / down            |
| `0` / `^`           | Line start / first non-blank   |
| `$`                 | Line end                       |
| `gg` / `G`          | File start / end               |
| `Ctrl-d` / `Ctrl-u` | Half-page down / up            |
| `Ctrl-o` / `Ctrl-i` | Jump back / forward in history |

---

### Searching

| Keys       | Action                              |
| ---------- | ----------------------------------- |
| `/pattern` | Search forward                      |
| `?pattern` | Search backward                     |
| `n` / `N`  | Next / Previous search result       |
| `*` / `#`  | Search word under cursor (fwd/back) |
| `%`        | Jump to matching `()[]{}`           |
| `s`        | Treesitter flash searching          |
| `grr`      | Shows LSP referesnces               |

---

### Editing

|Keys|Action|
|---|---|
|`i` / `a`|Insert before / after cursor|
|`o` / `O`|New line below / above|
|`x` / `X`|Delete char (forward/back)|
|`dd` / `yy`|Delete / yank (copy) line|
|`p` / `P`|Paste after / before|
|`u` / `Ctrl-r`|Undo / Redo|
|`.`|Repeat last edit|

---

### 📁 Files, Buffers, Splits

|Keys|Action|
|---|---|
|`:e file`|Edit (open) a file|
|`:w` / `:q`|Save / Quit|
|`:ls`|List open buffers|
|`:bnext` / `:bprev`|Switch buffers|
|`Ctrl-^`|Toggle between last two files|
|`:sp file` / `:vsp file`|Horizontal / vertical split|
|`Ctrl-w h/j/k/l`|Move between splits|
|`:tabnew` / `gt` / `gT`|New / next / prev tab|

---

### Treesitter

| Keys  | Actions                   |
| ----- | ------------------------- |
| `grr` | shows LSP refrences       |
| `grn` | Renames all lsp refrences |
| `gra` | shows fixes               |
| `gd`  | go to definition          |
| `grt` | go to type declartion     |
| `gri` | go to implementaiton      |

---

### Diagnostics

| Keys         | Actions                             |
| ------------ | ----------------------------------- |
| `<leader>sd` | Lists all diagnostics               |
| `<leader>cd` | Opens a window explaining the error |
| `]d`         | Go to next diagnostic               |
| `[d`         | Go to previous diagnostic           |
> Go to / find diagnostic, use `gra` to fix or `<leader>cd` to understand better

---

### Formatting

| Keys                       | Actions              |
| -------------------------- | -------------------- |
| `<leader>cf`               | Format file / buffer |
| `<leader>cd` (visual mode) | Formats selections   |

---

### Gitsigns

| Keys         | Actions              |
| ------------ | -------------------- |
| `]h`         | Next hunk (change)   |
| `[h`         | previous hunk        |
| `<leader>hp` | Inspect a change     |
| `<leader>hs` | stage hunk           |
| `<leader>hr` | reset hunk           |
| `<leader>hS` | stage buffer         |
| `<leader>hR` | rest buffer          |
| `<leader>hb` | shows blame for line |

---
tags:
  - neovim
  - vim
  - editor
type: moc
---
# Neovim

A hyperextensible, Lua-configured fork of Vim. Modal editing plus a real plugin ecosystem, LSP, and Treesitter built in.

## Core Vim

### Modes & Grammar
- [[Modes]] — Normal, insert, visual, visual-block, command, terminal
- [[Motions]] — `w`, `b`, `e`, `f`, `t`, `gg`, `G`, `%`, `{` / `}`
- [[Operators]] — `d`, `c`, `y`, `>`, `=` composed with motions
- [[Text Objects]] — `iw`, `ip`, `i"`, `a(`, `it` — the real superpower
- [[Counts and Repeats]] — `3dw`, `.`, registers, macros (`q`)

### Keybindings
- [[Keybinds]] — Personal cheat sheet for movement, search, edits, LSP, gitsigns
- [[Leader Key Mappings]] — `<leader>` conventions and namespaces

## Configuration

- [[Init Lua]] — `init.lua` entry point, structuring `lua/` modules
- [[Options]] — `vim.opt`, common settings (`number`, `expandtab`, `clipboard`)
- [[Keymaps]] — `vim.keymap.set`, modes, `desc`, `noremap`/`silent`
- [[Autocmds]] — `vim.api.nvim_create_autocmd`, augroups, `FileType` events
- [[Dotfiles]] — Managing config across machines, stow, bare git repo

## Plugins

- [[Plugin Management]] — `lazy.nvim` setup, lazy-loading, lockfile
- [[LSP]] — `nvim-lspconfig`, `mason.nvim`, capabilities, on_attach
- [[Treesitter]] — `nvim-treesitter`, parsers, highlights, text objects
- [[Telescope]] — Fuzzy finder for files, buffers, grep, LSP symbols
- [[Completion]] — `nvim-cmp`, sources, snippets (`LuaSnip`)
- [[Formatting and Linting]] — `conform.nvim`, `nvim-lint`
- [[Statusline]] — `lualine.nvim` configuration
- [[Common Plugins]] — `which-key`, `gitsigns`, `oil.nvim`, `flash.nvim`, `mini.*`

## Workflow

- [[Buffers Windows Tabs]] — Mental model and navigation
- [[Registers and Macros]] — Named registers, recording reusable macros
- [[Search and Replace]] — `/`, `:s`, quickfix list

## Reference

- [[Neovim Cheat Sheet]] — Movement, edits, and command quick lookup

## Quick Reference

```lua
vim.g.mapleader = " "
vim.opt.number = true
vim.opt.expandtab = true

vim.keymap.set("n", "<leader>w", ":w<CR>", { desc = "Save file" })

vim.api.nvim_create_autocmd("BufWritePre", {
  pattern = "*.lua",
  callback = function() vim.lsp.buf.format() end,
})

-- lazy.nvim plugin spec
{
  "nvim-telescope/telescope.nvim",
  dependencies = { "nvim-lua/plenary.nvim" },
  keys = { { "<leader>ff", "<cmd>Telescope find_files<cr>" } },
}
```

## Resources

- [Neovim Docs](https://neovim.io/doc/)
- `:help` — the real manual, always start here
- [Awesome Neovim](https://github.com/rockerBOO/awesome-neovim)
- [LazyVim](https://www.lazyvim.org/) — reference distro

## See Also

- [[Tools]] — Other dev tooling
- [[Code]] — Main programming hub

%% Begin Waypoint %%
- [[Neovim Cheat Sheet]]

%% End Waypoint %%

---
name: vscode-dark-pdf-macos
description: Configure Visual Studio Code for dark PDF viewing in LaTeX Workshop on macOS and Ubuntu, with right-side PDF tabs, source wrap, and optional LaTeX squiggle suppression.
---

# VS Code Dark PDF on macOS and Ubuntu

## Overview

Use LaTeX Workshop's internal PDF viewer first. Keep the configuration minimal and deterministic so the dark-viewer path stays predictable across macOS and Ubuntu.

For Overleaf-like editing, treat source-editor soft wrap as part of the workflow. If a `.tex` tab does not wrap to the current pane width, fix editor settings rather than rewriting LaTeX lines for display.

If the user only wants distracting red or yellow LaTeX squiggles to disappear inside the editor, prefer workspace editor settings for `latex` first and keep LaTeX Workshop-specific lint or message keys at default unless there is a proven need to change them.

## Quick Start

1. Apply the baseline settings with the script:

```bash
python3 scripts/apply_vscode_dark_pdf.py --invert 0.85
```

2. If the `.tex` source editor does not wrap long lines, or the user wants editor squiggles hidden without changing the document body, add or update workspace `.vscode/settings.json` with:

```json
{
  "[latex]": {
    "editor.wordWrap": "on",
    "editor.renderValidationDecorations": "off"
  }
}
```

Prefer workspace editor settings over a temporary toggle when the user wants durable Overleaf-like behavior for the project.

Use `editor.renderValidationDecorations = "off"` only for `latex`, not globally. This hides inline squiggles in the editor without requiring `.tex` cleanup.

3. If `tomoki1207.pdf` is installed, uninstall it:

```bash
code --uninstall-extension tomoki1207.pdf
```

4. Reopen the PDF from a fresh pathname inside VS Code.

On the validated Ubuntu path, reopening the PDF after applying the baseline settings was sufficient; a full VS Code restart was not required.

5. If the PDF is still bright, relaunch VS Code once with GPU disabled and open the `.tex` file plus a fresh-path PDF copy:

```bash
code --disable-gpu "/path/to/file.tex" "/path/to/fresh-copy.pdf"
```

6. Confirm the PDF opens on the right, the LaTeX source wraps inside its pane, and the PDF renders dark inside VS Code.

## Baseline Settings

The script enforces only these settings:

- `latex-workshop.view.pdf.invertMode.enabled = "always"`
- `latex-workshop.view.pdf.invert = <value>`
- `latex-workshop.view.pdf.viewer = "tab"`
- `latex-workshop.view.pdf.tab.editorGroup = "right"`
- `workbench.editorAssociations["*.pdf"] = "latex-workshop-pdf-hook"`

The script removes these keys if present because they commonly interfere with this route:

- `latex-workshop.view.pdf.color.light.pageColorsBackground`
- `latex-workshop.view.pdf.color.light.pageColorsForeground`
- `latex-workshop.view.pdf.color.light.backgroundColor`
- `latex-workshop.view.pdf.color.light.pageBorderColor`
- `latex-workshop.view.pdf.color.dark.pageColorsBackground`
- `latex-workshop.view.pdf.color.dark.pageColorsForeground`
- `latex-workshop.view.pdf.color.dark.backgroundColor`
- `latex-workshop.view.pdf.color.dark.pageBorderColor`
- `latex-workshop.view.pdf.invertMode.grayscale`

## Workflow

- Prefer LaTeX Workshop's internal viewer to preserve the Overleaf-style split view.
- Prefer workspace-level `[latex].editor.wordWrap = "on"` when the user wants the source editor to behave like Overleaf. Use `Option+Z` only as a quick temporary check.
- If the user says the file compiles but the editor is covered with distracting squiggles, prefer `[latex].editor.renderValidationDecorations = "off"` over changing document content.
- Keep `latex-workshop.message.*`, `latex-workshop.linting.*`, and similar extension-specific suppression keys at default unless troubleshooting shows a concrete need to change them.
- Use a fresh PDF pathname when retesting. Restored webviews can keep stale state.
- Start from `--invert 0.85` as the default initial value. It is a good first try when the user wants a dark PDF that is less harsh than full-strength inversion.
- If the user says contrast is still too high or too low, rerun the script with a nearby `--invert` value such as `0.80`, `0.90`, or `0.92`.
- On the validated Ubuntu path, first reopen the PDF from a fresh pathname before escalating to a full VS Code relaunch.
- If the PDF stays white, relaunch once with `--disable-gpu` before changing extensions.
- If the PDF is still white after a fresh GPU-disabled launch, treat the LaTeX Workshop dark-view path as unstable on that machine/version before trying third-party PDF viewers.

## Troubleshooting

- Long source lines run off the visible pane: this is usually an editor-wrap issue, not a LaTeX issue. First set workspace `.vscode/settings.json` to `[latex].editor.wordWrap = "on"`. Use `Option+Z` only to confirm the diagnosis.
- Inline red or yellow LaTeX squiggles are distracting but the file otherwise works: restore any experimental LaTeX Workshop suppression keys to default, then hide editor decorations with `[latex].editor.renderValidationDecorations = "off"` in workspace `.vscode/settings.json`.
- Conflict warning mentioning `vscode-pdf`: uninstall `tomoki1207.pdf`.
- PDF opens in the wrong pane: verify `latex-workshop.view.pdf.tab.editorGroup = "right"`.
- PDF opens but remains bright: first make sure the test used a new PDF path. On the validated Ubuntu path, a full VS Code restart was not required; if it remains bright, then try a GPU-disabled relaunch.
- Keep the official invert route and minimal settings as the starting point; add custom dark color keys only if later troubleshooting specifically requires them.
- Treat reset-to-default or "start over" as one troubleshooting method, not as a principle.
- Suggest reset only after repeated failed tweaks. The user decides whether to proceed. Before any reset, warn clearly, require two explicit confirmations, and confirm either that a backup exists or that the reset is low-risk or irrelevant.

# vscode-dark-pdf-macos

A `Codex App` skill for configuring Visual Studio Code for dark PDF viewing with LaTeX Workshop on macOS and Ubuntu, with right-side PDF tabs, source wrap, SyncTeX source/PDF alignment, and optional LaTeX squiggle suppression.

Chinese mirror: [README.zh-CN.md](README.zh-CN.md)

## What Ships

- `vscode-dark-pdf-macos/`: installable Codex App skill package
- `vscode-dark-pdf-macos/scripts/apply_vscode_dark_pdf.py`: helper script for applying the baseline VS Code settings on macOS or Ubuntu
- `vscode-dark-pdf-macos/agents/openai.yaml`: Codex App metadata

## Install

1. Copy `vscode-dark-pdf-macos/` into `${CODEX_HOME:-$HOME/.codex}/skills/`.
2. Restart Codex App or refresh local skills.
3. Invoke the skill as `$vscode-dark-pdf-macos`.

## Use Cases

Ask Codex App to:

- configure dark PDF viewing in VS Code on macOS or Ubuntu with LaTeX Workshop
- keep the PDF in the right-side tab and use the internal viewer
- enable `.tex` soft wrap without rewriting document lines
- jump from PDF to source by double-click and sync from source to PDF with `Ctrl+Alt+J`
- hide distracting LaTeX squiggles through workspace settings
- distinguish spell-checker language mismatches from real LaTeX diagnostics when words are underlined
- troubleshoot white PDF rendering, stale PDF paths, missing `.synctex.gz`, and `vscode-pdf` extension conflicts

## Validated Note

- On the validated Ubuntu path, reopening the PDF from a fresh pathname after applying the baseline settings was sufficient; a full VS Code restart was not required.
- On the validated Ubuntu path, workspace `.vscode/settings.json` with `[latex].editor.wordWrap = "on"` also worked without restarting VS Code.
- The helper script now sets reverse SyncTeX in the internal PDF viewer to `double-click`.
- Reverse SyncTeX also requires a sibling `.synctex.gz` file beside the PDF. If the user is still on LaTeX Workshop's default `Build LaTeX project` path, SyncTeX is normally already included. If the project uses custom tools, custom recipes, or an external build script, keep `-synctex=1` on every build rather than treating it as a one-time fix.
- If the PDF stays bright, the next fallback is a single `--disable-gpu` relaunch.
- If ordinary words are underlined but the file compiles, first check the spell-checker language for the file or workspace, for example selecting `English` in `Spell Right`, before changing LaTeX diagnostics settings.

## Trigger Examples

- `Configure dark PDF viewing in VS Code on Ubuntu with LaTeX Workshop.`
- `Make VS Code behave more like Overleaf for .tex editing plus PDF preview.`
- `Enable PDF double-click back to source in the LaTeX Workshop viewer.`
- `My PDF is still white in VS Code. Walk me through the dark-viewer path.`

## Privacy Boundary

This repository ships only the portable skill logic and helper script. It does not include private memory files, local personal paths, private context files, or user-specific workflow dependencies.

## Repository Layout

- `vscode-dark-pdf-macos/`: Codex App skill package
- `README.md`: English overview
- `README.zh-CN.md`: Chinese overview
- `LICENSE`: MIT license
- `CHANGELOG.md`: release history

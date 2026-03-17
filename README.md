# vscode-dark-pdf-macos

A `Codex App` skill for configuring Visual Studio Code for dark PDF viewing with LaTeX Workshop on macOS and Ubuntu, with right-side PDF tabs, source wrap, and optional LaTeX squiggle suppression.

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
- hide distracting LaTeX squiggles through workspace settings
- troubleshoot white PDF rendering, stale PDF paths, and `vscode-pdf` extension conflicts

## Validated Note

- On the validated Ubuntu path, reopening the PDF from a fresh pathname after applying the baseline settings was sufficient; a full VS Code restart was not required.
- If the PDF stays bright, the next fallback is a single `--disable-gpu` relaunch.

## Trigger Examples

- `Configure dark PDF viewing in VS Code on Ubuntu with LaTeX Workshop.`
- `Make VS Code behave more like Overleaf for .tex editing plus PDF preview.`
- `Hide LaTeX squiggles in this workspace without changing the document body.`
- `My PDF is still white in VS Code. Walk me through the dark-viewer path.`

## Privacy Boundary

This repository ships only the portable skill logic and helper script. It does not include private memory files, local personal paths, private context files, or user-specific workflow dependencies.

## Repository Layout

- `vscode-dark-pdf-macos/`: Codex App skill package
- `README.md`: English overview
- `README.zh-CN.md`: Chinese overview
- `LICENSE`: MIT license
- `CHANGELOG.md`: release history

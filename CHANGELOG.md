# Changelog

## 0.1.6 - 2026-03-18

- Document that LaTeX Workshop's default `Build LaTeX project` path normally already includes SyncTeX.
- Clarify that explicit `-synctex=1` is still required for custom tools, custom recipes, or external build scripts.
- Keep the validated Ubuntu `.tex` soft-wrap note visible alongside the SyncTeX workflow guidance.

## 0.1.5 - 2026-03-18

- Document that some `.tex` underlines come from spell-checker language mismatch rather than LaTeX diagnostics.
- Add a concrete troubleshooting note to check spell-checker language selection first, for example choosing `English` in `Spell Right`.

## 0.1.4 - 2026-03-18

- Treat `-synctex=1` as an every-build requirement for the validated source/PDF alignment workflow.
- Update the docs and helper output so users do not mistake SyncTeX as a one-time recovery flag.

## 0.1.3 - 2026-03-18

- Merge the validated SyncTeX source/PDF alignment workflow into the skill.
- Set `latex-workshop.view.pdf.internal.synctex.keybinding = "double-click"` in the helper script.
- Document reverse SyncTeX from PDF double-click, forward SyncTeX from source with `Ctrl+Alt+J`, and the requirement for a sibling `.synctex.gz` file.

## 0.1.2 - 2026-03-18

- Document the validated Ubuntu workspace soft-wrap path using `[latex].editor.wordWrap = "on"`.
- Note that this workspace-level `.tex` soft-wrap setting also took effect without restarting VS Code on the validated Ubuntu path.

## 0.1.1 - 2026-03-18

- Adapt the helper script to auto-detect macOS and Ubuntu VS Code settings paths.
- Remove both light and dark custom PDF color keys before applying the minimal LaTeX Workshop dark-viewer baseline.
- Update the skill and README docs to note the validated Ubuntu path, fresh-path reopening workflow, and that a full VS Code restart was not required there.

## 0.1.0 - 2026-03-18

- First public release of the `vscode-dark-pdf-macos` Codex App skill.

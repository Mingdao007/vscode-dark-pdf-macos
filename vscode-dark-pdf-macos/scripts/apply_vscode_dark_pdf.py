#!/usr/bin/env python3
"""Apply a minimal LaTeX Workshop dark-PDF configuration for macOS or Ubuntu VS Code."""

from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path


REMOVE_KEYS = [
    "latex-workshop.view.pdf.color.light.pageColorsBackground",
    "latex-workshop.view.pdf.color.light.pageColorsForeground",
    "latex-workshop.view.pdf.color.light.backgroundColor",
    "latex-workshop.view.pdf.color.light.pageBorderColor",
    "latex-workshop.view.pdf.color.dark.pageColorsBackground",
    "latex-workshop.view.pdf.color.dark.pageColorsForeground",
    "latex-workshop.view.pdf.color.dark.backgroundColor",
    "latex-workshop.view.pdf.color.dark.pageBorderColor",
    "latex-workshop.view.pdf.invertMode.grayscale",
]


def default_settings_path() -> Path:
    system = platform.system()
    if system == "Darwin":
        return Path.home() / "Library/Application Support/Code/User/settings.json"
    return Path.home() / ".config/Code/User/settings.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Apply a minimal VS Code + LaTeX Workshop dark PDF setup."
    )
    parser.add_argument(
        "--settings",
        default=str(default_settings_path()),
        help="Path to the VS Code user settings.json file.",
    )
    parser.add_argument(
        "--invert",
        type=float,
        default=0.85,
        help="LaTeX Workshop invert value between 0 and 1. Default: 0.85",
    )
    parser.add_argument(
        "--editor-group",
        default="right",
        choices=["current", "left", "right", "above", "below"],
        help="Target editor group for the PDF tab. Default: right",
    )
    return parser.parse_args()


def load_settings(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return data


def main() -> int:
    args = parse_args()
    if not 0 <= args.invert <= 1:
        raise ValueError("--invert must be between 0 and 1")

    settings_path = Path(args.settings).expanduser()
    settings_path.parent.mkdir(parents=True, exist_ok=True)

    settings = load_settings(settings_path)

    for key in REMOVE_KEYS:
        settings.pop(key, None)

    associations = settings.get("workbench.editorAssociations")
    if associations is None:
        associations = {}
    elif not isinstance(associations, dict):
        raise ValueError("workbench.editorAssociations must be a JSON object")
    associations["*.pdf"] = "latex-workshop-pdf-hook"
    settings["workbench.editorAssociations"] = associations

    settings["latex-workshop.view.pdf.invertMode.enabled"] = "always"
    settings["latex-workshop.view.pdf.invert"] = args.invert
    settings["latex-workshop.view.pdf.viewer"] = "tab"
    settings["latex-workshop.view.pdf.tab.editorGroup"] = args.editor_group
    settings["latex-workshop.view.pdf.internal.synctex.keybinding"] = "double-click"

    with settings_path.open("w", encoding="utf-8") as fh:
        json.dump(settings, fh, indent=4, ensure_ascii=True)
        fh.write("\n")

    print(f"Updated {settings_path}")
    print(f"latex-workshop.view.pdf.invert = {args.invert}")
    print("Reverse SyncTeX in the PDF viewer is set to double-click.")
    print("Next step: reopen the PDF from a fresh pathname inside VS Code.")
    print("If reverse SyncTeX does nothing, confirm a sibling .synctex.gz file exists.")
    print("If it stays bright, relaunch once with --disable-gpu.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

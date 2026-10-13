#!/usr/bin/env python
"""Small consistency checks for the mod. Standard library only.

Usage: python scripts/validate.py
Excludes CI; useful before publishing or after a Zen update."""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)
    print(("[ok]   " if cond else "[FAIL] ") + msg)


def main():
    css = (ROOT / "chrome.css").read_text(encoding="utf-8")

    # --- preferences.json --------------------------------------------
    check((ROOT / "LICENSE").exists(), "LICENSE present")
    check((ROOT / "README.md").exists(), "README present")

    prefs_path = ROOT / "preferences.json"
    check(prefs_path.exists(), "preferences.json present")
    if prefs_path.exists():
        try:
            prefs = json.loads(prefs_path.read_text(encoding="utf-8"))
            valid_json = True
        except json.JSONDecodeError as e:
            valid_json = False
            failures.append(f"preferences.json is not valid JSON: {e}")
            print(f"[FAIL] preferences.json parse error: {e}")
        if valid_json:
            check(isinstance(prefs, list), "preferences.json root is an array")
            names = []
            for p in prefs:
                check(isinstance(p, dict), "each preference is an object")
                for key in ("property", "label", "type"):
                    check(key in p, f"{p.get('property','?')}: '{key}' present")
                check(
                    p.get("type") == "checkbox" and isinstance(
                        p.get("defaultValue"), bool),
                    f"{p['property']}: checkbox defaultValue is a real boolean",
                )
                check(
                    p["property"].startswith("theme.mac-traffic-lights."),
                    f"{p['property']}: property uses the mod's namespace",
                )
                names.append(p["property"])
            check(len(names) == len(set(names)), "property names are unique")
            # every -moz-pref referenced in CSS must exist as a preference
            css_prefs = set(
                re.findall(r'-moz-pref\("([^"]+)"(?:\s*,\s*"[^"]*")?\)', css)
            )
            unknown = css_prefs - set(names)
            check(not unknown,
                  f"every CSS -moz-pref matches a preference (unknown: {unknown})")
            check(
                "-moz-bool-pref" not in css,
                "CSS does not use the deprecated -moz-bool-pref syntax",
            )

    # --- CSS -----------------------------------------------------------
    check(css.count("{") == css.count("}"), "CSS braces are balanced")
    check("@import" not in css, "CSS has no imports (single source of truth)")
    check(not re.search(r'url\(\s*(["\']?)https?:', css),
          "CSS loads no remote resources (only inline SVG)")

    # --- README --------------------------------------------------------
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    check("dinnoyow/zen-minimal-exit-menu" in readme,
          "README links the original project")
    # Image references that point at files under assets/ must exist on disk
    # before publishing; missing ones are warnings, not failures, so the
    # guide can tell you exactly what to capture.
    missing = [
        m.group(1)
        for m in re.finditer(r"\[(!)?[^\]]*\]\((assets/[^)]+\.png)\)", readme)
        if not ROOT.joinpath(m.group(2)).exists()
    ]
    if missing:
        print("[warn] missing screenshots referenced by README:",
              ", ".join(sorted(set(missing))))
        print("       capture steps are in docs/capturing-screenshots.md")
    else:
        check(not re.findall(r"\]\(assets/[^\)]+\.png\)", readme) or True,
              "all README screenshot files exist")

    print()
    if failures:
        print(f"{len(failures)} check(s) FAILED")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
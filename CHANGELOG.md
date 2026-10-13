# Changelog

## Unreleased

- Hover marks now appear and disappear instantly (the 100 ms fade was
  removed), making movement between the discs feel immediate and
  macOS-like

## 0.1.0-beta

Rework of [dinnoyow/zen-minimal-exit-menu](https://github.com/dinnoyow/zen-minimal-exit-menu)
(last upstream change: 2024-11-27), modernized for Zen 1.23.2b (Firefox 157.0.1).

Fixed
- Color-to-function mapping was inverted: minimize was green and
  maximize yellow; now close is red, minimize yellow, zoom green
- Hover marks and disc rendering rewritten for the Firefox 157 glyph
  model (text no longer leaks into the discs)
- `preferences.json`: root was `{ { … } }` (invalid); it is now an
  array, `defaultValue` values are real booleans, and CSS reads
  preferences via the current `-moz-pref()` syntax instead of the
  deprecated `-moz-bool-pref`

Changed
- Full visual rework to measured macOS values: 12px discs, 8px gap,
  close/minimize/zoom order matching macOS regardless of Zen toolbar
  layout (flex `order`, no DOM changes)
- Visibility rides Zen's stock auto-hidden top bar
  (`zen.view.hide-window-controls`, on by default): the group is
  invisible while the toolbar is collapsed, expands with it on a
  top-edge hover, and collapses again with it — no independent hover
  mechanism; the group stays anchored at the top-right of whichever
  row Zen places it in
- Group hover reveal, subtle press tint, inactive-window gray state
- Buttons/marks re-laid out for how Gecko 157 actually renders these
  XUL buttons (`::after` does not paint there, verified — the mark
  layer lives on `::before` and the discs are layered radial-gradient
  backgrounds)
- Windows Snap Layouts kept working (`-moz-default-appearance` left
  untouched); the mod is fully disabled on macOS

Added
- Two preferences: fall back to native controls, hide hover glyphs
- `scripts/validate.py` consistency checks
- `assets/preview.html` design preview (light/dark, states)
- Testing and screenshot capture guides, Zen Mods submission kit
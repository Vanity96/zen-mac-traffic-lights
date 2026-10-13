# Testing guide

What was verified by the developer, and what still needs eyes. Update
the "Status" column as you test on your machine.

## Static checks (automated, run here)

`python scripts/validate.py` — preferences schema, CSS braces, no
deprecated syntax, no remote assets, README/attribution links.
Status: **passed** in this repository at time of writing.

## Functional checks (needs a running Zen Browser)

Statuses filled from automated testing on the developer's machine:
Windows 11, Zen 1.23.2b (Firefox 157), 100% DPI, vertical tabs,
single-toolbar layout, dark theme. Anything not run on that setup is
marked accordingly — do not treat the ☐ rows as passing anywhere.

| Check | How | Status |
|---|---|---|
| Red closes the window | click the red disc on a test window | ✅ Verified — process terminated |
| Yellow minimizes | click yellow; window must minimize, not close | ✅ Verified — `IsIconic` true, window alive |
| Green maximizes | click green restored → maximized | ✅ Verified — `IsZoomed` true |
| Green restores | click green again while maximized | ✅ Verified — `IsZoomed` false |
| Hidden by default | auto-hidden toolbar collapsed | ✅ Verified — 0 disc pixels in captures |
| Top-edge hover reveals | hover near top edge | ✅ Verified — discs render inside the expanded toolbar, top-right (centers ≈ 74/54/34 px from the right edge, y ≈ 18) |
| Hides again after hover | move the cursor away | ✅ Verified — 0 disc pixels after collapse |
| Hover reveals all three glyphs | hover the group, capture | ✅ Verified — ×, −, and double-triangle marks (visual) |
| Restore glyph mirrors while zoomed | maximize, hover, capture | ✅ Verified — inward-pointing triangles |
| Discs are round and even | pixel scan of captures | ✅ Verified — no ellipses; straight baseline through centers |
| Order close/min/zoom | left to right | ✅ Verified — pixel positions |
| Fullscreen unaffected | F11 still fullscreens; controls hidden in fullscreen | ☐ Not tested (rule `:root[inFullscreen]` present; Zen also drops the strip in fullscreen) |
| Resize & Snap Layouts | drag the maximize button up/down on Win11; layout flyout appears | ☐ Not tested |
| Title bar still drags | drag empty toolbar space to move window | ☐ Not tested |
| Hover in single-toolbar vs multi-toolbar | change Zen toolbar layout | ☐ Not tested (single-toolbar only) |
| Compact mode | Zen Settings → compact mode | ☐ Not tested |
| Sidebar left and right | toggle sidebar position | ☐ Not tested |
| Vertical tabs on both sides | same | ☐ Not tested |
| Narrow windows | shrink to ~600px wide | ☐ Not tested |
| Inactive window | all discs gray when unfocused | ⚠ Not verified — the graying rule is present and `:-moz-window-inactive` is used by Zen itself, but Gecko did not repaint the test window while unfocused, so the state could not be captured (see note below) |
| Light / dark theme | toggle themes | ⚠ Partially verified — dark theme captured; light theme rules present but not captured |
| HiDPI | Windows scaling 125–200% | ☐ Not tested — sizes are CSS px, expected to scale; not confirmed on real HiDPI |
| Mixed-DPI monitors | drag between displays | ☐ Not tested |

### Why the inactive-window check is not verified

Firefox pauses painting for the unfocused window in this setup: after
taking focus away, screen grabs and `PrintWindow` both return the last
active frame (the two captures were byte-identical), and even forcing a
resize through `MoveWindow` did not trigger a repaint. So the styling
could never be observed. The rule itself is plain
`:root:-moz-window-inactive { --mtl-button-fill: … }`, and Zen's own
stylesheets use the pseudo-class heavily, so it should behave like the
stock gray-out — but treat it as unconfirmed until someone with a
second display or a manual focus switch checks it.

## DPI note

Sizes are in CSS px so they scale with Windows DPI like normal UI:
logical 12px discs at 200% = 24 physical px, same apparent size. The
`0.5px` rim lands on an exact device pixel at whole-number scalings
(100%, 125%, 150%, 200%); on 175% or dragging between mixed-DPI
monitors it may anti-alias softly — matches macOS behavior roughly,
cosmetic only.

## Loading the mod locally for testing

Fastest loop (no install needed):

1. Enable `zen.mod.debug` style user chrome: Settings → General →
   (or `zen://config` → `zen.themes.user-chrome-enabled`, depends on
   version), and place `chrome.css` in your profile's `chrome/` folder,
   or
2. Package the folder as a zip and load it like a theme per
   https://docs.zen-browser.app/guides/using-themes

For live editing, open the Browser Toolbox (Menu → More tools →
Browser Toolbox) and paste `chrome.css` into the Style Editor — see
https://docs.zen-browser.app/guides/live-editing
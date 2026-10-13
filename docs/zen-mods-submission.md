# Zen Mods submission kit

Everything below is ready to paste into the submission form/template
when you decide to submit. Nothing here submits anything for you.

## Registry status check (as of writing, 2026-10)

- `zen-browser/theme-store` — archived 2026-07-23. The submission
  guidelines on the docs site still describe creating an issue in that
  repo, but the repository is read-only. **Verify the active channel
  before submitting** (check https://zen-browser.app/mods/ and
  https://github.com/zen-browser/desktop for the current process).
  Catalog at https://zen-browser.app/mods/ still serves mods whose
  screenshots are hosted under the archived repo.
- Known historical requirements: name < 25 chars, description < 100
  chars, 600×400 PNG, open source, valid README, valid preferences.

## Prepared texts

**Name** (18 chars): `Mac Traffic Lights`

**Short description** (65 chars):
`Native-style macOS traffic-light window controls for Zen Browser.`

**Longer description:**
`Restyles Zen's window buttons on Windows and Linux as macOS traffic
lights: close red, minimize yellow, zoom green, 12px discs at native
spacing, hover marks, and a neutral gray state for inactive windows.
A careful rework of Zen Minimal Exit Menu by DinnoDEV for Zen 1.23.`

**Repository:** `https://github.com/Vanity96/zen-mac-traffic-lights` (created on publish)
**Entry point:** `chrome.css` at repo root
**Preferences:** 2 checkboxes (`theme.mac-traffic-lights.native`,
`theme.mac-traffic-lights.hide-glyphs`), schema validated by
`scripts/validate.py`
**License:** MIT (original copyright DinnoDEV preserved, see `LICENSE`)
**Screenshot:** `assets/registry-600x400.png` (must be captured first — see docs/capturing-screenshots.md)

## Checklist before submitting

- [ ] Screenshots captured from the real mod (docs/capturing-screenshots.md)
- [ ] Manual functional testing done (docs/testing-guide.md)
- [ ] Release published (see the release notes template there)
- [ ] Current submission channel re-verified (theme-store was archived;
      find the live channel)
- [ ] Preferences text pasted into the form as JSON, exactly as in
      `preferences.json`

Do not claim testing you didn't run; the registry team rejects mods
that misstate compatibility.
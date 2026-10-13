# Zen Mods submission kit

Everything below is ready to paste into the submission form/template
when you decide to submit. Nothing here submits anything for you.

## Registry status check (verified 2026-10-13)

- The **documented** channel is the official guidelines page:
  https://docs.zen-browser.app/themes-store/themes-marketplace-submission-guidelines
  — it still instructs opening a `[create-theme]: ` issue in
  `zen-browser/theme-store` (template `.github/ISSUE_TEMPLATE/create-theme.yml`,
  fields: name, description, homepage URL, image URL (PNG), styles
  (CSS/JSON), README, preferences). A bot then opens the PR.
- **But that channel is closed right now:** `zen-browser/theme-store`
  is archived (verified via the GitHub API, `archived: true`; last push
  2026-07-23, last `[create-theme]` issues from 2026-07, none since).
  A Zen maintainer confirmed in
  [theme-store#928](https://github.com/zen-browser/theme-store/issues/928)
  (2026-02) that mods are under a *soft freeze* pending a rework of the
  submission workflow. No replacement venue exists in the
  [zen-browser org](https://github.com/orgs/zen-browser/repositories)
  as of 2026-10-13 (checked every repo; nothing newer).
- Practical conclusion: **wait**. Before submitting, re-check the
  docs page, the archived repo, and
  [desktop discussions](https://github.com/zen-browser/desktop/discussions)
  for the new workflow. Nothing about this kit needs to change unless
  the new channel uses a different template.

- Requirements (unchanged in docs): name < 25 chars
  (`Mac Traffic Lights` = 18), description < 100 chars, 600×400 PNG,
  open source, valid README, valid preferences.

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
**Screenshot:** `assets/registry-600x400.png` (captured from the running mod — see docs/capturing-screenshots.md)

## Checklist before submitting

- [ ] Screenshots captured from the real mod (docs/capturing-screenshots.md)
- [ ] Manual functional testing done (docs/testing-guide.md)
- [x] Releases published: [v0.1.0-beta](https://github.com/Vanity96/zen-mac-traffic-lights/releases/tag/v0.1.0-beta)
      and [v0.1.1](https://github.com/Vanity96/zen-mac-traffic-lights/releases/tag/v0.1.1)
      (2026-10-13)
- [ ] Submission: **not submitted — awaiting the registry channel to
      reopen** (see status above; still frozen as of 2026-10-13)
- [ ] Preferences text pasted into the form as JSON, exactly as in
      `preferences.json`

Do not claim testing you didn't run; the registry team rejects mods
that misstate compatibility.
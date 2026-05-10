# Contributing

Pull requests welcome. A few guidelines.

## Voice and tone

- **Direct, technical, occasionally dry.** Prefer "this control sets X" over
  "you can use this control to set X".
- **Author from experience.** If a behaviour isn't documented in the
  official manual, name the source (Elektronauts thread, community
  reference, personal testing) inline or in a footnote.
- **No marketing language.** Avoid "powerful", "intuitive", "cutting-edge".
  The Octatrack speaks for itself.
- **British or American English** consistently within a chapter; the
  existing chapters use British spelling ("colour", "behaviour"). Stick
  to that.

## Structure

Each chapter is a standalone HTML fragment in `chapters/`. Filename
prefix determines order:

- `00–02` front matter (cover, colophon, TOC)
- `03–05` orientation (philosophy, hardware tour, rear panel)
- `06+` numbered chapters per the TOC structure

Use `<section class="chapter" data-running="N · Title">…</section>` as the
outer wrapper. The `data-running` attribute drives the running header.

## Code conventions

- HTML: 2-space indent, semantic tags (`<h1>`–`<h3>`, `<p>`, `<ul>`,
  `<dl>`)
- CSS: changes to design tokens go in `styles/main.css`; component-level
  styles in `components.css`; page rules in `print.css`
- SVG: viewBox-based sizing; CSS variables for colour where possible

## Components

Shared components are in `styles/components.css`:

- `<div class="callout note|tip|warn|secret">` — coloured sidebars
- `<kbd>FUNCTION</kbd>`, `<kbd class="fn">…</kbd>`, `<kbd class="trig">…</kbd>`
- `<span class="param">PTCH</span>` — parameter names
- `<div class="screen-mock">…</div>` — VT323-styled LCD mockups
- `<div class="recipe">…</div>` — performance recipe boxes
- `<span class="dc">T</span>` — drop-cap (chapter openers only)

## Building

```bash
python3 build/build.py
```

Inspect the generated PDF in `build/octatrack-mk1-manual.pdf` before
committing.

## Naming

The author's GitHub handle is `jordanaftermidnight`. Don't add additional
attributions ("Co-authored-by", "with help from", etc.) to commits.

## Erratum

Open an issue with:

- Page reference (chapter, section)
- The current text or behaviour described
- The corrected text or behaviour, with source if known

Or open a PR directly with the fix.

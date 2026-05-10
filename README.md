# Octatrack MK1 — Reworked Manual

An unofficial, community-oriented rework of the Elektron Octatrack MK1 manual.
Authored by **jordanaftermidnight**.

Built as a single-source HTML/CSS document rendered to PDF via WeasyPrint
(Paged Media spec).

## Status

- **First edition · work in progress**
- **24 numbered chapters + 3 appendices written**, covering Parts I–XI
  of the planned outline plus the first three reference appendices
- 5 SVG illustrations: front/rear panels (full-detail schematic),
  data hierarchy, signal flow, Pickup state machine
- Planned next: expanding Part XI (recipes) from one chapter into
  several; additional appendices (FX parameter tables, MIDI implementation
  chart, CF specs, OS history); screen mockups for individual parameter
  pages; additional SVG diagrams (LFO shapes, scene morph, sample chain
  anatomy)

## Structure

```
.
├── chapters/                            HTML source for each section
│   ├── 00-cover.html
│   ├── 01-colophon.html
│   ├── 02-toc.html
│   ├── 03-philosophy.html               Part I  · Why this manual
│   ├── 04-hardware-tour.html            Part II · Top panel anatomy
│   ├── 05-rear-panel.html               Part II · Rear panel
│   ├── 06-data-hierarchy.html           Part III · Sets, projects, banks, parts
│   ├── 07-audio-pool.html               Part III · Audio Pool, Static, Flex
│   ├── 08-signal-flow.html              Part III · 8 tracks + master + signal flow
│   ├── 09-trigs-plocks.html             Part IV · Trigs and parameter locks
│   ├── 10-microtiming-conditions.html   Part IV · Microtiming, conditional trigs
│   ├── 11-trig-modes.html               Part IV · Trig modes
│   ├── 12-live-record.html              Part IV · Live record and preview
│   ├── 13-static-flex.html              Part V · Static and Flex machines
│   ├── 14-thru-neighbor-master.html     Part V · Thru, Neighbor, Master
│   ├── 15-pickup.html                   Part V · Pickup machine
│   ├── 16-playback-amp.html             Part VI · PLAYBACK and AMP pages
│   ├── 17-lfos.html                     Part VI · LFOs and the designer
│   ├── 18-effects.html                  Part VI · FX1 and FX2 effects
│   ├── 19-recording-setup.html          Part VII · Recording setup
│   ├── 20-audio-editor.html             Part VII · Audio editor (TRIM, SLICE)
│   ├── 21-scenes-crossfader.html        Part VIII · Scenes and crossfader
│   ├── 22-midi-tracks.html              Part IX · MIDI tracks
│   ├── 23-midi-sync.html                Part IX · MIDI sync and clocking
│   ├── 24-arranger.html                 Part X · The arranger
│   ├── 25-recipes.html                  Part XI · Performance recipes
│   ├── 26-appendix-a-combos.html        Appendix A · Button combos
│   ├── 27-appendix-b-troubleshooting.html  Appendix B · Troubleshooting + early startup
│   └── 28-appendix-c-glossary.html      Appendix C · Glossary
├── illustrations/
│   ├── panel-front.svg                  Top panel, 26 callouts
│   ├── panel-rear.svg                   Rear panel, 12 callouts
│   ├── data-hierarchy.svg               Card → Set → Project → Bank → Pattern
│   ├── signal-flow.svg                  Per-track audio path schematic
│   └── pickup-states.svg                Pickup machine state diagram
├── styles/
│   ├── main.css                         Typography, colours, base elements
│   ├── print.css                        @page rules, headers/footers, TOC
│   └── components.css                   Callouts, kbd pills, screen mocks
├── fonts/webfonts/                      Self-hosted woff2 (Inter, Source Serif 4,
│                                        JetBrains Mono, VT323)
├── build/
│   ├── build.py                         Concat → render pipeline
│   └── octatrack-mk1-manual.pdf         Rendered artifact (committed; ~1 MB)
├── CONTRIBUTING.md
├── LICENSE                              CC BY-NC-SA 4.0
└── README.md
```

## Building locally

Requires Python 3.10+, WeasyPrint, and the system libraries it depends on
(Pango, Cairo, GDK-Pixbuf). On Ubuntu / Debian:

```bash
sudo apt install libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz0b
pip install weasyprint --break-system-packages
```

On macOS:

```bash
brew install pango
pip install weasyprint
```

Then from the repo root:

```bash
python3 build/build.py
```

The PDF is written to `build/octatrack-mk1-manual.pdf`.

## Design system

- **Page**: A4, 22mm/20mm margins, running headers, page numbers
- **Body**: Source Serif 4 (variable)
- **Headings & UI**: Inter (400–800)
- **Code & key labels**: JetBrains Mono
- **Screen mocks**: VT323 (pixel font)
- **Accent**: deep orange `#C84A1A`, muted compared to Elektron's brand
- **LCD pseudo-render**: `#C7E662` on dark olive `#1B1F14`

## Sources

- Elektron Octatrack User Manual, OS 1.40A (December 2020) — structural
  authority and callout numbering
- Octatrack OS 1.40C release notes (January 2024) — final firmware
- Rabid Elephant Master Reference
- Merlin's Guide ("Some Thoughts on Elektron's Octatrack")
- NoiseTheorem's cheat sheet
- Elektronauts forum threads (conditional trigs, FX1 reverb, Pickup
  machines, crossfader transitions, early startup menu)

## Licence

Personal use and non-commercial redistribution permitted, provided the
colophon and authoring credit (`jordanaftermidnight`) are preserved.

"Octatrack", "Elektron", and related marks belong to their respective
holders. This document is not endorsed by Elektron Music Machines MAV AB.
No copyrighted text from the official manual is reproduced; all
explanations are written fresh.

## Contributing

Pull requests welcome — particularly:

- Corrections to factual content
- Additional performance recipes (Part XI)
- Screen-mockup SVGs for chapter examples
- Translations (long-term goal)

When editing, run `python3 build/build.py` and visually diff the rendered
PDF before committing. The `chapters/` HTML files are concatenated in
filename order, so prefix new files with the next available number.

#!/usr/bin/env python3
"""Build the Octatrack manual: concat chapter HTML fragments into one document, render to PDF."""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).parent.parent
CHAPTERS = sorted((ROOT / "chapters").glob("*.html"))
OUT_HTML = ROOT / "build" / "manual.html"
OUT_PDF = ROOT / "build" / "octatrack-mk1-manual.pdf"

def inline_svg(html: str) -> str:
    """Replace <object data='../illustrations/X.svg' ...>...</object> with inline SVG.
    WeasyPrint can render external SVGs, but inlining sidesteps any path/MIME issues
    and gives us tighter control over sizing in the PDF."""
    import re
    pattern = re.compile(
        r'<object\s+data="\.\./illustrations/([^"]+\.svg)"[^>]*>.*?</object>',
        re.DOTALL,
    )
    def replace(match):
        svg_path = ROOT / "illustrations" / match.group(1)
        if not svg_path.exists():
            return match.group(0)
        svg = svg_path.read_text()
        # Strip the XML decl if any
        svg = re.sub(r'<\?xml[^>]*\?>', '', svg).strip()
        return f'<div class="figure-svg">{svg}</div>'
    return pattern.sub(replace, html)


def build_html() -> str:
    parts = []
    for ch in CHAPTERS:
        body = ch.read_text()
        body = inline_svg(body)
        parts.append(f"<!-- ===== {ch.name} ===== -->\n{body}")

    body = "\n\n".join(parts)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Octatrack MK1 — Reworked Manual</title>
<link rel="stylesheet" href="../styles/main.css">
<link rel="stylesheet" href="../styles/print.css">
<link rel="stylesheet" href="../styles/components.css">
<style>
  /* Inlined SVG figures — width control */
  .figure-svg svg {{ width: 100%; height: auto; display: block; }}
</style>
</head>
<body>
{body}
</body>
</html>
"""


def main():
    OUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    html = build_html()
    OUT_HTML.write_text(html)
    print(f"Wrote {OUT_HTML} ({len(html):,} bytes)")

    print(f"Rendering PDF with WeasyPrint...")
    result = subprocess.run(
        ["weasyprint", str(OUT_HTML), str(OUT_PDF), "-v"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print("STDOUT:", result.stdout[-2000:])
        print("STDERR:", result.stderr[-2000:])
        sys.exit(result.returncode)
    print(result.stderr[-1500:])
    print(f"\nPDF: {OUT_PDF}")
    print(f"Size: {OUT_PDF.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()

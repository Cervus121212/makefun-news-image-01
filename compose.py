#!/usr/bin/env python3
"""Compose the news-image-01 entry: 6 illustrated panels + PIL-rendered captions.

Canvas 1024x1024, navy header, 2 rows x 3 panels. Panel art is AI-generated
flat editorial illustration (no text in the art); every word on the image is
rendered here by PIL in DejaVu Sans Bold, so captions are crisp real text.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
PANELS_DIR = os.path.join(HERE, "panels")

NAVY = (20, 38, 74)
GOLD = (201, 162, 39)
BG = (247, 244, 238)
INK = (20, 38, 74)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# (panel file stem, caption) — captions are the verified facts of 13 Nov 2026.
PANELS = [
    ("panel-a-senate", "SENATE SUMMONS EX-NVIDIA CEO"),
    ("panel-b-warship", "DRONE HITS RUSSIAN WARSHIP"),
    ("panel-c-radar", "IRAN SAYS IT HIT US RADAR IN BAHRAIN"),
    ("panel-d-hack", "FBI: N. KOREA $400M CRYPTO HACK"),
    ("panel-e-deportations", "US DEPORTATIONS HIT RECORD 483,200"),
    ("panel-f-kane", "KANE BREAKS ENGLAND CAPS RECORD"),
]


def find_panel(stem):
    for name in sorted(os.listdir(PANELS_DIR)):
        if name.startswith("media-generation-" + stem) and name.endswith(".webp"):
            return os.path.join(PANELS_DIR, name)
    raise FileNotFoundError(stem)


def wrap_caption(draw, text, font, max_width):
    """Greedy word wrap; returns at most 2 lines (shrinks font if needed)."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    W = H = 1024
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Header bar
    draw.rectangle([0, 0, W, 100], fill=NAVY)
    draw.rectangle([0, 100, W, 104], fill=GOLD)
    title_font = ImageFont.truetype(FONT_BOLD, 50)
    date_font = ImageFont.truetype(FONT_BOLD, 26)
    draw.text((24, 50), "WORLD NEWS", font=title_font, fill=(255, 255, 255),
              anchor="lm")
    date = "FRIDAY 13 NOVEMBER 2026"
    draw.text((W - 24, 50), date, font=date_font, fill=(255, 255, 255),
              anchor="rm")

    # Grid: 3 cols x 2 rows
    margin, gutter = 16, 12
    top, bottom = 120, 1008
    col_w = (W - 2 * margin - 2 * gutter) // 3
    row_h = (bottom - top - gutter) // 2
    img_h = row_h - 104  # caption strip below each illustration

    cap_font = ImageFont.truetype(FONT_BOLD, 23)
    for i, (stem, caption) in enumerate(PANELS):
        col, row = i % 3, i // 3
        x0 = margin + col * (col_w + gutter)
        y0 = top + row * (row_h + gutter)

        art = Image.open(find_panel(stem)).convert("RGB")
        art = ImageOps.fit(art, (col_w, img_h), Image.LANCZOS)
        img.paste(art, (x0, y0))
        # thin navy frame around the illustration
        draw.rectangle([x0, y0, x0 + col_w - 1, y0 + img_h - 1],
                       outline=NAVY, width=2)

        lines = None
        font = None
        for size in range(23, 17, -1):
            f = ImageFont.truetype(FONT_BOLD, size)
            cand = wrap_caption(draw, caption, f, col_w - 16)
            if len(cand) <= 2:
                lines, font = cand, f
                break
        assert lines is not None, caption
        line_h = font.size + 7
        block_h = len(lines) * line_h
        cy = y0 + img_h + (104 - block_h) // 2
        for j, ln in enumerate(lines):
            draw.text((x0 + col_w // 2, cy + j * line_h + line_h // 2),
                      ln, font=font, fill=INK, anchor="mm")

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()

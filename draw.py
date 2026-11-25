#!/usr/bin/env python3
"""news-image-20261124 entry, v3.

Draws a newspaper front page summing up Tuesday 24 November 2026.
Every story below is a development of that Tuesday, verified against
real reporting (Reuters, AP, Daily Summary Of): the US jury verdict
against Huawei, Iran's Hormuz tanker claims, Ukraine's strikes on
Russian shipping, the Houthi drone attack on Riyadh, the Cartagena
hostage-taking, plus the day's other news in the foot strip.

Output: entry.png, 1024x1024, well under the 1 MiB cap.
Run: python3 draw.py
"""

from PIL import Image, ImageDraw, ImageFont

CANVAS = (1024, 1024)
NEWS = (248, 244, 235)      # newsprint off-white
INK = (16, 16, 16)
NAVY = (10, 30, 56)
CRIMSON = (176, 32, 32)
GOLD = (203, 164, 40)
MIDGREY = (96, 96, 96)
HAIRLINE = (178, 173, 158)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/liberation"
SERIF_BOLD = FONT_DIR + "/LiberationSerif-Bold.ttf"
SERIF_REG = FONT_DIR + "/LiberationSerif-Regular.ttf"
SANS_BOLD = FONT_DIR + "/LiberationSans-Bold.ttf"
SANS_REG = FONT_DIR + "/LiberationSans-Regular.ttf"

MARGIN = 44
CONTENT_W = CANVAS[0] - 2 * MARGIN
GUTTER = 24
HALF_W = (CONTENT_W - GUTTER) // 2


def typeface(path, size):
    return ImageFont.truetype(path, size)


def flow_text(canvas, text, face, limit):
    """Greedy word wrap; returns a list of lines fitting `limit` px."""
    out, current = [], ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if canvas.textlength(trial, font=face) <= limit or not current:
            current = trial
        else:
            out.append(current)
            current = word
    if current:
        out.append(current)
    return out


def draw_lines(canvas, x, y, lines, face, step, colour=INK):
    for line in lines:
        canvas.text((x, y), line, font=face, fill=colour)
        y += step
    return y


def draw_kicker(canvas, x, y, label):
    face = typeface(SANS_BOLD, 23)
    canvas.text((x, y), label.upper(), font=face, fill=CRIMSON)
    return y + 31


def draw_headline(canvas, x, y, text, size, limit):
    face = typeface(SERIF_BOLD, size)
    lines = flow_text(canvas, text, face, limit)
    return draw_lines(canvas, x, y, lines, face, int(size * 1.04))


def draw_body(canvas, x, y, text, size, limit):
    face = typeface(SERIF_REG, size)
    lines = flow_text(canvas, text, face, limit)
    return draw_lines(canvas, x, y, lines, face, int(size * 1.32))


def draw_rule(canvas, y, x0=MARGIN, x1=None):
    canvas.line([(x0, y), (x1 or CANVAS[0] - MARGIN, y)], fill=HAIRLINE, width=2)


def draw_vrule(canvas, x, y0, y1):
    canvas.line([(x, y0), (x, y1)], fill=HAIRLINE, width=2)


def draw_story(canvas, x, y, story, head_size=35):
    """One kicker + headline + body block. Returns the y below it."""
    y = draw_kicker(canvas, x, y, story["kicker"])
    y = draw_headline(canvas, x, y, story["headline"], head_size, HALF_W)
    y = draw_body(canvas, x, y + 4, story["body"], 22, HALF_W)
    return y


LEAD = {
    "kicker": "Technology  •  Justice",
    "headline": "HUAWEI GUILTY OF FRAUD",
    "body": (
        "A US jury finds Huawei guilty of trade-secret conspiracy "
        "and bank fraud on 10 of 12 counts after a two-month trial. "
        "Acquitted of the heavier racketeering charge, the company "
        "says it will appeal; sentencing is set for September 2027."
    ),
}

ROW_ONE = [
    {
        "kicker": "Middle East",
        "headline": "IRAN SAYS 4 TANKERS HIT BY MINES",
        "body": (
            "Iran's Revolutionary Guard claims four tankers were hit "
            "by mines in Hormuz; monitors call the claims unverified."
        ),
    },
    {
        "kicker": "Ukraine",
        "headline": "UKRAINE HITS RUSSIAN SHIP IN GULF",
        "body": (
            "Kyiv says drones hit the cargo ship Sparta II in the "
            "Gulf of Finland; Zelenskiy claims a Russian corvette "
            "sank off Libya."
        ),
    },
]

ROW_TWO = [
    {
        "kicker": "Saudi Arabia",
        "headline": "HOUTHI DRONE HITS RIYADH TOWER",
        "body": (
            "A Houthi drone hits Riyadh's Public Investment Fund "
            "tower, injuring 11, Saudi officials say — the second "
            "attack in a week."
        ),
    },
    {
        "kicker": "Colombia",
        "headline": "CARTAGENA HOSTAGE CRISIS: 25 HELD",
        "body": (
            "Gunmen hold 25 people in a Cartagena supermarket; five "
            "elderly women are freed as troops and police surround "
            "the building."
        ),
    },
]

ALSO_TODAY = [
    "Turkish air force helicopter crashes, 5 dead",
    "Shenzhou 24 launches with three astronauts",
    "Senegal wins Africa Cup of Nations after court appeal",
    "Trump awards Medal of Freedom to Rudy Giuliani",
    "Prabowo names replacements for VP Gibran",
    "Hanoi hot-pot restaurant blast kills 6",
]


def build():
    page = Image.new("RGB", CANVAS, NEWS)
    pen = ImageDraw.Draw(page)

    # ---- Masthead ---------------------------------------------------
    pen.rectangle([0, 0, CANVAS[0], 150], fill=NAVY)
    pen.text((512, 16), "THE WORLD TODAY", font=typeface(SERIF_BOLD, 76),
             fill=WHITE, anchor="ma")
    pen.text((512, 106), "T U E S D A Y   2 4   N O V E M B E R   2 0 2 6",
             font=typeface(SANS_BOLD, 25), fill=GOLD, anchor="ma")
    pen.rectangle([0, 150, CANVAS[0], 156], fill=GOLD)

    # ---- Lead story -------------------------------------------------
    y = 172
    y = draw_kicker(pen, MARGIN, y, LEAD["kicker"])
    y = draw_headline(pen, MARGIN, y, LEAD["headline"], 62, CONTENT_W)
    y = draw_body(pen, MARGIN, y + 6, LEAD["body"], 27, CONTENT_W)
    draw_rule(pen, y + 14)

    # ---- Row one: Hormuz | Ukraine ----------------------------------
    top = y + 28
    left_end = draw_story(pen, MARGIN, top, ROW_ONE[0])
    right_end = draw_story(pen, MARGIN + HALF_W + GUTTER, top, ROW_ONE[1])
    row_bottom = max(left_end, right_end)
    draw_vrule(pen, 512, top, row_bottom)
    draw_rule(pen, row_bottom + 14)

    # ---- Row two: Riyadh | Cartagena --------------------------------
    top2 = row_bottom + 28
    left_end = draw_story(pen, MARGIN, top2, ROW_TWO[0])
    right_end = draw_story(pen, MARGIN + HALF_W + GUTTER, top2, ROW_TWO[1])
    row2_bottom = max(left_end, right_end)
    draw_vrule(pen, 512, top2, row2_bottom)
    print("layout: lead ends", y, "| row1 ends", row_bottom,
          "| row2 ends", row2_bottom)
    assert row2_bottom <= 868, "row 2 overflows into the foot strip"

    # ---- Foot strip: also today -------------------------------------
    strip_top = 846
    pen.rectangle([0, strip_top, CANVAS[0], CANVAS[1]], fill=NAVY)
    pen.text((MARGIN, strip_top + 12), "ALSO TODAY",
             font=typeface(SANS_BOLD, 25), fill=GOLD)
    item_face = typeface(SANS_REG, 19)
    col_x = [MARGIN, MARGIN + HALF_W + GUTTER]
    rows_y = [strip_top + 48, strip_top + 74, strip_top + 100]
    for idx, item in enumerate(ALSO_TODAY):
        cx = col_x[idx % 2]
        cy = rows_y[idx // 2]
        pen.text((cx, cy), "\u2022  " + item, font=item_face, fill=WHITE)

    page.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    build()

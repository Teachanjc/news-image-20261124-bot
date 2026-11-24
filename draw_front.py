import os
from PIL import Image, ImageDraw, ImageFont

CANVAS_W = 1024
CANVAS_H = 1024
PAPER = (249, 243, 229)
INK = (20, 20, 20)
RED = (176, 32, 32)
NAVY = (22, 58, 112)
GREY = (96, 92, 84)
SAND = (233, 225, 207)
SKY = (168, 200, 226)
LEAF = (72, 138, 88)
GOLD = (216, 116, 22)
DARK = (52, 52, 58)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def load_font(filename, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, filename), size)


def serif_bold(size):
    return load_font("DejaVuSerif-Bold.ttf", size)


def serif(size):
    return load_font("DejaVuSerif.ttf", size)


def sans_bold(size):
    return load_font("DejaVuSans-Bold.ttf", size)


def sans(size):
    return load_font("DejaVuSans.ttf", size)


def text_wrap(text, fnt, width):
    parts = text.split()
    rows = []
    current = ""
    for part in parts:
        trial = part if current == "" else current + " " + part
        if fnt.getlength(trial) <= width:
            current = trial
        else:
            if current != "":
                rows.append(current)
            current = part
    if current != "":
        rows.append(current)
    return rows


def para(d, x, y, text, fnt, width, step, colour=INK):
    for row in text_wrap(text, fnt, width):
        d.text((x, y), row, font=fnt, fill=colour)
        y += step
    return y


def hline(d, x, y, width, colour=INK, thick=2):
    d.line([(x, y), (x + width, y)], fill=colour, width=thick)


def tag(d, x, y, label, colour=RED):
    d.text((x, y), label, font=sans_bold(17), fill=colour)
    return y + 27


def head(d, x, y, text, size, width, step, colour=INK):
    fnt = serif_bold(size)
    for row in text_wrap(text, fnt, width):
        d.text((x, y), row, font=fnt, fill=colour)
        y += step
    return y


def draw_blast(d, cx, cy, r):
    points = []
    import math
    for i in range(16):
        ang = math.pi * i / 8
        rad = r if i % 2 == 0 else r * 0.45
        points.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    d.polygon(points, fill=GOLD, outline=RED)
    d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=RED)


def draw_skyline(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    d.rectangle([x, y + h - 26, x + w, y + h], fill=SAND)
    d.rectangle([x + 12, y + 58, x + 52, y + h - 26], fill=DARK)
    d.rectangle([x + 62, y + 30, x + 104, y + h - 26], fill=(74, 74, 82))
    d.rectangle([x + 114, y + 72, x + 150, y + h - 26], fill=DARK)
    d.rectangle([x + 160, y + 44, x + 204, y + h - 26], fill=(74, 74, 82))
    for bx in (12, 62, 114, 160):
        for wy in range(y + 40, y + h - 40, 18):
            d.rectangle([x + bx + 8, wy, x + bx + 20, wy + 8], fill=(240, 220, 140))
    draw_blast(d, x + w - 52, y + 46, 30)


def draw_block(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(196, 188, 172))
    d.rectangle([x, y, x + w, y + 8], fill=(140, 132, 118))
    for col in range(4):
        wx = x + 14 + col * 52
        d.rectangle([wx, y + 18, wx + 30, y + 34], fill=(70, 76, 90))
    d.polygon([(x + 150, y + 8), (x + 182, y + 30), (x + 204, y + 8)], fill=(120, 112, 98))
    d.rectangle([x + 8, y + h - 6, x + w - 8, y + h], fill=GREY)


def draw_jet(d, x, y, w, h):
    d.polygon([(x, y + h // 2), (x + w - 60, y + 8), (x + w, y + h // 2), (x + w - 60, y + h - 8)], fill=NAVY)
    d.polygon([(x + w // 2, y + h // 2 - 6), (x + w // 2 + 40, y - 14), (x + w // 2 + 70, y + h // 2 - 6)], fill=NAVY)
    d.polygon([(x + w // 2 + 10, y + h // 2 + 6), (x + w // 2 + 50, y + h + 12), (x + w // 2 + 80, y + h // 2 + 6)], fill=NAVY)
    d.ellipse([x + w - 58, y + h // 2 - 7, x + w - 34, y + h // 2 + 7], fill=SKY)
    d.line([(x - 46, y + h // 2 - 8), (x - 8, y + h // 2 - 8)], fill=GREY, width=3)
    d.line([(x - 30, y + h // 2 + 8), (x - 4, y + h // 2 + 8)], fill=GREY, width=3)


def draw_phone(d, x, y, w, h):
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=(24, 24, 30), outline=GREY, width=2)
    d.rectangle([x + 8, y + 8, x + w - 8, y + h - 8], fill=(238, 238, 244))
    d.text((x + 16, y + 12), "GROK", font=sans_bold(18), fill=INK)
    d.polygon([(x + w - 44, y + 12), (x + w - 18, y + 12), (x + w - 31, y + 40)], fill=RED)
    d.text((x + w - 35, y + 16), "!", font=sans_bold(18), fill=(255, 255, 255))


def draw_processor(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(18, 18, 24), outline=(92, 200, 122), width=3)
    d.rectangle([x + w // 4, y + h // 4, x + 3 * w // 4, y + 3 * h // 4], fill=(28, 88, 48), outline=(92, 200, 122), width=2)
    d.text((x + w // 4 + 8, y + h // 4 + 6), "AI", font=sans_bold(18), fill=(220, 255, 230))
    for i in range(3):
        px = x + 20 + i * (w - 40) // 2
        d.line([(px, y - 10), (px, y)], fill=(92, 200, 122), width=4)


def masthead(d):
    d.text((36, 24), "THE WORLD TODAY", font=serif_bold(64), fill=INK)
    hline(d, 36, 108, 952, INK, 4)
    d.text((36, 120), "TUESDAY 24 NOVEMBER 2026", font=sans_bold(23), fill=RED)
    d.text((540, 122), "WORLD EDITION  •  FIVE STORIES", font=sans_bold(19), fill=INK)
    hline(d, 36, 154, 952, INK, 2)


def lead(d):
    y = 172
    y = tag(d, 36, y, "GAZA  •  ISRAEL-HAMAS WAR")
    y = head(d, 36, y, "Israeli strike kills Hamas security chief in Gaza City", 37, 590, 45)
    y = para(d, 36, y + 8, "Israeli airstrikes on Tuesday killed Naeem Abu Nahel, the director of Hamas' internal security apparatus, and six others, including two police officers, medics and police said.", sans(18), 590, 25)
    y = para(d, 36, y + 6, "The military said it had struck a senior Hamas militant. Earlier strikes in Khan Younis and near the Netzarim corridor killed six more people.", sans(18), 590, 25)
    draw_skyline(d, 660, 200, 328, 210)
    d.text((660, 422), "Abu Nahel killed in western Gaza City", font=sans_bold(15), fill=NAVY)
    hline(d, 36, 478, 952, INK, 2)


def middle(d):
    top = 496
    d.line([(512, 496), (512, 700)], fill=GREY, width=1)
    y = tag(d, 36, top, "UKRAINE WAR  •  ZAPORIZHZHIA")
    y = head(d, 36, y, "Russian overnight attack kills two, wounds 40", 25, 440, 32)
    y = para(d, 36, y + 6, "The strike hit an apartment building in Zaporizhzhia. Four children were among the wounded.", sans(16), 440, 22)
    draw_block(d, 120, 646, 260, 48)
    y = tag(d, 548, top, "KOREA  •  AIR DEFENCE ZONE")
    y = head(d, 548, y, "Foreign jets enter South Korea's defence zone", 25, 440, 32)
    y = para(d, 548, y + 6, "Several Russian aircraft flew inside the zone over waters between Korea and Japan, Seoul said.", sans(16), 440, 22)
    draw_jet(d, 620, 650, 220, 36)
    hline(d, 36, 700, 952, INK, 2)


def bottom(d):
    top = 718
    d.line([(512, 718), (512, 906)], fill=GREY, width=1)
    y = tag(d, 36, top, "UNITED STATES  •  ARTIFICIAL INTELLIGENCE")
    y = head(d, 36, y, "States sue Musk firms over Grok images", 25, 440, 32)
    y = para(d, 36, y + 6, "Oregon and Virginia sued Musk companies over sexualised images made with Grok.", sans(16), 440, 22)
    draw_phone(d, 210, 856, 120, 52)
    y = tag(d, 548, top, "BUSINESS  •  NVIDIA")
    y = head(d, 548, y, "Vance lobbied Nvidia board to bring back Huang", 25, 440, 32)
    y = para(d, 548, y + 6, "Trump and Vance pressed the board over the weekend to reinstate Jensen Huang.", sans(16), 440, 22)
    draw_processor(d, 700, 866, 110, 46)


def strip(d):
    d.rectangle([0, 918, 1024, 978], fill=INK)
    text = "ALSO TODAY  —  NATO vows to defend space after Russian nuclear satellite reports  •  Trump to order faster federal death sentences  •  UK sanctions five Myanmar generals after ICJ genocide ruling"
    rows = text_wrap(text, sans_bold(15), 952)
    yy = 930
    for row in rows:
        d.text((36, yy), row, font=sans_bold(15), fill=PAPER)
        yy += 21
    d.text((36, 988), "Events of Tuesday 24 November 2026, as reported that day.", font=sans(14), fill=GREY)


def build():
    img = Image.new("RGB", (CANVAS_W, CANVAS_H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1023, 1023], outline=INK, width=4)
    masthead(d)
    lead(d)
    middle(d)
    bottom(d)
    strip(d)
    return img


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    build().save(os.path.join(here, "entry.png"), optimize=True)

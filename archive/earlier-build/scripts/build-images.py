#!/usr/bin/env python3
"""Builds the decision guide and the link preview image.

Outputs, written to ../assets/:
  decision-guide.png / .svg   1600 x 900, the Part A decision guide
  og-image.png / .svg         1200 x 630, Discord embed and Open Graph size

The SVG files are the editable sources. Both formats come from the same layout,
so edit the DATA block below and run:  python3 scripts/build-images.py

Needs Pillow. If assets/dao-logo-on-dark.png exists it is placed in the header,
otherwise the Redbelly DAO wordmark is set in Be Vietnam Pro 700.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")
FONTS = os.path.join(HERE, "fonts")

# ---------- Brand tokens (Task Board brand kit, dark theme) ----------
C = dict(
    bg="#0c1317", slate="#141f26", edge="#263641", steel="#1d3140",
    text="#f1f5f8", text2="#c2ced6", muted="#8fa1ad",
    brand="#EF5350", ok="#86EFAC", warn="#FCD34D", accent="#ffb3ae",
)
FONT_FILES = {
    ("Be Vietnam Pro", 400): "BeVietnamPro_400Regular.ttf",
    ("Be Vietnam Pro", 600): "BeVietnamPro_600SemiBold.ttf",
    ("Be Vietnam Pro", 700): "BeVietnamPro_700Bold.ttf",
    ("JetBrains Mono", 500): "JetBrainsMono_500Medium.ttf",
}
SANS, MONO = "Be Vietnam Pro", "JetBrains Mono"
LAST_VERIFIED = "LAST VERIFIED 18 OCT 2026"

# ---------- DATA ----------
STATUS = {
    "NOT NEEDED": C["ok"],
    "UNCONFIRMED": C["warn"],
    "NEEDED": C["brand"],
}
GROUPS = [
    ("OUTSIDE REDBELLY MAINNET", [
        ("NOT NEEDED", "RBNT on an exchange (Gate, MEXC)",
         "Your coins sit in your exchange account, not in a Redbelly mainnet wallet."),
        ("NOT NEEDED", "Bridged or wrapped RBNT on another chain",
         "It is a separate token on that chain. Redbelly KYC covers Redbelly Network accounts only."),
    ]),
    ("ACROSS THE BRIDGE AND ON MAINNET", [
        ("UNCONFIRMED", "Bridging RBNT onto Redbelly mainnet",
         "Redbelly does not say if coins can arrive in a wallet that is not enabled. Verify first, then bridge."),
        ("NEEDED", "Bridging RBNT off Redbelly mainnet",
         "The bridge starts with a transaction from your mainnet wallet."),
        ("NEEDED", "Sending, swapping or using apps on mainnet",
         "Only enabled accounts have write access to the network."),
        ("NEEDED", "Staking on Redbelly mainnet",
         "Staking is a deposit call to a mainnet contract, so it is a mainnet transaction."),
    ]),
]


# ---------- Tiny drawing model ----------
class Scene:
    def __init__(self, w, h):
        self.w, self.h, self.ops = w, h, []

    def rect(self, x, y, w, h, fill=None, stroke=None, sw=1, r=0):
        self.ops.append(("rect", x, y, w, h, fill, stroke, sw, r))

    def circle(self, cx, cy, r, fill):
        self.ops.append(("circle", cx, cy, r, fill))

    def text(self, x, y, s, family, weight, size, fill, ls=0.0, anchor="start"):
        self.ops.append(("text", x, y, s, family, weight, size, fill, ls, anchor))

    def image(self, x, y, h, path, href):
        self.ops.append(("image", x, y, h, path, href))


_font_cache = {}


def font(family, weight, size):
    key = (family, weight, size)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(os.path.join(FONTS, FONT_FILES[(family, weight)]), size)
    return _font_cache[key]


def width(s, family, weight, size, ls=0.0):
    return font(family, weight, size * 4).getlength(s) / 4 + ls * len(s)


def wrap(s, family, weight, size, max_w):
    lines, cur = [], ""
    for word in s.split(" "):
        trial = (cur + " " + word).strip()
        if width(trial, family, weight, size) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def header(sc, x, y, right_x):
    logo = os.path.join(ASSETS, "dao-logo-on-dark.png")
    if os.path.exists(logo):
        sc.image(x, y - 34, 44, logo, "dao-logo-on-dark.png")
    else:
        sc.text(x, y, "Redbelly", SANS, 700, 28, C["text"])
        off = width("Redbelly ", SANS, 700, 28)
        sc.text(x + off, y, "DAO", SANS, 700, 28, C["accent"])
    sc.text(right_x, y, LAST_VERIFIED, MONO, 500, 16, C["muted"], ls=0.8, anchor="end")


def status(sc, x, cy, label, size=17):
    sc.circle(x + 7, cy, 7, STATUS[label])
    sc.text(x + 26, cy + size * 0.36, label, MONO, 500, size, C["text"], ls=0.9)


# ---------- Scenes ----------
def decision_guide():
    W, H = 1600, 900
    sc = Scene(W, H)
    sc.rect(0, 0, W, H, fill=C["bg"])
    L, R = 80, 1520
    header(sc, L, 78, R)
    sc.text(L, 150, "Do I need KYC on Redbelly?", SANS, 700, 48, C["text"], ls=-0.9)
    sc.text(L, 192, "KYC is for sending transactions on Redbelly mainnet. Find your situation below.", SANS, 400, 23, C["text2"])

    y = 238
    for gi, (gname, rows) in enumerate(GROUPS):
        sc.text(L, y + 12, gname, SANS, 700, 14, C["muted"], ls=1.6)
        y += 26
        for st, who, why in rows:
            h = 70
            sc.rect(L, y, R - L, h, fill=C["slate"], stroke=C["edge"], sw=1, r=8)
            status(sc, L + 26, y + h / 2, st)
            lines = wrap(who, SANS, 600, 22, 490)
            ly = y + h / 2 - (len(lines) - 1) * 13 + 8
            for i, ln in enumerate(lines):
                sc.text(L + 330, ly + i * 26, ln, SANS, 600, 22, C["text"])
            lines = wrap(why, SANS, 400, 18, 540)
            ly = y + h / 2 - (len(lines) - 1) * 11.5 + 6
            for i, ln in enumerate(lines):
                sc.text(L + 870, ly + i * 23, ln, SANS, 400, 18, C["text2"])
            y += h + 10
        y += 16

    sc.text(L, 822, "KYC means the access credential that lets a wallet send transactions on Redbelly Network. Exchanges set their own rules.", SANS, 400, 18, C["muted"])
    sc.text(L, 852, "Last verified 18 Oct 2026. Sources are listed in the full guide.", SANS, 400, 18, C["muted"])
    return sc


def og_image():
    W, H = 1200, 630
    sc = Scene(W, H)
    sc.rect(0, 0, W, H, fill=C["bg"])
    sc.rect(0, 0, W, 392, fill=C["steel"])
    L, R = 60, 1140
    header(sc, L, 82, R)
    for i, ln in enumerate(["KYC and Wallet Activation", "Explainer"]):
        sc.text(L, 178 + i * 64, ln, SANS, 700, 56, C["text"], ls=-1.1)
    sc.text(L, 300, "Do you need KYC on Redbelly? One rule, five answers,", SANS, 400, 26, C["text2"])
    sc.text(L, 336, "and the steps to activate your wallet.", SANS, 400, 26, C["text2"])
    cards = [("On an exchange", "NOT NEEDED"), ("On another chain", "NOT NEEDED"), ("On Redbelly mainnet", "NEEDED")]
    cw, gap = 340, 30
    for i, (t, st) in enumerate(cards):
        x = L + i * (cw + gap)
        sc.rect(x, 430, cw, 118, fill=C["slate"], stroke=(C["brand"] if st == "NEEDED" else C["edge"]), sw=(2 if st == "NEEDED" else 1), r=8)
        sc.text(x + 24, 478, t, SANS, 600, 24, C["text"])
        status(sc, x + 24, 518, st, size=16)
    sc.text(L, 590, LAST_VERIFIED, MONO, 500, 15, C["muted"], ls=0.8)
    return sc


# ---------- Renderers ----------
def render_png(sc, path, scale=2):
    img = Image.new("RGB", (sc.w * scale, sc.h * scale), C["bg"])
    d = ImageDraw.Draw(img)
    for op in sc.ops:
        k = op[0]
        if k == "rect":
            _, x, y, w, h, fill, stroke, sw, r = op
            box = [x * scale, y * scale, (x + w) * scale - 1, (y + h) * scale - 1]
            if r:
                d.rounded_rectangle(box, radius=r * scale, fill=fill, outline=stroke, width=int(sw * scale) if stroke else 0)
            else:
                d.rectangle(box, fill=fill, outline=stroke, width=int(sw * scale) if stroke else 0)
        elif k == "circle":
            _, cx, cy, r, fill = op
            d.ellipse([(cx - r) * scale, (cy - r) * scale, (cx + r) * scale, (cy + r) * scale], fill=fill)
        elif k == "text":
            _, x, y, s, fam, wt, size, fill, ls, anchor = op
            f = font(fam, wt, int(round(size * scale)))
            total = width(s, fam, wt, size, ls) * scale
            px = x * scale - (total if anchor == "end" else 0)
            if ls:
                for ch in s:
                    d.text((px, y * scale), ch, font=f, fill=fill, anchor="ls")
                    px += f.getlength(ch) + ls * scale
            else:
                d.text((px, y * scale), s, font=f, fill=fill, anchor="ls")
        elif k == "image":
            _, x, y, h, path_, _href = op
            logo = Image.open(path_).convert("RGBA")
            nh = int(h * scale)
            nw = int(logo.width * nh / logo.height)
            logo = logo.resize((nw, nh), Image.LANCZOS)
            img.paste(logo, (int(x * scale), int(y * scale)), logo)
    img = img.resize((sc.w, sc.h), Image.LANCZOS)
    img.save(path, "PNG", optimize=True)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_svg(sc, path, title, desc):
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{sc.w}" height="{sc.h}" viewBox="0 0 {sc.w} {sc.h}" role="img" aria-labelledby="t d">',
        f'<title id="t">{esc(title)}</title><desc id="d">{esc(desc)}</desc>',
    ]
    for op in sc.ops:
        k = op[0]
        if k == "rect":
            _, x, y, w, h, fill, stroke, sw, r = op
            attrs = f'x="{x}" y="{y}" width="{w}" height="{h}"' + (f' rx="{r}"' if r else "")
            attrs += f' fill="{fill}"' if fill else ' fill="none"'
            if stroke:
                attrs += f' stroke="{stroke}" stroke-width="{sw}"'
            out.append(f"<rect {attrs}/>")
        elif k == "circle":
            _, cx, cy, r, fill = op
            out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>')
        elif k == "text":
            _, x, y, s, fam, wt, size, fill, ls, anchor = op
            extra = (f' letter-spacing="{ls}"' if ls else "") + (' text-anchor="end"' if anchor == "end" else "")
            out.append(f'<text x="{x:g}" y="{y:g}" font-family="\'{fam}\', sans-serif" font-weight="{wt}" font-size="{size}" fill="{fill}"{extra}>{esc(s)}</text>')
        elif k == "image":
            _, x, y, h, _p, href = op
            out.append(f'<image x="{x}" y="{y}" height="{h}" href="{href}"/>')
    out.append("</svg>")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    dg = decision_guide()
    render_png(dg, os.path.join(ASSETS, "decision-guide.png"))
    render_svg(dg, os.path.join(ASSETS, "decision-guide.svg"),
               "Do I need KYC on Redbelly?",
               "RBNT on an exchange and bridged or wrapped RBNT on another chain: not needed. Bridging onto mainnet: unconfirmed, verify first. Bridging off mainnet, using mainnet and staking: needed. Last verified 18 October 2026.")
    og = og_image()
    render_png(og, os.path.join(ASSETS, "og-image.png"))
    render_svg(og, os.path.join(ASSETS, "og-image.svg"),
               "KYC and Wallet Activation Explainer",
               "Link preview image for the KYC and Wallet Activation Explainer.")
    print("built decision-guide and og-image")

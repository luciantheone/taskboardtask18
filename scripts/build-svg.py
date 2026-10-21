"""Build assets/decision-guide.svg, the editable vector version of the decision guide.

The logo is the unmodified brand kit PNG, embedded as an image. Fonts are embedded,
so the SVG looks the same on any machine. Run from the repo root:
    python3 scripts/build-svg.py
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent


def b64(path):
    return base64.b64encode((ROOT / path).read_bytes()).decode()


FONTS = [
    ("Be Vietnam Pro", 400, "fonts/be-vietnam-pro-latin-400-normal.woff2"),
    ("Be Vietnam Pro", 600, "fonts/be-vietnam-pro-latin-600-normal.woff2"),
    ("Be Vietnam Pro", 700, "fonts/be-vietnam-pro-latin-700-normal.woff2"),
    ("JetBrains Mono", 500, "fonts/jetbrains-mono-latin-500-normal.woff2"),
]
font_css = "\n".join(
    f'@font-face{{font-family:"{n}";font-weight:{w};src:url(data:font/woff2;base64,{b64(p)}) format("woff2")}}'
    for n, w, p in FONTS
)

COL = {"y": ("#ffb3ae", "#EF5350"), "n": ("#86EFAC", "#86EFAC"), "u": ("#FCD34D", "#FCD34D")}
ROWS = [
    ("Hold RBNT on an exchange", "n", "NOT NEEDED", "Nothing is signed on Redbelly Network."),
    ("Hold wrapped RBNT on another chain", "n", "NOT NEEDED", "The token lives on another chain."),
    ("Bridge into Redbelly mainnet", "u", "UNCONFIRMED", "No official page says. Enable your wallet first."),
    ("Bridge out of Redbelly mainnet", "y", "NEEDED", "You sign on Redbelly Network."),
    ("Send, swap or use apps on mainnet", "y", "NEEDED", "Write access needs an enabled account."),
    ("Stake RBNT", "y", "NEEDED", "Staking is a mainnet transaction."),
]

rows = []
for i, (what, k, label, why) in enumerate(ROWS):
    top = 198 + 78 * i
    mid = top + 39
    text_col, dot_col = COL[k]
    rows.append(f'<line x1="80" x2="1520" y1="{top}" y2="{top}" stroke="#34444f"/>')
    rows.append(f'<text x="80" y="{mid + 9}" class="w">{what}</text>')
    rows.append(f'<circle cx="647" cy="{mid}" r="7" fill="{dot_col}"/>')
    rows.append(f'<text x="666" y="{mid + 7}" class="st" fill="{text_col}">{label}</text>')
    rows.append(f'<text x="870" y="{mid + 7}" class="r">{why}</text>')
rows.append('<line x1="80" x2="1520" y1="666" y2="666" stroke="#34444f"/>')

logo = b64("assets/logo/dao-logo-on-dark-web.png")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-labelledby="t d">
<title id="t">Do I need KYC on Redbelly?</title>
<desc id="d">KYC is needed for anything you sign on Redbelly mainnet. Needed: bridge out, send or swap, stake. Not needed: RBNT on an exchange, wrapped RBNT on another chain. Unconfirmed: bridge into mainnet.</desc>
<style>
{font_css}
text{{font-family:"Be Vietnam Pro",system-ui,sans-serif;fill:#f1f5f8}}
.cap{{font-size:14px;font-weight:700;letter-spacing:1.4px;fill:#ffb3ae}}
.h{{font-size:46px;font-weight:700;letter-spacing:-0.92px}}
.rule{{font-size:22px;fill:#c6d2da}}
.w{{font-size:25px;font-weight:600}}
.st{{font-family:"JetBrains Mono",monospace;font-weight:500;font-size:19px;letter-spacing:0.95px}}
.r{{font-size:20px;fill:#c6d2da}}
.box{{font-size:18px;fill:#c6d2da}}
.box b{{font-weight:600}}
.foot{{font-size:16px;fill:#8fa1ad}}
.mono{{font-family:"JetBrains Mono",monospace;font-weight:500}}
</style>
<rect width="1600" height="900" fill="#0c1317"/>
<image x="1374" y="36" width="146" height="104" href="data:image/png;base64,{logo}" xlink:href="data:image/png;base64,{logo}"/>
<text x="80" y="77" class="cap">DO I NEED KYC?</text>
<text x="80" y="122" class="h">KYC is needed for anything you sign on Redbelly mainnet</text>
<text x="80" y="168" class="rule">Chain ID <tspan class="mono">151</tspan>. Anywhere else, <tspan fill="#ffb3ae" style="font-weight:600">no Redbelly KYC</tspan>.</text>
{chr(10).join(rows)}
<rect x="80.5" y="688.5" width="707" height="94" rx="8" fill="#141f26" stroke="#223039"/>
<text x="101" y="716" class="box"><tspan style="font-weight:600;fill:#f1f5f8">Native vs wrapped.</tspan> Signing on Redbelly (chain ID 151) needs KYC. Wrapped</text>
<text x="101" y="741" class="box">RBNT on another chain does not.</text>
<rect x="812.5" y="688.5" width="707" height="119" rx="8" fill="#141f26" stroke="#223039"/>
<text x="833" y="716" class="box"><tspan style="font-weight:600;fill:#f1f5f8">DAO vs network.</tspan> The DAO is open to general members from any</text>
<text x="833" y="741" class="box">region. High Council and leadership limits remain. The</text>
<text x="833" y="766" class="box">network does not offer services in 18 jurisdictions</text>
<text x="833" y="791" class="box">(terms, clause 15.1).</text>
<text x="80" y="868" class="foot">Sources are listed in the full guide.</text>
<text x="1520" y="868" text-anchor="end" class="foot mono">Last verified 21 Oct 2026</text>
</svg>
'''
(ROOT / "assets" / "decision-guide.svg").write_text(svg, encoding="utf8")
print("wrote assets/decision-guide.svg", len(svg) // 1024, "KB")

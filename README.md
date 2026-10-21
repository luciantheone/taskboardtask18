# KYC and Wallet Activation Explainer

A static guide for the Redbelly DAO Task Board (TASK-18). It answers whether you need KYC on Redbelly, how to get verified and activate a wallet, and what to do when it gets stuck.

## Contents

| Path | What it is |
| --- | --- |
| `index.html` | The guide: Parts A to D, the short version and the source list |
| `KYC-and-Wallet-Activation-Explainer.pdf` | The guide as a PDF |
| `assets/decision-guide.png` | Part A as a standalone image, 1600 x 900 |
| `assets/decision-guide.svg` | The decision guide as a vector image, with the logo and fonts embedded |
| `assets/og-image.png` | Link preview image, 1200 x 630 |
| `assets/logo/` | The two brand kit logos, unmodified (`dao-logo-on-dark.png`, `dao-logo-on-light.png`), plus small `-web.png` copies that only change the size |
| `evidence.html` | The /evidence page. Where the portal wording, the DAO vote and the Averer form fields were read, with file names and checksums |
| `short-version.md` | Text and image for pinning in Discord or Telegram |
| `SOURCES.md` | Source list and a claim by claim map |
| `scripts/render.py` | Rebuilds the two PNG images and the PDF |
| `scripts/build-svg.py` | Rebuilds `assets/decision-guide.svg` |
| `deploy/` | nginx example and a deploy script |

## Run it

No build step. Serve the folder with any static server.

```
python3 -m http.server 8080
```

## Deploy to a VPS

```
sudo ./deploy/deploy.sh /var/www/kyc
sudo cp deploy/nginx.conf.example /etc/nginx/sites-available/kyc
# edit server_name and root, then
sudo ln -s /etc/nginx/sites-available/kyc /etc/nginx/sites-enabled/kyc
sudo nginx -t && sudo systemctl reload nginx
```

## Rebuild the images and PDF

```
pip install playwright
python3 scripts/render.py
```

The image sources are `assets/src/guide.html` and `assets/src/og.html`.

## Link preview

Discord and X need absolute URLs for preview images. The `og:image` and `canonical` values in `index.html` use https://wallet-activation.vercel.app/. Change them if the page moves.

## Brand

Colours, type, spacing and voice follow the Task Board brand kit: https://taskboard.redbellydao.network/brand

The brand kit offers the logo as PNG only, in two variants, so the SVG embeds the PNG. Light ink goes on dark backgrounds and dark ink on light ones. Scale by height, 28px minimum, no plate, no recolour.

Fonts are Be Vietnam Pro and JetBrains Mono, both under the SIL Open Font License. The licence texts are in `fonts/`.

## Keeping it current

The guide carries a last verified date. The wallet limit, the restricted jurisdictions and the portal wording can change. Recheck the pages in `SOURCES.md`, update the date in `index.html`, `assets/src/guide.html` and `assets/src/og.html`, then run `scripts/render.py`.

## Clean URLs

`vercel.json` turns on clean URLs, so `evidence.html` is served at `/evidence`.

# KYC and Wallet Activation Explainer

A static guide for the Redbelly DAO Task Board (TASK-18). It answers whether you need KYC on Redbelly, how to get verified and activate a wallet, and what to do when it gets stuck.

## Contents

| Path | What it is |
| --- | --- |
| `index.html` | The guide, Parts A to D, the short version and the source list |
| `assets/decision-guide.png` | Part A as a standalone image, 1600 x 900 |
| `assets/decision-guide.svg` | Editable source of the decision guide |
| `assets/og-image.png` | Link preview image, 1200 x 630 |
| `short-version.md` | The text and image for pinning in Discord or Telegram |
| `SOURCES.md` | Source list and a claim by claim map |
| `scripts/build-images.py` | Rebuilds the images from one layout (needs Pillow) |
| `scripts/set-site-url.cjs` | Adds absolute link preview tags once the domain is known |
| `deploy/nginx.conf.example` | Sample server block for a static host |

## Run it

No build step. Serve the folder with any static server.

```
python3 -m http.server 8080
```

## Rebuild the images

```
pip install pillow
python3 scripts/build-images.py
```

If `assets/dao-logo-on-dark.png` and `assets/dao-logo-on-light.png` are present, the page header and images use them. Both files are downloadable from the Task Board brand kit. Without them the page uses the brand's wordmark fallback.

## Set the link preview URL

Discord and X need absolute URLs for preview images.

```
node scripts/set-site-url.cjs https://your.domain
```

## Brand

Colours, type, spacing and voice follow the Task Board brand kit: https://taskboard.redbellydao.network/brand

Fonts are Be Vietnam Pro and JetBrains Mono, both under the SIL Open Font License. The licence texts are in `assets/fonts/`.

## Keeping it current

The guide carries a last verified date. The wallet limit, the restricted jurisdictions and the portal wording can change. Recheck the pages listed in `SOURCES.md`, update the date in `index.html` and in `scripts/build-images.py`, then rebuild the images.

"""Render the decision guide PNG, the link preview PNG and the PDF.

Needs: pip install playwright, and a Chromium for Playwright.
Run from the repo root: python3 scripts/render.py
"""
import asyncio
import pathlib

from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        for src, out, w, h in [
            ("assets/src/guide.html", "assets/decision-guide.png", 1600, 900),
            ("assets/src/og.html", "assets/og-image.png", 1200, 630),
        ]:
            page = await browser.new_page(viewport={"width": w, "height": h})
            await page.goto((ROOT / src).as_uri())
            await page.evaluate("document.fonts.ready")
            await page.wait_for_timeout(400)
            await page.screenshot(path=str(ROOT / out))
            await page.close()

        page = await browser.new_page(viewport={"width": 1000, "height": 900})
        await page.goto((ROOT / "index.html").as_uri())
        await page.evaluate("document.fonts.ready")
        # SITE_LINKS: point file:// links at the live site so the PDF has no local paths
        await page.evaluate("""() => {
          const base = location.href.substring(0, location.href.lastIndexOf("/") + 1);
          document.querySelectorAll("a[href]").forEach(a => {
            const h = a.getAttribute("href");
            if (h.startsWith("#")) return;
            if (a.href.startsWith(base)) a.href = "https://wallet-activation.vercel.app/" + a.href.slice(base.length);
          });
        }""")
        await page.wait_for_timeout(400)
        await page.pdf(
            path=str(ROOT / "KYC-and-Wallet-Activation-Explainer.pdf"),
            format="A4",
            print_background=True,
            margin={"top": "16mm", "bottom": "16mm", "left": "14mm", "right": "14mm"},
        )
        await browser.close()


asyncio.run(main())

#!/usr/bin/env node
// Usage: node scripts/set-site-url.cjs https://your.domain
// Rewrites the marked meta block in index.html with absolute preview URLs.
const fs = require("fs");
const path = require("path");

const url = (process.argv[2] || "").replace(/\/+$/, "");
if (!/^https?:\/\/[^\s/]+/.test(url)) {
  console.error("Usage: node scripts/set-site-url.cjs https://your.domain");
  process.exit(1);
}

const file = path.join(__dirname, "..", "index.html");
const html = fs.readFileSync(file, "utf8");

const block = [
  "<!-- og:start -->",
  '<meta property="og:type" content="website">',
  '<meta property="og:title" content="KYC and Wallet Activation Explainer">',
  '<meta property="og:description" content="Do you need KYC on Redbelly? One rule, five answers, a step by step wallet activation, and fixes for when it gets stuck.">',
  `<meta property="og:url" content="${url}/">`,
  `<meta property="og:image" content="${url}/assets/og-image.png">`,
  '<meta property="og:image:width" content="1200">',
  '<meta property="og:image:height" content="630">',
  '<meta name="twitter:card" content="summary_large_image">',
  `<meta name="twitter:image" content="${url}/assets/og-image.png">`,
  `<link rel="canonical" href="${url}/">`,
  "<!-- og:end -->",
].join("\n");

if (!/<!-- og:start -->[\s\S]*?<!-- og:end -->/.test(html)) {
  console.error("Marker block not found in index.html");
  process.exit(1);
}
fs.writeFileSync(file, html.replace(/<!-- og:start -->[\s\S]*?<!-- og:end -->/, block));
console.log("Preview tags set for " + url);

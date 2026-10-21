#!/usr/bin/env bash
# Publish the static guide to an nginx host.
# Usage: sudo ./deploy/deploy.sh /var/www/kyc
set -euo pipefail

TARGET="${1:-/var/www/kyc}"
HERE="$(cd "$(dirname "$0")/.." && pwd)"

mkdir -p "$TARGET"
rsync -a --delete \
  --exclude '.git' --exclude 'archive' --exclude 'deploy' --exclude 'scripts' \
  --exclude 'assets/src' --exclude 'node_modules' \
  "$HERE"/ "$TARGET"/

echo "Copied to $TARGET"
echo "Next: copy deploy/nginx.conf.example to /etc/nginx/sites-available/kyc,"
echo "set server_name and root, enable it, then: nginx -t && systemctl reload nginx"

# aws-ug-ensenada.github.io

Link page for the AWS User Group Ensenada ("Conecta con nosotros"), served by GitHub Pages at https://aws-ug-ensenada.github.io/.

It replaces the dynamic QR page on QR Code Generator Pro (`qrco.de/berbf6`). The QR printed on swag encodes this page's URL directly (a static QR), so it never expires and needs no subscription; to change where it leads, edit `index.html`.

## Files

- `index.html`: the page (Spanish, no trackers, no external scripts).
- `logo.png`: the group logo (hexagon, whale tail over waves), full size with a transparent background; `logo-512.png` for the page and link previews; `icon-192.png` for the browser tab and phone home screen.
- `qr/`: static QR codes for the page, made with `uv run --with segno python qr/make_qr.py`.
  - `link-page-compact.svg` / `.png`: encodes `HTTPS://AWS-UG-ENSENADA.GITHUB.IO` in uppercase (valid, and a smaller 29×29 grid that is easier to 3D-print). **Use this one for keychains.**
  - `link-page.svg` / `.png`: the same URL in lowercase (33×33), for print or screens.
  - Both use the highest error correction (H), so they still scan with small print defects.

## Publish

1. Create the public repo `aws-ug-ensenada/aws-ug-ensenada.github.io` (the name gives the root URL).
2. Push this folder to `main`; in Settings → Pages, source "Deploy from a branch", `main`, `/ (root)`.
3. Scan `qr/link-page-compact.png` with a phone and check every link.
4. Send the SVG to G&V Design and Modeling 3D for the next keychain batch.
5. Keep `qrco.de/berbf6` active while the old keychains are in use; point it at this page if QR Code Generator allows it.

## Later

- Own domain (for example `links.<domain>`): add a `CNAME` file and DNS record; the QR must then be regenerated for the new URL, so decide the final URL before a big print run.
- Scan counts, if wanted: a privacy-friendly counter (GoatCounter) or, on AWS, CloudFront access logs.

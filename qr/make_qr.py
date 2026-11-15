"""Static QR codes for the link page. Run: uv run --with segno python qr/make_qr.py

A static QR only encodes the URL, so it never expires. Uppercase is valid for the
scheme and host, and lets the QR use alphanumeric mode: fewer modules, easier to 3D-print.
"""
import segno

URL = "https://aws-ug-ensenada.github.io"
for name, data in {"link-page": URL, "link-page-compact": URL.upper()}.items():
    qr = segno.make(data, error="q", micro=False)
    qr.save(f"qr/{name}.svg", scale=10, border=4, dark="#161E2D")
    qr.save(f"qr/{name}.png", scale=20, border=4, dark="#161E2D")
    print(f"{name}: {data} -> version {qr.version}, {qr.symbol_size(border=0)[0]}x{qr.symbol_size(border=0)[1]} modules, error {qr.error}")

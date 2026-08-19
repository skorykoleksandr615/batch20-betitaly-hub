import os
from pathlib import Path

SRC = Path(r"C:\Users\Дмитрий\.cursor\projects\c-AndroidStudioProjects-batch20-hubs\assets")
DST = Path(r"C:\AndroidStudioProjects\batch20-hubs\betitaly")

MAP = {
    "bi-logo.png": "assets/brand/logo.png",
    "bi-hero.jpg": "assets/hero.jpg",
    "bi-og.jpg": "assets/og.jpg",
    "bi-slot-dog-house.jpg": "assets/slots/the-dog-house.jpg",
    "bi-slot-wolf-gold.jpg": "assets/slots/wolf-gold.jpg",
    "bi-slot-canyon-gold.jpg": "assets/slots/wild-west-gold.jpg",
    "bi-slot-great-rhino.jpg": "assets/slots/great-rhino.jpg",
    "bi-slot-buffalo-king.jpg": "assets/slots/buffalo-king.jpg",
    "bi-slot-cleopatra.jpg": "assets/slots/cleopatra.jpg",
    "bi-slot-fruit-party.jpg": "assets/slots/fruit-party.jpg",
    "bi-slot-bbb.jpg": "assets/slots/big-bass-bonanza.jpg",
    "bi-slot-wisdom-athena.jpg": "assets/slots/wisdom-of-athena.jpg",
    "bi-slot-starlight.jpg": "assets/slots/starlight-princess.jpg",
    "bi-crash-jetx.jpg": "assets/crash/jetx.jpg",
    "bi-crash-aviator.jpg": "assets/crash/aviator.jpg",
    "bi-crash-plinko.jpg": "assets/crash/plinko.jpg",
    "bi-crash-spaceman.jpg": "assets/crash/spaceman.jpg",
    "bi-crash-lucky-jet.jpg": "assets/crash/lucky-jet.jpg",
    "bi-crash-mines.jpg": "assets/crash/mines.jpg",
    "bi-live-lightning.jpg": "assets/live/lightning-roulette.jpg",
    "bi-live-crazy-time.jpg": "assets/live/crazy-time.jpg",
    "bi-live-blackjack.jpg": "assets/live/blackjack.jpg",
    "bi-live-mega-wheel.jpg": "assets/live/mega-wheel.jpg",
    "bi-live-baccarat.jpg": "assets/live/baccarat.jpg",
    "bi-live-dream-catcher.jpg": "assets/live/dream-catcher.jpg",
    "bi-page-login.jpg": "assets/pages/bi-login.jpg",
    "bi-page-join.jpg": "assets/pages/bi-join.jpg",
    "bi-page-bonus.jpg": "assets/pages/bi-bonus.jpg",
    "bi-page-slots.jpg": "assets/pages/bi-slots.jpg",
    "bi-page-odds.jpg": "assets/pages/bi-odds.jpg",
    "bi-page-crash.jpg": "assets/pages/bi-crash.jpg",
    "bi-page-live.jpg": "assets/pages/bi-live.jpg",
    "bi-page-app.jpg": "assets/pages/bi-app.jpg",
    "bi-page-pay.jpg": "assets/pages/bi-pay.jpg",
    "bi-page-help.jpg": "assets/pages/bi-help.jpg",
    "bi-promo-bonus.jpg": "assets/promo/promo-bonus.jpg",
    "bi-promo-slots.jpg": "assets/promo/promo-slots.jpg",
    "bi-promo-crash.jpg": "assets/promo/promo-crash.jpg",
    "bi-promo-live.jpg": "assets/promo/promo-live.jpg",
    "bi-promo-odds.jpg": "assets/promo/promo-odds.jpg",
    "bi-promo-pay.jpg": "assets/promo/promo-pay.jpg",
    "bi-promo-login.jpg": "assets/promo/promo-login.jpg",
    "bi-promo-join.jpg": "assets/promo/promo-join.jpg",
    "bi-promo-app.jpg": "assets/promo/promo-app.jpg",
    "bi-promo-help.jpg": "assets/promo/promo-help.jpg",
}

def main():
    from PIL import Image
    missing = []
    for src_name, rel in MAP.items():
        src = SRC / src_name
        dst = DST / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not src.exists():
            missing.append(src_name)
            continue
        im = Image.open(src)
        if src.suffix.lower() == ".png":
            im = im.convert("RGBA")
            im.thumbnail((512, 512), Image.Resampling.LANCZOS)
            im.save(dst, "PNG", optimize=True)
        else:
            im = im.convert("RGB")
            w, h = im.size
            max_w = 1600 if "promo" in rel or rel.endswith("og.jpg") else 1200
            if w > max_w:
                nh = int(h * max_w / w)
                im = im.resize((max_w, nh), Image.Resampling.LANCZOS)
            im.save(dst, "JPEG", quality=82, optimize=True, progressive=True)
        print(f"{rel}\t{dst.stat().st_size}")
    logo = DST / "assets/brand/logo.png"
    if logo.exists():
        raw = Image.open(logo).convert("RGBA")
        sizes = {
            "favicon-32x32.png": 32,
            "favicon-48x48.png": 48,
            "favicon-96x96.png": 96,
            "favicon-192x192.png": 192,
            "apple-touch-icon.png": 180,
        }
        for name, size in sizes.items():
            canvas = Image.new("RGBA", (size, size), (7, 20, 40, 255))
            icon = raw.copy()
            icon.thumbnail((size, size), Image.Resampling.LANCZOS)
            x = (size - icon.width) // 2
            y = (size - icon.height) // 2
            canvas.paste(icon, (x, y), icon)
            canvas.save(DST / name, "PNG", optimize=True)
            print(f"{name}\t{(DST / name).stat().st_size}")
        ico = Image.open(DST / "favicon-32x32.png").convert("RGBA")
        ico.save(DST / "favicon.ico", sizes=[(32, 32)])
        print(f"favicon.ico\t{(DST / 'favicon.ico').stat().st_size}")
    if missing:
        raise SystemExit("MISSING: " + ", ".join(missing))
    print("OK")

if __name__ == "__main__":
    main()

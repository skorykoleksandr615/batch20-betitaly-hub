from pathlib import Path
root = Path(r"C:\AndroidStudioProjects\batch20-hubs\betitaly")
exts = {".jpg", ".jpeg", ".png", ".ico", ".webp"}
rows = []
for p in sorted(root.rglob("*")):
    if p.is_file() and p.suffix.lower() in exts and "_gen" not in p.name:
        rows.append((p.stat().st_size, p.relative_to(root).as_posix()))
zero = [r for r in rows if r[0] == 0]
print("IMAGE_COUNT", len(rows))
print("ZERO", len(zero))
for sz, name in rows:
    print("%8d  %s" % (sz, name))

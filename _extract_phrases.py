import re, html
from pathlib import Path
ROOT = Path(r"C:\AndroidStudioProjects\batch20-hubs\betitaly")
skip_re = re.compile(r"<(script|style|noscript)[\s\S]*?</\1>", re.I)
tag_re = re.compile(r"<[^>]+>")
texts = []
for p in sorted(ROOT.glob("*.html")):
    raw = p.read_text(encoding="utf-8")
    raw = skip_re.sub(" ", raw)
    raw = re.sub(r"<[^>]+>", "\n", raw)
    raw = html.unescape(raw)
    for line in raw.splitlines():
        t = re.sub(r"\s+", " ", line).strip()
        if len(t) < 3:
            continue
        if re.fullmatch(r"[\d\s.,:%+\-–—|/]+", t):
            continue
        t = t.replace("BetItaly", "{Brand}").replace("betitaly.online", "{Domain}")
        texts.append(t)
uniq = []
seen = set()
for t in texts:
    if t not in seen:
        seen.add(t)
        uniq.append(t)
(ROOT / "_phrases.txt").write_text("\n".join(uniq), encoding="utf-8")
print(len(uniq))

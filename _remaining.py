import re
from pathlib import Path
ROOT = Path(r"C:\AndroidStudioProjects\batch20-hubs\betitaly")
keys = set()
for name in ("i18n-dict.js", "i18n-more.js", "i18n-more2.js", "i18n-more3.js", "i18n-seed.js", "i18n-more4.js", "i18n-more5.js", "i18n-more6.js", "i18n-more7.js"):
    p = ROOT / "js" / name
    if p.exists():
        raw = p.read_text(encoding="utf-8")
        found = re.findall(r'"((?:\\.|[^"\\])+)"\s*:\s*[ts]\(', raw)
        keys |= set(k.replace('\\"', '"').replace("\\\\", "\\") for k in found)
phrases = (ROOT / "_phrases.txt").read_text(encoding="utf-8").splitlines()
skip = []
need = []
for p in phrases:
    if " | " in p:
        continue
    if p in ("Bet", "Italy", "English", "{Brand}"):
        continue
    if p in keys:
        continue
    need.append(p)
(ROOT / "_missing.txt").write_text("\n".join(need), encoding="utf-8")
print(len(need))

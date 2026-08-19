from pathlib import Path
root = Path(r"C:\AndroidStudioProjects\batch20-hubs\betitaly")
old = '<script src="/js/i18n-more3.js?v=bi1"></script>\n<script src="/js/i18n.js?v=bi1"></script>'
new = (
    '<script src="/js/i18n-more3.js?v=bi1"></script>\n'
    '<script src="/js/i18n-more4.js?v=bi1"></script>\n'
    '<script src="/js/i18n-more5.js?v=bi1"></script>\n'
    '<script src="/js/i18n-more6.js?v=bi1"></script>\n'
    '<script src="/js/i18n.js?v=bi1"></script>'
)
for p in root.glob("*.html"):
    t = p.read_text(encoding="utf-8")
    t = t.replace("not a mood", "not a whim")
    if old in t:
        t = t.replace(old, new)
        print("wired", p.name)
    else:
        print("no script block", p.name)
    p.write_text(t, encoding="utf-8")
bp = root / "_build_pages.py"
bp.write_text(bp.read_text(encoding="utf-8").replace("not a mood", "not a whim"), encoding="utf-8")
print("done")

from pathlib import Path
root = Path(r"C:\AndroidStudioProjects\batch20-hubs\betitaly")
old = '<script src="/js/i18n-more6.js?v=bi1"></script>\n<script src="/js/i18n.js?v=bi1"></script>'
new = '<script src="/js/i18n-more6.js?v=bi1"></script>\n<script src="/js/i18n-more7.js?v=bi1"></script>\n<script src="/js/i18n.js?v=bi1"></script>'
for p in root.glob("*.html"):
    t = p.read_text(encoding="utf-8")
    if old in t:
        p.write_text(t.replace(old, new), encoding="utf-8")
        print("ok", p.name)
    else:
        print("skip", p.name)

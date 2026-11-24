#!/usr/bin/env python3
"""把資料夾內的 .md 轉成同名 .html,供 GitHub Pages 使用。
用法:pip install markdown pyyaml   然後   python3 build_site.py
Wiki 更新後重跑一次即可。"""
import os, re, html, sys
import markdown, yaml

ROOT = os.path.dirname(os.path.abspath(__file__))
SLIDES = "https://claude.ai/artifact/X1tYwyXWwQr4K1spMCeQX2"
SKIP = {"CLAUDE.md"}
NAV = [("首頁", "index.html"), ("綜述", "wiki/overview.html"), ("目錄", "wiki/index.html"),
       ("指標總比較", "wiki/comparisons/risk-metrics-comparison.html"), ("AGENTS", "AGENTS.html")]

CSS = """
:root{--bg:#fbfaf7;--fg:#23262d;--mute:#667085;--line:#e2ddd0;--acc:#1f8a7d;--card:#fff;--code:#f1eee6}
@media(prefers-color-scheme:dark){:root{--bg:#16181d;--fg:#e8e6df;--mute:#a3a8b3;--line:#2e323b;--acc:#5cc6b8;--card:#1f232b;--code:#262a33}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.75 "Noto Sans TC","PingFang TC","Microsoft JhengHei",system-ui,sans-serif}
header{border-bottom:1px solid var(--line);background:var(--card);position:sticky;top:0;z-index:5}
nav{max-width:920px;margin:0 auto;padding:12px 20px;display:flex;flex-wrap:wrap;gap:6px 20px;font-size:15px}
nav a{color:var(--fg);text-decoration:none}nav a:hover{color:var(--acc)}
main{max-width:920px;margin:0 auto;padding:28px 20px 80px}
h1{font-size:2rem;line-height:1.3;margin:.4em 0 .6em}h2{font-size:1.45rem;margin:2em 0 .6em;padding-bottom:.25em;border-bottom:1px solid var(--line)}h3{font-size:1.15rem;margin:1.6em 0 .5em}
a{color:var(--acc)}code{background:var(--code);padding:.1em .35em;border-radius:4px;font-size:.9em}
pre{background:var(--code);padding:14px 16px;border-radius:8px;overflow-x:auto;line-height:1.5}pre code{background:none;padding:0}
pre.mermaid{background:none;text-align:center}
.wrap{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:.93em;background:var(--card)}
th,td{border:1px solid var(--line);padding:8px 12px;text-align:left;vertical-align:top}th{background:var(--code)}
blockquote{margin:1em 0;padding:.4em 1em;border-left:4px solid var(--acc);background:var(--card);color:var(--mute)}
.meta{font-size:13px;color:var(--mute);background:var(--card);border:1px solid var(--line);border-radius:8px;padding:8px 12px;margin-bottom:1.2em;line-height:1.6}
mjx-container[display=true]{overflow-x:auto;overflow-y:hidden}
footer{max-width:920px;margin:0 auto;padding:0 20px 40px;font-size:13px;color:var(--mute)}
"""

def extract(pattern, text, store, tag, flags=0):
    def rep(m):
        store.append(m.group(0)); return f"@@{tag}{len(store)-1}@@"
    return re.sub(pattern, rep, text, flags=flags)

def convert(md_text):
    code, math = [], []
    t = extract(r"```.*?```", md_text, code, "C", re.S)
    t = extract(r"`[^`\n]+`", t, code, "C")
    t = extract(r"\$\$.+?\$\$", t, math, "M", re.S)
    t = extract(r"(?<!\\)\$(?!\$)[^\n$]+?(?<!\\)\$", t, math, "M")
    t = re.sub(r"@@C(\d+)@@", lambda m: code[int(m.group(1))], t)
    body = markdown.markdown(t, extensions=["tables", "fenced_code", "sane_lists"])
    body = re.sub(r"@@M(\d+)@@", lambda m: html.escape(math[int(m.group(1))], quote=False), body)
    body = re.sub(r'<pre><code class="language-mermaid">(.*?)</code></pre>',
                  lambda m: '<pre class="mermaid">' + html.unescape(m.group(1)) + "</pre>", body, flags=re.S)
    body = re.sub(r"<table>", '<div class="wrap"><table>', body).replace("</table>", "</table></div>")
    return body

def split_front(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m: return {}, text
    try: return (yaml.safe_load(m.group(1)) or {}), m.group(2)
    except Exception: return {}, m.group(2)

def fix_links(body):
    def rep(m):
        url = m.group(1)
        if re.match(r"^(https?:|mailto:|#)", url): return m.group(0)
        return 'href="' + re.sub(r"\.md(#|$)", r".html\1", url) + '"'
    return re.sub(r'href="([^"]+)"', rep, body)

def page(rel, body, title, meta_html):
    depth = rel.count("/")
    pre = "../" * depth
    nav = "".join(f'<a href="{pre}{h}">{n}</a>' for n, h in NAV) + f'<a href="{SLIDES}">教學簡報</a>'
    mermaid = ('<script type="module">import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";'
               'mermaid.initialize({startOnLoad:true});</script>') if 'class="mermaid"' in body else ""
    return f"""<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><style>{CSS}</style>
<script>window.MathJax={{tex:{{inlineMath:[['$','$']],displayMath:[['$$','$$']]}}}};</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script></head>
<body><header><nav>{nav}</nav></header><main>{meta_html}{body}</main>
<footer>投資風險衡量 LLM Wiki · 由 Agent 維護的 markdown 知識庫</footer>{mermaid}</body></html>"""

def meta_block(fm):
    if not fm: return ""
    items = []
    for k, v in fm.items():
        if k == "source_url": v = f'<a href="{html.escape(str(v))}">{html.escape(str(v))}</a>'
        elif isinstance(v, list): v = html.escape("、".join(map(str, v)))
        else: v = html.escape(str(v))
        items.append(f"<b>{html.escape(str(k))}</b>:{v}")
    return '<div class="meta">' + " ｜ ".join(items) + "</div>"

count = 0
for d, _, files in os.walk(ROOT):
    for f in files:
        if not f.endswith(".md") or f in SKIP: continue
        path = os.path.join(d, f); rel = os.path.relpath(path, ROOT)
        fm, text = split_front(open(path, encoding="utf-8").read())
        h1 = re.search(r"^#\s+(.+)$", text, re.M)
        title = h1.group(1).strip() if h1 else f
        out_rel = "index.html" if rel == "README.md" else rel[:-3] + ".html"
        body = fix_links(convert(text))
        out = os.path.join(ROOT, out_rel)
        open(out, "w", encoding="utf-8").write(page(out_rel, body, title, meta_block(fm)))
        count += 1
open(os.path.join(ROOT, ".nojekyll"), "w").close()
print(f"built {count} pages")

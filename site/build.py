# Baut die GitHub-Pages-Seite aus README-Inhalten, docs/*.md und CHANGELOG.md
import os, re, sys, shutil, html, markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "_site")
REPO = "https://github.com/Exorzist26666/ds-toolkit-public"
D = os.path.join(ROOT, "docs")

if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)
shutil.copytree(os.path.join(D, "img"), os.path.join(OUT, "img"))

cl = open(os.path.join(ROOT, "CHANGELOG.md"), encoding="utf-8").read()
m = re.search(r"^## v(\S+)", cl, re.M)
VER = m.group(1) if m else ""
DL = "%s/releases/latest/download/DS-Toolkit-Setup-v%s.zip" % (REPO, VER) if VER else REPO + "/releases"

CSS = """
:root{--bg:#0f1115;--panel:#171a20;--panel2:#1d2129;--text:#eceef1;--muted:#9aa1ac;--acc:#ff6a2b;--acc2:#ff3b5c;--line:#272c35}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.6 'Segoe UI',system-ui,-apple-system,sans-serif}
a{color:#7cc4ff;text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
header.top{position:sticky;top:0;z-index:10;background:rgba(15,17,21,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
header.top .wrap{display:flex;align-items:center;gap:22px;height:60px}
.brand{font-weight:800;letter-spacing:4px;font-size:18px;color:var(--text)}
.brand span{background:linear-gradient(90deg,var(--acc),var(--acc2));-webkit-background-clip:text;background-clip:text;color:transparent}
nav.links{margin-left:auto;display:flex;gap:18px;flex-wrap:wrap}nav.links a{color:var(--muted);font-weight:600;font-size:15px}nav.links a:hover{color:var(--text);text-decoration:none}
.btn{display:inline-block;padding:13px 24px;border-radius:10px;font-weight:700;color:#fff;background:linear-gradient(90deg,var(--acc),var(--acc2));box-shadow:0 8px 24px rgba(255,80,60,.25)}
.btn:hover{text-decoration:none;filter:brightness(1.08)}
.btn.ghost{background:transparent;border:1px solid var(--line);box-shadow:none;color:var(--text)}
.hero{padding:64px 0 40px}.hero .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center}
.hero h1{font-size:46px;line-height:1.1;margin:0 0 14px;letter-spacing:1px}
.hero p.lead{color:var(--muted);font-size:18px;margin:0 0 26px}
.hero .ver{display:inline-block;border:1px solid var(--acc);color:var(--acc);border-radius:20px;padding:2px 12px;font-size:13px;margin-bottom:16px}
.hero .cta{display:flex;gap:12px;flex-wrap:wrap}.hero .small{color:var(--muted);font-size:13px;margin-top:12px}
.hero img{width:100%;border-radius:12px;border:1px solid var(--line);box-shadow:0 20px 60px rgba(0,0,0,.5)}
section{padding:56px 0;border-top:1px solid var(--line);scroll-margin-top:60px}
section h2{font-size:30px;margin:0 0 8px}section p.sub{color:var(--muted);margin:0 0 28px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden;display:flex;flex-direction:column;color:var(--text)}
.card:hover{border-color:var(--acc);text-decoration:none}
.card img{width:100%;height:170px;object-fit:cover;object-position:top;border-bottom:1px solid var(--line)}
.card div{padding:14px 16px}.card h3{margin:0 0 4px;font-size:17px}.card p{margin:0;color:var(--muted);font-size:14px}
.steps{counter-reset:s;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}
.step{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:18px}
.step:before{counter-increment:s;content:counter(s);display:inline-grid;place-items:center;width:30px;height:30px;border-radius:50%;background:linear-gradient(90deg,var(--acc),var(--acc2));font-weight:800;margin-bottom:8px}
.step h3{margin:4px 0 6px;font-size:17px}.step p{margin:0;color:var(--muted);font-size:14px}
table{border-collapse:collapse;width:100%;margin:18px 0}th,td{border:1px solid var(--line);padding:9px 12px;text-align:left;vertical-align:top}th{background:var(--panel2)}
code{background:#0b0d10;border:1px solid var(--line);border-radius:5px;padding:1px 5px;font-family:Consolas,monospace;font-size:13px;word-break:break-all}
.note{background:var(--panel);border-left:4px solid #7cc4ff;padding:12px 16px;border-radius:6px;color:#c9d3e0}
footer{border-top:1px solid var(--line);padding:28px 0;color:var(--muted);font-size:14px}
@media(max-width:820px){.hero .wrap{grid-template-columns:1fr}.hero h1{font-size:34px}nav.links{display:none}}
/* Anleitung */
.doc{display:grid;grid-template-columns:230px 1fr;gap:34px;padding:30px 20px 80px;max-width:1180px;margin:0 auto}
.doc aside{position:sticky;top:80px;align-self:start;max-height:calc(100vh - 100px);overflow:auto}
.doc aside a{display:block;color:var(--muted);padding:6px 10px;border-radius:6px;font-weight:600}.doc aside a:hover{background:var(--panel);color:var(--text);text-decoration:none}
.doc main section{scroll-margin-top:70px;padding:10px 0 28px;border-top:none;border-bottom:1px solid var(--line)}
.doc h1{font-size:28px;margin:18px 0 12px}.doc h2{font-size:20px;margin:26px 0 8px;padding-left:10px;border-left:4px solid var(--acc)}
.doc img{max-width:100%;max-height:820px;border:1px solid var(--line);border-radius:8px;display:block;margin:12px 0}
.doc blockquote{margin:12px 0;padding:8px 14px;border-left:4px solid #7cc4ff;background:#151a22;color:#c9d3e0}
.doc pre{background:#0b0d10;border:1px solid var(--line);border-radius:6px;padding:10px;overflow:auto}.doc pre code{border:0;padding:0}
@media(max-width:820px){.doc{grid-template-columns:1fr}.doc aside{position:static;max-height:none}}
"""

def page(title, body, desc):
    return """<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title><meta name="description" content="%s"><style>%s</style></head><body>
<header class="top"><div class="wrap"><a class="brand" href="index.html"><span>DS</span> TOOLKIT</a>
<nav class="links"><a href="index.html#funktionen">Funktionen</a><a href="index.html#installation">Installation</a><a href="anleitung.html">Anleitung</a><a href="index.html#updates">Updates</a><a href="%s">GitHub</a></nav>
<a class="btn" style="padding:8px 16px" href="%s">Download</a></div></header>
%s
<footer><div class="wrap">DS Toolkit %s für DaVinci Resolve Studio · <a href="%s">GitHub</a> · <a href="%s/releases">Alle Versionen</a> · <a href="%s/blob/main/CHANGELOG.md">Änderungen</a></div></footer>
</body></html>""" % (title, desc, CSS, REPO, DL, body, VER, REPO, REPO, REPO)

CARD_TXT = {
    "medien": "Media Pool nach Format sortieren, Clips umbenennen, Ungenutztes finden und Proxys per Klick erstellen.",
    "schnitt": "Stille automatisch rausschneiden oder Clips auf echte Schläge des Songs schneiden – Kick, Snare, Hi-Hat, Drops.",
    "timeline": "Farbige Beat-Marker zum Einrasten, Varianten der Timeline und eine Schnitt-Statistik.",
    "text": "8 animierte Titel – Impact, Glitch, Neon, Chrome & Co. – per Klick am Playhead, im Inspector frei bearbeitbar.",
    "masken": "8 Masken-Übergänge wie Ink Splash oder Smoke: Der neue Clip erscheint in Form der Maske.",
    "video-fx": "8 Effekte wie Kamera-Shake, Glitch, Zoom Punch oder VHS – direkt auf den Clip, ideal auf den Beat.",
    "color": "Look kopieren und auf beliebig viele Clips übertragen, .drx-Looks und LUTs in einem Rutsch.",
    "audio": "Lautheit messen und normalisieren, Ton klarer machen, Rauschen entfernen, externe Mikros automatisch synchronisieren.",
    "export": "Doppel-Export: Master in voller Qualität für Instagram plus kompakte Datei mit Größen-Grenze.",
    "info": "Bebilderte Anleitung direkt im Tool und Updates mit einem Klick – ohne Konto.",
}

# ---------------------------------------------------------------- Anleitung
files = ["README.md"] + sorted(f for f in os.listdir(D) if re.match(r"\d\d-.*\.md$", f))
anchor = {f: (re.sub(r"^\d\d-", "", f[:-3]) if f != "README.md" else "start") for f in files}
anchor["10-info.md"] = "info"
parts, nav, cards = [], [], []
for f in files:
    md = open(os.path.join(D, f), encoding="utf-8").read()
    md = re.sub(r"^\[.*?\]\(.*?\.md\).*$", "", md, flags=re.M)
    md = re.sub(r"\]\((\d\d-[\w-]+\.md)\)", lambda mm: "](#%s)" % anchor[mm.group(1)], md)
    md = md.replace("](README.md)", "](#start)").replace("](../CHANGELOG.md)", "](%s/blob/main/CHANGELOG.md)" % REPO)
    md = md.replace("](../../../releases)", "](%s/releases)" % REPO).replace("](../README.md#-installation)", "](index.html#installation)")
    title = re.search(r"^# (.+)$", md, re.M).group(1)
    short = re.sub(r"^\d\d – ", "", title)
    nav.append('<a href="#%s">%s</a>' % (anchor[f], html.escape(short)))
    parts.append('<section id="%s">%s</section>' % (anchor[f], markdown.markdown(md, extensions=["tables", "fenced_code"])))
    if f != "README.md":
        img = re.search(r"!\[[^\]]*\]\((img/[^)]+)\)", md)
        cards.append((anchor[f], short, img.group(1) if img else "", CARD_TXT.get(anchor[f], "")))
open(os.path.join(OUT, "anleitung.html"), "w", encoding="utf-8").write(page(
    "DS Toolkit – Anleitung", '<div class="doc"><aside>%s</aside><main>%s</main></div>' % ("".join(nav), "".join(parts)),
    "Bebilderte Anleitung zum DS Toolkit für DaVinci Resolve"))

# ---------------------------------------------------------------- Startseite
card_html = "".join('<a class="card" href="anleitung.html#%s"><img src="%s" alt="%s" loading="lazy"><div><h3>%s</h3><p>%s</p></div></a>'
                    % (a, i, html.escape(t), html.escape(t), html.escape(x)) for a, t, i, x in cards)
body = """
<div class="hero"><div class="wrap"><div>
<span class="ver">Version %s</span>
<h1>Mehr schneiden,<br>weniger klicken.</h1>
<p class="lead">Ein Werkzeug-Fenster für DaVinci Resolve Studio: Beat-Schnitt auf echte Schläge, animierte Titel, Masken-Übergänge, Video-Effekte, Looks übertragen, Ton angleichen und Doppel-Export – jeweils mit einem Klick.</p>
<div class="cta"><a class="btn" href="%s">⬇ Download v%s</a><a class="btn ghost" href="anleitung.html">Anleitung ansehen</a></div>
<p class="small">Windows 10/11 · DaVinci Resolve Studio · kostenlos · Updates per Klick</p>
</div><img src="img/02-schnitt.png" alt="DS Toolkit – Tab Schnitt"></div></div>

<section id="funktionen"><div class="wrap"><h2>Funktionen</h2><p class="sub">Zehn Tabs, in der Reihenfolge eines typischen Projekts. Klick auf eine Karte öffnet die Anleitung dazu.</p>
<div class="grid">%s</div></div></section>

<section id="installation"><div class="wrap"><h2>Installation</h2><p class="sub">Einmal doppelklicken – das Setup erledigt den Rest.</p>
<div class="steps">
<div class="step"><h3>Herunterladen</h3><p><a href="%s">DS-Toolkit-Setup-v%s.zip</a> laden. Nur diese Datei wird für die Installation gebraucht.</p></div>
<div class="step"><h3>Entpacken</h3><p>Rechtsklick auf die ZIP-Datei › <i>Alle extrahieren</i>. DaVinci Resolve schließen.</p></div>
<div class="step"><h3>INSTALL.bat starten</h3><p>Doppelklick, Admin-Abfrage mit <i>Ja</i> bestätigen. Jeder Schritt wird mit <b>OK</b> angezeigt.</p></div>
<div class="step"><h3>Loslegen</h3><p>Resolve starten › <b>Workspace › Scripts › DS Toolkit</b>.</p></div>
</div>
<table><tr><th>Baustein</th><th>Wozu</th><th>Was das Setup macht</th></tr>
<tr><td><b>DS Toolkit</b></td><td>Fenster, Titel, Effekte, Masken, Color-Tools, Anleitung</td><td>wird installiert bzw. aktualisiert</td></tr>
<tr><td><b>Python 3</b></td><td>Resolve braucht es, um Python-Skripte auszuführen</td><td>wird installiert, falls es fehlt</td></tr>
<tr><td><b>numpy</b></td><td>Audio-Analyse (Beat-Erkennung, Lautheit)</td><td>wird installiert, falls es fehlt</td></tr>
<tr><td><b>ffmpeg</b></td><td>Audio, Export, Proxys</td><td>wird installiert, falls es fehlt</td></tr></table>
<p class="note">Voraussetzungen: Windows 10/11, <a href="https://www.blackmagicdesign.com/de/products/davinciresolve/studio">DaVinci Resolve Studio</a> und Internet beim ersten Setup.
Falls etwas nicht automatisch klappt, sagt das Setup genau, was fehlt – dann <a href="https://www.python.org/downloads/">Python</a> bzw.
<a href="https://www.gyan.dev/ffmpeg/builds/">ffmpeg</a> von Hand installieren und <code>INSTALL.bat</code> erneut starten.</p>
</div></section>

<section id="updates"><div class="wrap"><h2>Updates</h2>
<p class="sub">Im Toolkit: Tab <b>Info › Nach Updates suchen</b> – lädt die neueste Version und installiert sie. Kein Konto, keine Anmeldung.
Danach das Toolkit-Fenster schließen und neu öffnen.</p>
<div class="cta" style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn ghost" href="%s/releases">Alle Versionen</a><a class="btn ghost" href="%s/blob/main/CHANGELOG.md">Was ist neu?</a></div>
</div></section>
""" % (VER, DL, VER, card_html, DL, VER, REPO, REPO)
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(page(
    "DS Toolkit für DaVinci Resolve", body, "Werkzeug-Fenster für DaVinci Resolve Studio – Beat-Schnitt, Titel, Masken, Effekte, Audio und Export"))
open(os.path.join(OUT, ".nojekyll"), "w").write("")
print("Seite gebaut:", OUT, "Version", VER)

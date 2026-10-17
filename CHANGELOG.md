# Changelog – DS Toolkit

Hier stehen alle **fertigen Versionen** mit ihren Neuerungen. Jede Version gibt es unter [Releases](../../releases) als Vollinstallation (`Setup.zip`) und als Update-Datei (`.dsupdate`).

---

## v2.0 – 17.10.2026

### Neu
- **Neues Logo** (Timeline mit Abspielkopf) im Toolkit-Fenster, auf der Website und in der Anleitung.
- **Auf den Beat schneiden in 3 Schritten** (Tab Schnitt): Beat-Marker setzen → Marker selbst verschieben, löschen oder ergänzen → **Schnitt nach Markern**.
- **Takt-Raster wie bei Profi-Plugins:** Tempo und Takt werden erkannt. Muster *jeder Beat, Beat + Offbeat, halbe Zeit, jeder Takt, jeder 2. Takt* und **automatisch nach Energie** (laute Stellen schneller).
- **Material beim Schnitt nach Markern:** Video-Spur 1 der Reihe nach, Video-Spur 1 gemischt (kein Ausschnitt doppelt) oder markierte Clips im Media Pool.
- Marker-Versatz in Frames, **alle Marker verschieben**, Tempo halb/doppelt.
- **Jeder Tab hat seine eigene Farbe** – Reiter, Akzentlinie und Hauptbuttons passen zum Bereich, wie im Protokoll.

### Verbessert
- **Neue Schlag-Erkennung:** Kick/808, Clap/Snare und Hi-Hat werden mit 1 ms Genauigkeit gefunden – auch bei Bass-lastigen Songs.
- Das Takt-Raster richtet sich an Clap und Kick aus und liegt auf den Schlägen statt dazwischen.
- Projekt- und Timeline-Zeile oben ist farbig hervorgehoben.
- Neue, neutrale Vorschauen bei Text, Masken und FX.
- Beat-Marker und Marker-Werkzeuge sind vom Tab Timeline in den Tab Schnitt umgezogen.

### Behoben
- Ungenaue Beat-Schnitte: Das Raster wanderte über den Song weg, Marker saßen teils bis zu 100 ms neben dem Schlag.
- Bass-Brummen wurde als Snare oder Hi-Hat markiert.
- Versatz bei Clips mit anderer Bildrate (z. B. 60-fps-Material auf 24-fps-Timeline).

---

## v1.9 – 16.10.2026

Erste öffentliche Version.

### Funktionen
- **Medien:** Media Pool nach Format sortieren, Stapel-Umbenennung, ungenutzte und doppelte Clips finden, **Proxys per Klick** erstellen und verknüpfen.
- **Schnitt:** Stille entfernen (neue Timeline nur mit den lauten Abschnitten); **Beat-Schnitt** auf echte Schläge – Kick/Bass, Snare/Clap, Hi-Hat, Drops – mit „jeder 2./3./4.“, Empfindlichkeit sowie Mindest- und Höchstlänge.
- **Timeline:** farbige Beat-Marker (Rot Kick, Gelb Snare, Cyan Hi-Hat, Lila Drop), Varianten, Statistik, Marker als CSV.
- **Text:** 8 animierte Text+-Titel mit Vorschau, per Klick am Playhead auf eine eigene Spur – im Inspector voll bearbeitbar.
- **Masken:** 8 Masken-Übergänge (Ink Splash, Ink Drops, Brush, Smoke, Burn, Liquid, Glitch Blocks, Stripes) in 9:16 und 16:9 – der obere Clip erscheint per Klick in Form der Maske.
- **FX:** 8 Video-Effekte (Handheld, Impact Shake, Glitch, Zoom Punch, Whip Zoom, RGB Split, Flash Hit, Retro VHS) direkt auf den Clip am Playhead.
- **Color:** Look kopieren und einfügen (auch auf alle Clips danach / gleiche Datei / alle), .drx-Looks und LUTs auf viele Clips.
- **Audio:** Lautheit (LUFS) messen, Spur direkt normalisieren, Ton aufbereiten (Klarheit, Rauschen entfernen, Ausgleichen) inkl. automatischer Synchronisation externer Mikrofon-Aufnahmen.
- **Export:** Doppel-Export – Master in voller Qualität (Instagram) + kompakte Datei mit genauer Größen-Grenze (PC/WhatsApp), Standbild.

### Bedienung
- Kurzinfo an jedem Regler, „?“-Anleitung zu jedem Bereich, bebilderte Anleitung im Tab **Info** (auch offline).
- Bereiche einklappbar, Protokoll-Größe umschaltbar, Fenstergröße und letzter Tab werden gemerkt.
- **Updates per Klick** (Tab Info › Nach Updates suchen) – ohne Konto.
- **Setup mit einem Doppelklick** – installiert Python, numpy und ffmpeg automatisch, falls sie fehlen.

> Nach der Installation Resolve einmal neu starten.

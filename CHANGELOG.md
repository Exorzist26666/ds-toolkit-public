# Changelog – DS Toolkit

Hier stehen alle **fertigen Versionen** mit ihren Neuerungen. Jede Version gibt es unter [Releases](../../releases) als Vollinstallation (`Setup.zip`) und als Update-Datei (`.dsupdate`).

---

## v2.1 – 24.10.2026

### Neu
- **Speedramp** (Tab Schnitt): 13 Verläufe (Speed Up, Slow Down, Fast-Slow-Fast, Boomerang, Freeze …), Umkehren/Spiegeln und ein eigener **Kurven-Editor** mit ziehbaren Punkten und Bézier-Griffen.
- **Font Scramble** (Tab Text): Text wechselt animiert durch verschiedene Schriften – ganzes Wort, einzelne Buchstaben oder ein einzelnes Wort, auf Wunsch mit Symbolschriften.
- **Lens Streak** (Tab FX): Lichtstreifen auf hellen Stellen.
- **Schnitt-Übergänge** (Tab Masken): Whip Pan, Slide Blur, Zoom In, Zoom Out, Spin, Zoom Spin, Glitch Cut, Flash Cut – direkt auf einen harten Schnitt, ohne Überlappung, mit Bewegungsunschärfe.
- **Shape Reveals** (Balken, Chevron, Rauten, Kreise, Iris, Jalousie, Dreiecke, Schlitz) und **Kachel-Reveals** (Zufall, Treppe, Mitte, Spirale, Zeilen, Fein) in 4K für 16:9 und 9:16.
- **Portal-Übergang:** Ein Kreis öffnet sich, der nächste Clip zoomt aus dem Portal heran.
- **Light Leaks & Flashes:** 8 Lichteffekte (Warm Leak, Golden Flare, Film Burn, White Flash …) mit Höhepunkt am Playhead, auf eigener Spur.
- **Look-Bibliothek** (Tab Color): 14 fertige Looks plus Day-for-Night, Color Pop, Atmosphäre und Clarity – mit Stärke-Regler und Vorher/Nachher-Vorschau. Deine eigenen Grades bleiben unverändert.
- **Clip Check** (Tab Color): Belichtungswarnung für abgesoffene Schatten und ausgebrannte Lichter.

### Verbessert
- **Kleinere Updates:** Ab jetzt werden nur noch die Teile geladen, die sich geändert haben – meist wenige hundert KB statt des kompletten Pakets. (Das Update von 2.0 auf 2.1 wird noch einmal komplett geladen.)
- Anleitung um alle neuen Funktionen ergänzt.

---

## v2.0 – 17.10.2026

### Neu
- **Neues Logo** im Toolkit-Fenster, auf der Website und in der Anleitung.
- **Auf den Beat schneiden in 3 Schritten** (Tab Schnitt): Beat-Marker automatisch setzen → Marker selbst verschieben, löschen oder ergänzen → **Schnitt nach Markern**.
- **Takt-Raster:** Tempo und Takt des Songs werden erkannt. Muster *jeder Beat, Beat + Offbeat, halbe Zeit, jeder Takt, jeder 2. Takt* und **automatisch nach Energie** (laute Stellen schneller geschnitten).
- **Material beim Schnitt nach Markern:** Clips von Video-Spur 1 der Reihe nach, gemischt (kein Ausschnitt doppelt) oder die markierten Clips im Media Pool.
- Marker-Versatz in Frames, **alle Marker verschieben**, Tempo halb/doppelt.
- **Jeder Tab hat seine eigene Farbe** – Reiter, Akzentlinie und Hauptbuttons passen zum Bereich, wie im Protokoll.

### Verbessert
- **Genauere Schlag-Erkennung:** Kick/Bass, Clap/Snare und Hi-Hat werden zuverlässiger erkannt und genauer auf den Anschlag gesetzt.
- Das Takt-Raster richtet sich an Kick und Clap aus.
- Schnitte liegen bildgenau auf den Markern.
- Projekt- und Timeline-Zeile oben ist farbig hervorgehoben.
- Neue Vorschauen bei Text, Masken und FX.
- Beat-Marker und Marker-Werkzeuge sind vom Tab Timeline in den Tab Schnitt umgezogen.

### Behoben
- Beat-Schnitte und Beat-Marker saßen teils nicht genau auf dem Schlag.

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

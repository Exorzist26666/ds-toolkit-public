# 02 – Schnitt

[← Medien](01-medien.md) · [Übersicht](README.md) · [Weiter: Timeline →](03-timeline.md)

![Tab Schnitt](img/02-schnitt.png)

## Stille entfernen
Schneidet leise Stellen aus den Clips auf **Video-Spur 1** und legt eine **neue Timeline** an – ideal für Sprache/Talking-Head.

| Regler | Bedeutung | Tipp |
|---|---|---|
| **Schwelle (dB)** | alles leiser gilt als Stille | -40 für Sprache, -45/-50 bei leiser Aufnahme |
| **Min. Pause (s)** | kürzere Pausen bleiben drin | 0,4 s wirkt natürlich |
| **Min. Ton (s)** | kürzere Geräusche zählen nicht als Ton | gegen Klicks, Atmer |
| **Rand (s)** | Sicherheitsabstand vor/nach jedem Abschnitt | 0,1 s |

## Auf den Beat schneiden – in 3 Schritten
Wie bei den Profi-Plugins: erst Marker automatisch setzen, dann **selbst nachbessern**, dann auf genau diese Marker schneiden.

### 1. Beat-Marker setzen
1. Song auf eine Audio-Spur legen und deren Nummer bei **Musik auf Audio-Spur** eintragen (A1 = 1).
2. **Erkennung** wählen:
   - **Takt-Raster (empfohlen):** Tempo und Takt des Songs werden erkannt, jeder Beat rastet auf den echten Anschlag ein – gleichmäßig über den ganzen Song, ohne Wegdriften.
   - **Einzelne Schläge:** nur die hörbaren Schläge – 🟥 Kick/Bass (neuer Bass-/808-Einsatz), 🟨 Clap/Snare (lauter, heller Knall), 🩵 Hi-Hat (kurzer Klick); mit *jeder 2./3./4.* und Empfindlichkeit.
3. **Muster** (nur Takt-Raster):

| Muster | Wirkung |
|---|---|
| Jeder Beat | Schnitt auf jedem Schlag |
| Beat + Offbeat | doppelt so schnell (Achtel) |
| Halbe Zeit | jeder 2. Beat |
| Jeder Takt | alle 4 Beats |
| Jeder 2. Takt | alle 8 Beats, sehr ruhig |
| Automatisch nach Energie | laute Stellen jeder Beat, mittlere halbe Zeit, ruhige jeder Takt |

4. **Tempo:** nur ändern, wenn die Marker doppelt oder halb so dicht liegen wie der gefühlte Takt.
5. **Versatz (Frames):** verschiebt alle neuen Marker. Die Marker sitzen genau am Beginn des Schlags. Wirken sie beim Abspielen zu früh, weil der Ton über Bluetooth oder ein Audio-Interface verzögert ankommt, *+1* bis *+3* probieren. *-1* = Schnitt ein Bild früher (knackiger).
6. **Beat-Marker setzen**.

| Farbe | Bedeutung |
|---|---|
| 🟦 Blau | Takt-Anfang |
| 🟩 Grün | Beat |
| 🩵 Sky | Offbeat |
| 🟪 Lila | Einsatz/Drop |
| 🟥 Rot · 🟨 Gelb · 🩵 Cyan | Kick · Snare · Hi-Hat (Modus *Einzelne Schläge*) |

### 2. Marker bearbeiten
Direkt in der Timeline: **ziehen** = verschieben, **anklicken + Entf** = löschen, **Taste M** = neuer Marker. Mit **Snapping (Taste N)** rastet alles auf den Markern ein.

- **Farbe löschen** – alle Marker einer Farbe auf einmal (*All* = alle).
- **Alle verschieben** – alle Marker (oder nur die gewählte Farbe) um X Frames früher/später.
- **Marker exportieren / importieren** – als CSV (`Sekunde;Name;Farbe;Notiz`).

### 3. Schnitt nach Markern
Schneidet **genau auf die Marker** der aktuellen Timeline – auch auf die, die du selbst gesetzt oder verschoben hast. Ergebnis: neue Timeline *„… – Marker-Schnitt“*, das Original bleibt.

| Material | Was passiert |
|---|---|
| Video-Spur 1 der Reihe nach | deine (vorgeschnittenen) Clips in ihrer Reihenfolge, jeweils auf den Markerabstand gekürzt |
| Video-Spur 1 gemischt | Ausschnitte aus allen Clips abwechselnd, kein Ausschnitt doppelt, nie zweimal derselbe Clip hintereinander – jeder Klick = neue Mischung |
| Markierte Clips im Media Pool | wie gemischt, mit den im Media Pool markierten Clips |

- **Marker:** *Alle Marker* oder nur eine Farbe (z. B. nur Blau = jeder Takt).
- **Clip-Einstieg:** ab Clipanfang, ab 10 % oder ab Mitte.
- Jeder Clip wird **bildgenau** auf seinen Marker gelegt – auch bei 50/60-fps-Material auf 24/25-fps-Timelines summiert sich kein Versatz auf.
- **Alles in einem** = Marker setzen und sofort schneiden.

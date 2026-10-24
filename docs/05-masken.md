# 05 – Masken

[← Text](04-text.md) · [Übersicht](README.md) · [Weiter: Video-FX →](06-video-fx.md)

![Tab Masken](img/05-masken.png)

Der Tab hat drei Bereiche: **Schnitt-Übergänge** (direkt auf einen harten Schnitt), **Masken-Übergänge & Shape Reveals** (Clip B erscheint in Form einer Maske) und **Light Leaks & Flashes** (Lichteffekte über dem Bild).

## Schnitt-Übergänge
Whip Pan, Slide Blur, Zoom In, Zoom Out, Spin, Zoom Spin, Glitch Cut, Flash Cut – direkt auf den Schnitt zwischen zwei Clips, **ohne Überlappung oder Handles**.

1. Zwei Clips liegen **direkt hintereinander auf derselben Spur** (harter Schnitt).
2. Playhead **auf den Schnitt** setzen (2–3 Bilder daneben reicht auch).
3. Übergang anklicken, **Richtung**, **Länge (Bilder)**, **Stärke** und **Bewegungsunschärfe** wählen → **Auf Schnitt am Playhead**.

Das Ende von Clip A und der Anfang von Clip B bekommen je eine Hälfte – Tempo und Richtung laufen nahtlos durch. Bewegungsunschärfe ist eingebaut, Bildränder werden gespiegelt (keine schwarzen Ecken).

| Einstellung | Bedeutung |
|---|---|
| **Richtung** | links/rechts/oben/unten bei Whip Pan und Slide, Drehsinn bei Spin (bei Zoom, Glitch, Flash ohne Wirkung) |
| **Länge (Bilder)** | Gesamtlänge – 8–14 = schnell, 20+ = ruhig |
| **Stärke** | 1.0 = Standard |
| **Bewegungsunschärfe** | 0 = gestochen scharf, 1 = natürlich, 2–3 = sehr verwischt |

- **Ändern:** Clip › Fusion-Seite › Node `DS<Name>1_Ctl` (Start, Länge, Stärke, Unschärfe).
- **Entfernen:** Playhead auf den Schnitt › **Übergang entfernen** – andere DS-Effekte bleiben erhalten.

## Masken-Übergänge & Shape Reveals
Clip B erscheint **in Form der Maske** über Clip A. Zur Auswahl stehen:
- **Masken:** Ink Splash, Ink Drops, Brush Strokes, Smoke, Burn, Liquid Wipe, Glitch Blocks, Stripes
- **Shape Reveals:** Balken, Chevron, Rauten, Kreise, Iris, Jalousie, Dreiecke, Schlitz – geometrisch mit scharfen Kanten
- **Kacheln:** Zufall, Treppe, Mitte, Spirale, Zeilen, Fein – Kacheln poppen nacheinander auf
- **Portal** (Mitte, Links, Rechts): ein Kreis öffnet sich an der Stelle, Clip B zoomt dabei aus dem Portal heran

Alle Masken gibt es in 4K für **16:9 und 9:16** – das passende Format wird automatisch zur Timeline gewählt.

### Übergang am Playhead
1. **Clip A** liegt auf einer Spur, **Clip B auf einer Spur darüber** – beide **überlappen** sich.
2. Playhead dorthin stellen, wo der Übergang beginnen soll (innerhalb von Clip B).
3. Maske anklicken → **Übergang am Playhead**.

Ergebnis: Vor dem Playhead siehst du A, dann erscheint B in Form der Maske, danach ist B voll sichtbar.

```
V2   [======= Clip B =======]
V1 [===== Clip A =====]
              ^ Playhead = Start des Übergangs
```

> **Wichtig:** Liegen A und B **hintereinander auf derselben Spur**, gibt es unter der Maske nichts – dann siehst du dort nur Schwarz. Für harte Schnitte auf einer Spur die **Schnitt-Übergänge** oben nehmen.

- **Ändern:** Fusion-Clip anklicken › Fusion-Seite. Beim Portal: Node `DS_PortalZoom` (Pivot) und Maske verschieben, um die Stelle anzupassen.
- **Auflösen:** Rechtsklick auf den Fusion-Clip › *Decompose in Place*.

### Nur Maske einfügen
Legt das Schwarz-Weiß-Video auf die Spur **DS Masken** an die freie Stelle am Playhead (es wird keine neue Spur pro Maske angelegt) – z. B. für eigene Fusion-Comps oder *Color › External Matte*. Weiß = sichtbar, Schwarz = durchsichtig.

**Masken-Ordner öffnen** zeigt die Masken-Videos im Explorer.

## Light Leaks & Flashes
Warm Leak, Golden Flare, Pink Haze, Blue Prism, Film Burn, White Flash, Rainbow Leak, Bokeh Lights.

1. Playhead auf den Beat oder Schnitt setzen, an dem das Licht **am hellsten** sein soll.
2. Licht anklicken (Vorschau), **Stärke (%)** und **Position** wählen → **Am Playhead einfügen (Spur 'DS Licht')**.

Das Licht kommt auf die Spur **DS Licht** über alles andere und wird per *Screen* eingerechnet – nur das Leuchten wirkt, Schwarz ist unsichtbar. Andere Clips werden nicht verschoben.

- **Position:** Höhepunkt am Playhead (Standard), Start am Playhead oder Ende am Playhead.
- **Ändern:** Licht-Clip anklicken › Inspector › Deckkraft / Composite-Modus. Kürzer: Clip einfach kürzer ziehen.
- **Tipp:** *White Flash* genau auf einen Schnitt = klassischer Flash-Übergang.

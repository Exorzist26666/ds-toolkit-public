# 05 – Masken

[← Text](04-text.md) · [Übersicht](README.md) · [Weiter: Video-FX →](06-video-fx.md)

![Tab Masken](img/05-masken.png)

Masken-Übergänge: Clip B erscheint **in Form der Maske** (Ink Splash, Ink Drops, Brush Strokes, Smoke, Burn, Liquid Wipe, Glitch Blocks, Stripes) über Clip A.

## Übergang am Playhead
1. **Clip A** liegt auf einer Spur, **Clip B auf einer Spur darüber** – beide **überlappen** sich.
2. Playhead dorthin stellen, wo der Übergang beginnen soll (innerhalb von Clip B).
3. Maske anklicken → **Übergang am Playhead**.

Ergebnis: Vor dem Playhead siehst du A, dann erscheint B in Form der Maske, danach ist B voll sichtbar.

```
V2   [======= Clip B =======]
V1 [===== Clip A =====]
              ^ Playhead = Start des Übergangs
```

> **Wichtig:** Liegen A und B **hintereinander auf derselben Spur**, gibt es unter der Maske nichts – dann siehst du dort nur Schwarz.

- **Ändern:** Fusion-Clip anklicken › Fusion-Seite.
- **Auflösen:** Rechtsklick auf den Fusion-Clip › *Decompose in Place*.

## Nur Maske einfügen
Legt das Schwarz-Weiß-Video auf die Spur **DS Masken** an die freie Stelle am Playhead (es wird keine neue Spur pro Maske angelegt) – z. B. für eigene Fusion-Comps oder *Color › External Matte*. Weiß = sichtbar, Schwarz = durchsichtig.

**Masken-Ordner öffnen** zeigt die Masken-Videos (4K, 9:16 und 16:9). Das passende Format wird automatisch zur Timeline gewählt.

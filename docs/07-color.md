# 07 – Color

[← Video-FX](06-video-fx.md) · [Übersicht](README.md) · [Weiter: Audio →](08-audio.md)

![Tab Color](img/07-color.png)

## Look kopieren und einfügen
Wie Kopieren/Einfügen – alle Nodes werden übernommen.
1. Playhead auf den Clip mit dem fertigen Look → **1. Look merken** (das Feld darüber zeigt den gemerkten Clip).
2. Playhead auf einen anderen Clip → **2. Auf aktuellen Clip einfügen**. Beliebig oft wiederholbar.

Schneller:
- **Auf alle Clips danach** – rechts vom Playhead, gleiche Spur
- **Auf gleiche Datei** – alle Ausschnitte derselben Videodatei
- **Auf alle Clips** – alles

Der bisherige Look der Ziel-Clips wird ersetzt. Mit **… nicht überschreiben** bleiben bereits bearbeitete Clips (mehr als 1 Node) verschont.

## Look oder LUT auf viele Clips
**Clips** oben gilt für beide Buttons: alle Video-Spuren, nur V1, nur Clips mit Clipfarbe oder markierte Clips.

- **Look (.drx):** Color-Seite › Rechtsklick ins Bild › *Grab Still*, dann in der Galerie Rechtsklick › *Export* → `.drx`. Datei wählen › **Look anwenden**. *Keyframes*: normalerweise „Ohne Keyframes“.
- **LUT (.cube):** Datei wählen, **In Node Nr.** einstellen › **LUT setzen**. Die LUT muss im Resolve-LUT-Ordner liegen.

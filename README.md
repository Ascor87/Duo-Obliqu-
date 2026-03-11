# Duo-Oblique

A tactical two-player game on a classic peg solitaire board. CC BY 4.0

## 🎯 Spielziel & Siegbedingung

Im Gegensatz zum klassischen Solitär ist Duo Obliqué kein Solospiel zur Eliminierung aller Kugeln, sondern ein territoriales Verdrängungsspiel.

1. **Hauptziel:** Sichere dir die numerische Überlegenheit auf dem Brett.
2. **Der Mechanismus:** Reduziere die Gesamtanzahl der Murmeln durch Sprünge, während du versuchst, deine eigenen Steine in vorteilhaften Positionen zu halten oder den Gegner zu isolieren.
3. **Sieg:** Es gewinnt der Spieler, der nach dem letzten möglichen Zug mehr Murmeln seiner Farbe auf dem Spielfeld hat.


### 📊 Erweiterte Balance-Simulation (n=175)

Um die statistische Ausgeglichenheit zu verifizieren, wurden 175 Partien via Python-Skript simuliert. Die Agenten nutzten semi-randomisierte Züge mit einem Fokus auf gegnerische Elimination und nutzten die *Pie Rule* (Tauschregel) nach dem ersten Zug in 50 % der Fälle.

| Metrik | Ergebnis |
| :--- | :--- |
| **Gespielte Partien** | 175 |
| **Siege Spieler 1** | 37,7 % (66 Partien) |
| **Siege Spieler 2** | 45,1 % (79 Partien) |
| **Unentschieden (Patt)** | 17,1 % (30 Partien) |
| **Ø Züge pro Partie** | 17,9 |
| **Ø Kettensprünge pro Partie** | 2,6 |
| **Ø Verbleibende Murmeln** | 7,5 (gesamtes Brett) |

*Fazit der Simulation:* Das Spiel zeigt eine solide Balance. Der leichte statistische Überhang für Spieler 2 in dieser Stichprobe resultiert oft aus der defensiven Latenz des "Nachziehenden". Die Unentschieden-Quote von 17 % belegt, dass ein absichtliches Herbeiführen eines Patts eine valide Defensivstrategie bleibt.

🧠 Strategische Erkenntnisse (KI-Audit)
In Zusammenarbeit mit Large Language Models (Claude & Gemini) wurde Duo Obliqué auf seine Spieltheorie hin untersucht.
Wichtigste Erkenntnis: Eine rein defensive Spielweise ("eigene Steine schützen/opfern") führt gegen einen aggressiven Spieler in 86 % der Fälle zur Niederlage.
Aggressive Strategie: Priorisiert das Schlagen gegnerischer Murmeln.
Defensive Strategie: Versucht, die eigene Formation kompakt zu halten.
Tipp für Spieler: Duo Obliqué ist ein dynamisches Spiel. Passivität wird bestraft. Nutze die Tausch-Regel am Anfang weise, um nicht in eine reaktive Position gedrängt zu werden!

"""
Erzeugt drei miteinander korrelierte, normalverteilte Messreihen und speichert sie in
data.txt, data2.txt und data3.txt. Durch die Korrelation zeigt die 3D-Punktwolke in
ZweiterVersuch.py einen sichtbaren Zusammenhang (die Punkte liegen ungefähr auf einer
schiefen Ebene) statt einer unabhängigen Streuung.
"""

import sqlite3

import numpy as np

# Parameter
anzahl = 100
mittelwerte = [0, 0, 0]

# Kovarianzmatrix: Diagonale = Varianz jeder Reihe, Nebendiagonalen = Stärke des
# Zusammenhangs zwischen den Reihen (0 = unabhängig, nahe 1 = starker linearer Zusammenhang)
kovarianz = [
    [1.0, 0.8, 0.6],
    [0.8, 1.0, 0.7],
    [0.6, 0.7, 1.0],
]

DB_DATEI = "messwerte.db"


def speichere_als_txt(daten, dateiname):
    with open(dateiname, "w") as datei:
        for wert in daten:
            datei.write(f"{wert:.5f}\n")
    print(f"{len(daten)} Werte in '{dateiname}' gespeichert.")


def speichere_in_datenbank(daten, experiment, db_datei=DB_DATEI):
    with sqlite3.connect(db_datei) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS messwerte (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                experiment TEXT NOT NULL,
                wert REAL NOT NULL
            )
        """)
        conn.executemany(
            "INSERT INTO messwerte (experiment, wert) VALUES (?, ?)",
            [(experiment, float(wert)) for wert in daten],
        )
    print(f"{len(daten)} Werte unter Experiment '{experiment}' in '{db_datei}' gespeichert.")


# Drei korrelierte Normalverteilungen gleichzeitig erzeugen
daten = np.random.multivariate_normal(mittelwerte, kovarianz, anzahl)
data1, data2, data3 = daten[:, 0], daten[:, 1], daten[:, 2]

speichere_als_txt(data1, "data.txt")
speichere_als_txt(data2, "data2.txt")
speichere_als_txt(data3, "data3.txt")
# speichere_in_datenbank(data1, "versuch1")

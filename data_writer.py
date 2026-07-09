"""
Erzeugt synthetische, normalverteilte Messwerte und speichert sie entweder in einer TXT-Datei
oder direkt in der Datenbank aus webdatenbank.py (messwerte.db).
"""

import sqlite3

import numpy as np

# Parameter
anzahl = 100
mittelwert = 1
standardabweichung = 0.5

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


# Reine Normalverteilung erzeugen
daten = np.random.normal(mittelwert, standardabweichung, anzahl)

# Ziel wählen: die eine oder andere Zeile (aus)kommentieren
speichere_als_txt(daten, "data3.txt")
# speichere_in_datenbank(daten, "versuch1")

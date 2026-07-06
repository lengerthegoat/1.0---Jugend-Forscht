import numpy as np

# Parameter
anzahl = 1000
mittelwert = 0
standardabweichung = 1

# Reine Normalverteilung erzeugen
daten = np.random.normal(mittelwert, standardabweichung, anzahl)

# Speichern als TXT
with open("data.txt", "w") as datei:
    for wert in daten:
        datei.write(f"{wert:.5f}\n")

print("Normalverteilung gespeichert.")
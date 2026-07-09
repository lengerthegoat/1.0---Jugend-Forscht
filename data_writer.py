import numpy as np

# Parameter
anzahl = 100
mittelwert = 1
standardabweichung = 0.5

# Reine Normalverteilung erzeugen
daten = np.random.normal(mittelwert, standardabweichung, anzahl)

# Speichern als TXT
with open("data3.txt", "w") as datei:
    for wert in daten:
        datei.write(f"{wert:.5f}\n")

print("Normalverteilung gespeichert.")
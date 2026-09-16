import numpy as np
import pandas as pd
from matplotlib import pyplot
import random

data = pd.read_csv('experiment_daten.csv')

# Eingänge (X) und Ziel (y) trennen
X = data[['Strom_mA', 'Spannung_kV', 'Temperatur_C', 'Luftfeuchtigkeit_%', 'Diodenabstand_mm']]
y = data['Schub_mN']

# Normieren: jede Spalte hat danach Mittelwert 0 und Standardabweichung 1
X_mittelwert = X.mean()
X_std = X.std()
X_norm = (X - X_mittelwert) / X_std

y_mittelwert = y.mean()
y_std = y.std()
y_norm = (y - y_mittelwert) / y_std

# Als Listen, damit jede Zeile direkt an berechne_ausgangswert gegeben werden kann
eingaenge = X_norm.values.tolist()
ziele = y_norm.tolist()

print(X_norm.describe().loc[['mean', 'std']].round(3))
print(eingaenge[0], ziele[0])

class Neuron:
    def __init__(self, funktion, bias, anzahl_eingaenge=5):
        self.funktion = funktion
        self.bias = bias
        self.weights = []
        for i in range(anzahl_eingaenge):
            self.weights.append(random.uniform(-1, 1))
    def berechne_ausgangswert(self, nummern: list):
        summe = 0
        for weight in self.weights:
            for nummer in nummern:
                summe += nummer*self.weight

        summe += self.bias
        return self.funktion(summe)

    
def relu(x):
	return max(0.0, x)

layers = 2
neuronen_per_layer = 32



Netz = []

for i in range(layers):
     Neuronen = []
     for x in range(neuronen_per_layer):
          Neuronen.append(Neuron(funktion=relu,bias= 1))
     Netz.append(Neuronen)



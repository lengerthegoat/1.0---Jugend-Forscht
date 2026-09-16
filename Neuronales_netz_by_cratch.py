import numpy as np
import pandas as pd
from matplotlib import pyplot
import random

data = pd.read_csv('experiment_daten.csv')
print(type(data))
print(data.head())
print(data.ndim)
print(data.shape)

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

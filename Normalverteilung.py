import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

data = np.loadtxt("data.txt")


plt.hist(data, bins=30, density=True, alpha=0.5)


mu = np.mean(data)
sigma = np.std(data)


x = np.linspace(min(data), max(data), 200)
y = norm.pdf(x, mu, sigma)

plt.plot(x, y)

plt.xlabel("Wert")
plt.ylabel("Wahrscheinlichkeit")
plt.title("Normalverteilung")
plt.show()
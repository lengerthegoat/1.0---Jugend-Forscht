import numpy as np
import matplotlib.pyplot as plt


data1 = np.loadtxt("data.txt")
mu1 = np.mean(data1)
sigma1 = np.std(data1)
print("Mean and standard divietion data1")
print(str(mu1) + " " + str(sigma1))

data2 = np.loadtxt("data2.txt")
mu2 = np.mean(data2)
sigma2 = np.std(data2)
print("Mean and standard divietion data2")
print(str(mu2) + " " + str(sigma2))


data = np.stack([data1, data2])



plt.hist(data, bins=30, density=True, alpha=0.5)
plt.hist(data2, bins=30, density=True, alpha=0.5)

plt.xlabel("Wert")
plt.ylabel("Wahrscheinlichkeit")
plt.title("Normalverteilung")
plt.show()

print(np.cov(data))
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("../data.txt")

print(data)

plt.hist(data, bins=100)
plt.show()
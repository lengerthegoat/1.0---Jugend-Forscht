import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.txt")

plt.hist(data, bins=30)
plt.show()
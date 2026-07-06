import numpy as np
import matplotlib.pyplot as plt
data_1 = []

with open("data.txt") as f:
  indice = 0
  for x in f:
    number  = x.split(" ")
    number = number[1].replace("\n","")
    number = int(number)
    data_1.append(number)
    indice =+ 1

data_1 = np.array(data_1)
print(data_1)
data_2 = [[],[]]
for x in range(19):
  y = x+2
  data_2[0].append(y)
  tuple1 = np.where(data_1 == y)
  data_2[1].append(len(tuple1[0]))

data_2 = np.array(data_2)
print(data_2)

plt.plot(data_2[0],data_2[1])
plt.show()

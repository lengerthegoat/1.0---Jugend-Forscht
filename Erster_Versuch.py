import numpy as np
import matplotlib.pyplot as plt
data_1 = []

with open("data.txt") as f:
  
  for x in f:
    number  = x
    
    number = float(number)
    data_1.append(number)
    

data_1 = np.array(data_1)
print(data_1)
data_2 = [[],[]]
for x in range(19):
  y = x
  data_2[0].append(y)
  tuple1 = np.where(data_1 == y)
  data_2[1].append(float(len(tuple1[0])))

data_2 = np.array(data_2)
print(data_2)

plt.plot(data_2[0],data_2[1])
plt.show()

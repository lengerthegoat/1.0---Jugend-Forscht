import random
import os

if os.path.exists("data.txt"):
  os.remove("data.txt")
f = open("data.txt", "x")


with open("data.txt", "a") as f:
  for i in range(100000):
    wuerfel_1 = random.randint(1,10)
    wuerfel_2 = random.randint(1,10)
    total_score = wuerfel_1 + wuerfel_2
    f.write(str(i) + " " + str(total_score) + "\n" )
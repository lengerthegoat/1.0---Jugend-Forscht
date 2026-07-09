import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

data1 = np.loadtxt("data.txt")
mu1 = np.mean(data1)
sigma1 = np.std(data1)
print(f"data1: Mittelwert = {mu1:.3f}, Standardabweichung = {sigma1:.3f}")

data2 = np.loadtxt("data2.txt")
mu2 = np.mean(data2)
sigma2 = np.std(data2)
print(f"data2: Mittelwert = {mu2:.3f}, Standardabweichung = {sigma2:.3f}")

data3 = np.loadtxt("data3.txt")
mu3 = np.mean(data3)
sigma3 = np.std(data3)
print(f"data3: Mittelwert = {mu3:.3f}, Standardabweichung = {sigma3:.3f}")


data = np.stack([data1, data2, data3])



plt.hist(data1, bins=30, density=True, alpha=0.5)
plt.hist(data2, bins=30, density=True, alpha=0.5)
plt.hist(data3, bins=30, density=True, alpha=0.5)


plt.xlabel("Wert")
plt.ylabel("Wahrscheinlichkeit")
plt.title("Normalverteilung")
plt.show()

print("Kovarianzmatrix:")
print(np.round(np.cov(data), 3))

fig = go.Figure(data=[go.Scatter3d(
    x=data1, y=data2, z=data3,
    mode='markers',
    marker=dict(
        size=4,
        color=data3,                # Färbe die Punkte basierend auf der z-Achse
        colorscale='Viridis',   # Farbskala (z.B. Viridis, Plasma)
        opacity=0.8
    )
)])

# 3. Layout anpassen
fig.update_layout(
    title='Interaktive 3D-Gauß-Wolke',
    scene=dict(
        xaxis_title='X-Achse',
        yaxis_title='Y-Achse',
        zaxis_title='Z-Achse'
    )
)

fig.show()

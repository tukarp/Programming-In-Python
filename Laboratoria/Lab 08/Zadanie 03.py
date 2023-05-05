# Importowanie bibliotek
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


# Funkcja animująca punkty na wykresie
def anima(frame):
    y[:-1] = y[1:]
    y[-1] = np.sin(2 * np.pi * frame / 100)
    scat.set_data([x, y])


# Zaadresowanie zmiennych
fig, ax = plt.subplots()  # Wykresy
x = np.linspace(0, 2 * np.pi, 100)  # Wartości X
y = np.sin(x)  # Wartości Y

# Wykres
scat = ax.plot(x, y)[0]

# Animowanie wykresu
animation = FuncAnimation(fig, anima, frames=100, interval=50)

# Wyświetlenie wykresu
plt.show()

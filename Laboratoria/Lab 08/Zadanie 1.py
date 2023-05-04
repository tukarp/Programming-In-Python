# Importowanie bibliotek
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


# Funkcja animująca punkty na wykresie
def anima(frame):
    x = frame
    y = 0
    point.set_data([x], [y])
    return point


# Zaadresowanie zmiennych
fig, ax = plt.subplots()  # Wykresy
ax.set_xlim(-10, 10)  # Oś x
ax.set_ylim(-10, 10)  # Oś y
point = ax.plot([], [], "ro")[0]  # Punkt

# Animowanie wykresu
animation = FuncAnimation(fig, anima, frames=np.arange(-10, 10, 0.1), interval=20)

# Wyświetlenie wykresu
plt.show()

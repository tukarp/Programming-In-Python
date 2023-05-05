# Importowanie bibliotek
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


# Funkcja ustawiająca wartości startowe
def init():
    ax.set_xlim(0, np.pi * 2)
    ax.set_ylim(-1.5, 1.5)


# Funkcja animująca punkty na wykresie
def anima(frame):
    x = frame
    y = np.sin(frame)
    scat.set_offsets([x, y])


# Zaadresowanie zmiennych
x = 0  # Punkt X
y = 0  # Punkt Y
fig, ax = plt.subplots()  # Wykresy
scat = ax.scatter(x, y)  # Wykres punktowy

# Animowanie wykresu
animation = FuncAnimation(fig, anima, frames=np.linspace(0, 2 * np.pi, 100), init_func=init, interval=50)

# Wyświetlenie wykresu
plt.show()

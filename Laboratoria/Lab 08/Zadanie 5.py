# Importowanie bibliotek
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


# Funkcja animująca punkty na wykresie
# poprzez obliczanie ich następnych wartości
def anim(frame, X, Y, Z):
    Z = np.sin(X + np.sin(frame / 10)) * \
        np.cos(Y - np.sin(frame / 20)) + \
        np.sin(X + Y) * np.cos(frame / 10)

    mat.set_data(Z)
    return mat


# Zaadresowanie zmiennych
grid_size = 100  # Wielkość wykresu
linear_space = np.linspace(-np.pi / 2, np.pi / 2, grid_size)  # Przestrzeń liniowa
X, Y = np.meshgrid(linear_space, linear_space)  # Utworzenie siatek przestrzeni liniowej

# Utworzenie zmiennej przechowującej wartości wykresu
Z = np.sin(X) * np.cos(Y)

# Utworzenie wykresów
fig, ax = plt.subplots()

# Wyświetlenie macierzy wartości wykresu
mat = ax.matshow(Z, cmap="jet")

# Animowanie wykresu
anim = FuncAnimation(fig, anim, frames=200, fargs=(X, Y, Z), interval=5)

# Wyświetlenie wykresu
plt.show()

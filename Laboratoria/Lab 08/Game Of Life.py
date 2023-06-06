# Importowanie bibliotek
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


# Funkcja animująca punkty na wykresie
# poprzez obliczanie ich następnych wartości
# za pomocą algorytmu "Game of Life"
def anim(frame):
    # Ustawienie globalnej zmiennej Z
    global Z
    # Skopiowanie Z do Z_new
    Z_new = Z.copy()
    for i in range(size):
        for j in range(size):
            # Obliczenie sumy wartości sąsiednich komórek
            neighbours = Z[i - 1:i + 2, j - 1:j + 2].sum() - Z[i, j]
            # Jeśli komórka istnieje
            if Z[i, j] == 1:
                # Jeśli ilość sąsiadów jest mniejsza od 2 lub większa od 3
                if (neighbours < 2) or (neighbours > 3):
                    # Komórka umiera
                    Z_new[i, j] = 0
                # W przeciwnym wypadku
                else:
                    # Komórka zostaje
                    Z_new[i, j] = 1

            # Jeśli komórka nie istnieje
            else:
                # Jeśli ilość sąsiadów jest równa 3
                if neighbours == 3:
                    # Komórka się rodzi
                    Z_new[i, j] = 1
                # W przeciwnym wypadku
                else:
                    # Komórka się nie rodzi
                    Z_new[i, j] = 0
    # Ustaw wartość macierzy
    mat.set_data(Z_new)
    # Ustaw wartość Z
    Z = Z_new
    # Zwróć macierz
    return mat


# Zaadresowanie zmiennych
size = 100  # Wielkość wykresu
Z = np.random.rand(size, size)  # Utworzenie macierzy losowych punktów

# Ustawienie losowych punktów w macierzy Z tylko i wyłącznie na 0 lub 1
Z[Z >= 0.5] = 1
Z[Z < 0.5]  = 0

# Utworzenie wykresów
fig, ax = plt.subplots()

# Wyświetlenie macierzy wartości wykresu z określoną mapą kolorów
mat = ax.matshow(Z, cmap="plasma")

# Animowanie wykresu
anim = FuncAnimation(fig, anim, frames=1000, interval=10)

# Wyświetlenie wykresu
plt.show()

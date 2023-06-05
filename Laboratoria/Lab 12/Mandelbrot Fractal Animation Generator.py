# Importowanie bibliotek
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


# Funkcja animująca punkty na wykresie
def animate_points(frame):
    global z  # Ustawienie z jako zmiennej globalnej
    result[np.abs(z) > 2] = frame  # Ustawianie wartości w tablicy wynikowej dla punktów spełniających warunek
    z = (result == 255) * (z ** 2 + z0)  # Obliczanie kolejnych wartości z dla animacji
    plot.set_array(result)  # Aktualizacja klatki animacji na wykresie


# Ustawienie zmiennych
# Utworzenie przestrzeni liniowych x i y
x = np.arange (-2,   1,   .01)  # Przestrzeń liniowa dla osi x
y = np.arange (-1.5, 1.5, .01)  # Przestrzeń liniowa dla osi y

# Generowanie przestrzeni punktów x i y
x, y = np.meshgrid(x, y)

# Generowanie siatki
z = x + 1j * y

# Ustawienie kształtu wykresu
shape = z.shape

# Utworzenie figury
fig = plt.figure(figsize=(12, 9))

# Utworzenie kopii siatki do generowania kolejnych klatek animacji
z0 = np.copy(z)

# Utworzenie tablicy wynikowej
result = np.ones(shape) * 255

# Utworzenie wykresu
plot = plt.imshow(result, vmin=0, vmax=255, cmap="jet")

# Animowanie wykresu
animation = FuncAnimation(fig, animate_points, frames=256, interval=40, repeat=False)

# Wyświetlenie wykresu
plt.show()
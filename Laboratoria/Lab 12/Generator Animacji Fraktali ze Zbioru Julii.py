# Importowanie bibliotek
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


# Funkcja animująca punkty fraktali ze zbioru Julii na wykresie
def animate_fractal(frame):
    global z  # Ustawienie z jako zmiennej globalnej
    result[np.abs(z) > 2] = frame  # Ustawianie wartości w tablicy wynikowej dla punktów spoza zbioru
    z = z ** 2 + c  # Obliczanie kolejnych wartości z dla zbioru Julii
    plot.set_array(result)  # Aktualizacja klatki animacji na wykresie


# Ustawienie parametru c dla zbioru Julii
c = -0.7 + 0.27015j

# Utworzenie przestrzeni liniowych x i y
x = np.linspace(-2, 2, 800)  # Przestrzeń liniowa dla osi x
y = np.linspace(-2, 2, 800)  # Przestrzeń liniowa dla osi y

# Generowanie przestrzeni punktów x i y
x, y = np.meshgrid(x, y)

# Generowanie siatki z punktami zespolonymi
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
animation = FuncAnimation(fig, animate_fractal, frames=256, interval=40, repeat=False)

# Wyświetlenie wykresu
plt.show()

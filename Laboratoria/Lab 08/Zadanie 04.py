# Importowanie bibliotek
import matplotlib.pyplot as plt
import numpy as np

# Zaadresowanie zmiennych
n = 100  # Wielkość wykresu
linear_space = np.linspace(0, n, n)  # Przestrzeń liniowa wykresu
X, Y = np.meshgrid(linear_space, linear_space)  # Stworzenie siatki na podstawie przestrzeni liniowej wykresu
Z = (100 ** 2 - ((50 - X) ** 2 + (Y - 50) ** 2))  # Obliczenie wartości dla podanych wartości ze wzoru

# Wyświetlenie wykresu
plt.matshow(Z)
plt.show()

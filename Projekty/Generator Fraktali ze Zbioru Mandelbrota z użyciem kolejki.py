# Importowanie bibliotek
from multiprocessing import Process
from multiprocessing import Queue
import matplotlib.pyplot as plt
from time import time
import numpy as np


# Funkcja generująca fraktale Mandelbrota
def mandelbrot(z, a, queue):
    timer = time()  # Pomiar czasu wykonania funkcji
    z0 = np.copy(z)  # Skopiowanie tablicy z
    shape = z.shape  # Rozmiar tablicy z
    result = 255 * np.ones(shape)  # Utworzenie tablicy wynikowej
    for i in range(255):  # Iteracja po liczbie iteracji
        mask = np.abs(z) <= 2  # Utworzenie maski
        z[mask] = z[mask] ** 2 + z0[mask]  # Obliczenie wartości zespolonych z
        result[~mask] = i  # Zapisanie wyników do tablicy wynikowej
    print("Function: ", time() - timer)  # Wyświetlenie pomiaru czasu
    queue.put((a, result))  # Zapisanie wyników do kolejki


# Funkcja main
if __name__ == '__main__':
    # Zaalokowanie zmiennych
    x = np.arange(-2, 1, 0.02)  # Zmienna tablicowa x
    y = np.arange(-1.5, 1.5, 0.02)  # Zmienna tablicowa y
    x, y = np.meshgrid(x, y)  # Utworzenie siatki zmiennych x i y

    # Utworzenie tablicy z wartościami zespolonymi
    z = x + 1j*y  # Obliczenie wartości zespolonych z
    shape = z.shape  # Rozmiar tablicy z

    # Utworzenie kolejki i procesów
    queue = Queue()  # Utworzenie kolejki
    n = 4  # Utworzenie liczby procesów
    l = [z[:, i * shape[1] // n : (i + 1) * shape[1] // n] for i in range(n)]  # Podział tablicy z na n części
    processes = [Process(target=mandelbrot, args=(l[i], i, queue)) for i in range(n)]  # Utworzenie procesów

    # Pomiar czasu wykonania programu
    timer = time()  # Pomiar czasu wykonania programu
    for process in processes:  # Iteracja po procesach
        process.start()  # Uruchomienie procesu

    # Wyświetlenie pomiaru czasu
    print("Program: ", time() - timer)

    # Zapisanie wyników do tablicy
    result = sorted([queue.get() for _ in range(n)], key=lambda x: x[0])  # Pobranie wyników z kolejki
    result = [x[1] for x in result]  # Pobranie wyników z tablicy
    result = np.hstack(result)

    # Wyświetlenie wykresu
    fig, ax = plt.subplots()  # Utworzenie podwykresu
    ax.matshow(result)  # Wyświetlenie macierzy wynikowej

    # Wyświetlenie wykresu
    plt.show()

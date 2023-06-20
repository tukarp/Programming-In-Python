# Rozwiązanie
# Importowanie biblioteki
import random


# Wprowadzenie danych
rule = int("01011010", 2)   # Reguła
n = 80                      # Długość ciągu
k = 30                      # Liczba kroków

# Utworzenie słownika do zastosowania podanej reguły
chars = ["*", "_"]  # Utworzenie listy znaków
predict = ["***", "**_", "*_*", "*__", "_**", "_*_", "__*", "___"]  # Utworzenie listy predykatów
prerule = ["_" * int(i=='0') + "*" * int(i=='1') for i in str(bin(rule))[2:].zfill(8)]  ## Utworzenie listy zasad początkowych
automat = {key: value for (key, value) in zip(predict, prerule)}  # Utworzenie automatu łączącego wartości

# Wyświetlenie wprowadzonych danych
print(f"Reguła: {rule}")
print(f"Dlugosc ciagu: {n}")
print(f"Liczba Kroków: {k}")

# Zaalokowanie zmiennych
current_value = ""
result = ""

# Wylosowanie znaków
for i in range(n):
    # Dodaj do wyniku losowy znak
    result += random.choice(chars)

# Ustawienie result w środku
result = 39 * '_' + '*' + 40 * '_'

# Pętla automatu
for i in range(k):
    # Obecna wartość
    current_value = ""
    
    # Obliczanie wartości automatu
    current_value += automat["".join([result[-1], result[0], result[1]])]
    for i in range(1, n - 1):
        current_value += automat[result[i - 1:i + 2]]
    current_value += automat["".join([result[-2], result[-1], result[0]])]
    
    # Przypisanie wartości do wyniku
    result = current_value

    # Wyświetlenie wyniku
    print(result)

# Importowanie biblioteki
import time


# Funkcja porównująca sekwencje DNA
def dna_sequences_comparer(primer1, primer2):
    # Jeżeli któraś z sekwencji nie istnieje lub jest pusta
    if not primer1 or not primer2:
        # Zwróć -1
        return -1
    # Jeżeli sekwencje istnieją i nie są puste
    else:
        # Utworzenie potrzebnych zmiennych
        primer2 = primer2[::-1]  # Odwrócenie sekwencji primer2
        primers1_list = '*' * (len(primer1 + primer2) - 2) + primer1  # Utworzenie listy pierwszej sekwencji DNA
        primers2_list = '*' * (len(primer1) - 1) + primer2  # Utworzenie listy drugiej sekwencji DNA
        align = []  # Utworzenie listy align przechowującej liczbę wystąpień par DNA
        for i in range(len(primer1 + primer2) - 1):  # Dla każdego elementu z zakresu od 0 do długości sumy obu sekwencji
            common = list(zip(primers1_list[i:], primers2_list))  # Utworzenie listy common przechowującej wylistowane i złączone pary DNA
            align.append(  # Dodanie do listy align liczby wystąpień par DNA
                common.count(("A", "T")) + common.count(("T", "A")) +  # Liczba wystąpień par A-T i T-A
                common.count(("C", "G")) + common.count(("G", "C"))    # Liczba wystąpień par C-G i G-C
            )
        # Zwrócenie maksymalnej liczby wystąpień par DNA
        return max(align)


# Funkcja main
if __name__ == '__main__':
    # Zainicjaliowanie zmiennych
    file_input = open("primers.txt", 'r')  # Utworzenie zmiennej odczytującej plik primers
    dna_sequences_sum = 0  # Utworzenie zmiennej przechowującej sumę wystąpień par sekwencji DNA
    dna_sequences = []  # Utworzenie listy przechowującej sekwencje DNA

    # Wyświetlenie komunikatu o rozpoczęciu skanowania
    print("Skanowanie...")

    # Dla każdej linii w pliku
    for line in file_input:
        # Dodanie do listy sekwencji DNA pierwszego elementu z linii
        dna_sequences.append(line.split(",")[0])
    # Zamknięcie pliku
    file_input.close()
    # Zliczenie elementów w liście sekwencji DNA
    count = len(dna_sequences)

    # Utworzenie licznika czasu
    start_time = time.time()
    # Utworzenie zmiennej i przypisanie do niej pierwszego elementu z listy sekwencji DNA
    primer_1 = dna_sequences[0]
    # Dla każdego elementu z listy sekwencji DNA
    for i in range(count):
        # Utworzenie zmiennej i przypisanie do niej kolejnych elementów z listy sekwencji dna
        primer_2 = dna_sequences[i]
        # Zsumowanie liczb wystąpień par sekwencji DNA
        dna_sequences_sum += dna_sequences_comparer(primer_1, primer_2)
    # Zakończenie licznika czasu
    end_time = time.time()

    # Wyświetlenie czasu wykonania programu
    print(f"Czas wykonania programu: {end_time - start_time} sekundy")

    # Wyświetlenie sumy liczb wystąpień par DNA
    print(f"Suma liczb wystąpień par DNA: {dna_sequences_sum}")

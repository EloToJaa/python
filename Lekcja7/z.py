import random

MIN = 1
MAX = 1000

wylosowana_liczba = random.randint(MIN, MAX)

wpisana_liczba = None
liczba_prob = 0

print(f"Witaj w grze! Została wylosowana liczba z zakresu {MIN} - {MAX}")

while wpisana_liczba != wylosowana_liczba:
    wpisana_liczba = int(input("Podaj liczbę: "))

    if wpisana_liczba < wylosowana_liczba:
        print("Liczba jest za mała")
    elif wpisana_liczba > wylosowana_liczba:
        print("Liczba jest za duża")
    
    liczba_prob += 1

print("Gratualcje! Udało ci się odgadnąć wylosowaną liczbę!")
print(f"Wylosowana liczba: {wylosowana_liczba}")
print(f"Ilość prób: {liczba_prob}")
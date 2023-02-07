liczba = int(input())

if liczba % 3 == 0 or liczba % 10 == 0 or liczba % 77 == 0:
    print("Podana liczba jest podzielna przez 3, 10 lub 77")
elif liczba % 3 == 0 and liczba % 10 == 0 and liczba % 77 == 0:
    print("Podana liczba jest podzielna przez 3, 10 i 77")
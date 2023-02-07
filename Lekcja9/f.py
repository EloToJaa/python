liczby = []

for i in range(10):
    a = int(input("Podaj liczbę: "))

    if a in liczby:
        print("Wprowadzono już taką liczbę")
    else:
        liczby.append(a)

print(liczby)
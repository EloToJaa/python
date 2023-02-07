suma = 0

while True:
    wprowadzona_liczba = input()

    if wprowadzona_liczba == "koniec":
        break

    suma += int(wprowadzona_liczba)

print(f"Suma wszystkich podanych liczb wynosi: {suma}")
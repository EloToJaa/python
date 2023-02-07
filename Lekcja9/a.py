oceny = []

while True:
    wprowadzony_tekst = input()

    if wprowadzony_tekst == 'q':
        break

    ocena = int(wprowadzony_tekst)

    oceny.append(ocena)

print(oceny)

srednia = sum(oceny) / len(oceny)
print(f"Średnia ocen wynosi: {srednia}")
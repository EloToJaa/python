szerokosc = int(input("Podaj szerokość: "))
wysokosc = int(input("Podaj wysokość: "))

for i in range(wysokosc):
    print("*" * szerokosc)

print()

for i in range(wysokosc):
    if i == 0 or i == wysokosc - 1:
        print("*" * szerokosc)
    else:
        print("*" + " " * (szerokosc - 2) + "*")
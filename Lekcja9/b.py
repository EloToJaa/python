liczba_elementow = int(input("Podaj liczbę elementów: "))
elementy = []

for i in range(liczba_elementow):
    element = input(f"Podaj element numer {i}: ")
    elementy.append(element)

for ele in elementy:
    print(ele)


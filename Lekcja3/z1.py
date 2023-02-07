imie = input('Podaj imię: ')
nazwisko = input('Podaj nazwisko: ')
rok_urodzenia = int(input('Podaj rok urodzenia: '))
wiek = 2022 - rok_urodzenia

tekst = f'{imie} {nazwisko} ma rocznikowo {wiek} lat'
print(tekst)
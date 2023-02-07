miesiac = int(input('Podaj numer miesiąca (1-12): '))

cena = -1

if miesiac == 1 or miesiac == 2:
    cena = 150
elif miesiac == 3 or miesiac == 4 or miesiac == 11 or miesiac == 12:
    cena = 199
elif miesiac == 5 or miesiac == 6 or miesiac == 10:
    cena = 249
elif miesiac == 7 or miesiac == 8 or miesiac == 9:
    cena = 299

if cena == -1:
    print("Podałeś zły miesiąc")
else:
    print(f"Cena wynosi: {cena}")
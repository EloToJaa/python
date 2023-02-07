wygrane = int(input('Podaj liczbę wygranych: '))
przegrane = int(input('Podaj liczbę przegranych: '))
mvp = int(input('Podaj liczbę odznaczeń MVP: '))

if wygrane >= 10 and (wygrane > przegrane or mvp >= 7):
    print("Gratulę przejścia do następnej fazy turnieju!")
else:
    print('Niestety nie udało ci się przejść dalej ;(')
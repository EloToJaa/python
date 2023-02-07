WZROST_MINIMALNY = 150
WZROST_MAKSYMALNY = 215

print('Sprawdź czy masz odpowiedni wzrost, aby pskorzystać z wagonika')
wzrost = float(input('Podaj swój wzrost w cm: '))

warunek = wzrost >= WZROST_MINIMALNY and wzrost <= WZROST_MAKSYMALNY
print(warunek)
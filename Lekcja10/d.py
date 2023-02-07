import math

def pole_szesciokata_foremnego(a):
    return 3 * a ** 2 * math.sqrt(3) / 2

def objetosc_graniastoslupa(podstawa, wysokosc):
    return wysokosc * pole_szesciokata_foremnego(podstawa)

x = int(input())
pole = pole_szesciokata_foremnego(x)
print(pole)
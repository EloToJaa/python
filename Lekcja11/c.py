from math import sqrt

def prostokat(a: float, b: float) -> float:
    obwod = 2 * a + 2 * b
    pole = a * b
    przekatna = sqrt(a**2 + b**2)

    return obwod, pole, przekatna

a, b, c = prostokat(3.11, 4.23)
print(f'Obwód = {a}, Pole = {b}, Przekątna = {c}')
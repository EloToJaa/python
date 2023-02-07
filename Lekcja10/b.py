import math

def pole_prostokata(a, b):
    pole = a * b
    print(f"Pole prostokąta o bokach {a}x{b} = {pole}")

def pole_kola(r):
    pole = math.pi * r * r
    print(f"Pole koła o promeniu {r} = {pole}")

pole_prostokata(3, 4)
pole_prostokata(5, 2)
pole_prostokata(10, 3)

pole_kola(12)
pole_kola(4)
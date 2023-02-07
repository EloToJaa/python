def oblicz_wysokosc(proporcje_szerokosc, proporcje_wyskosc, piksele_szerokosc):
    return piksele_szerokosc / proporcje_szerokosc * proporcje_wyskosc

print(oblicz_wysokosc(16, 9, 1280))
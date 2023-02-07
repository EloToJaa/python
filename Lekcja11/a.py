# polacz(‘?’, [‘ala’, ‘ma’, ‘kota’]) -> ‘ala?ma?kota’

def polacz(lacznik, slowa):
    nowe_slowo = slowa[0]

    for slowo in slowa[1:]:
        nowe_slowo += lacznik
        nowe_slowo += slowo
    
    return nowe_slowo

print(polacz('!!', ['ala', 'ma', 'kota', 'test']))
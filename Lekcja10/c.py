import time

def pasek_ladowania(gotowe, wszystko=100, znaki=10):
    wykonane = round(znaki * gotowe / wszystko)
    niewykonane = znaki - wykonane

    tekst_wykonane = '#' * wykonane
    tekst_niewykonane = '-' * niewykonane

    print(f"\r[{tekst_wykonane}{tekst_niewykonane}]", end=' ')

for i in range(101):
    pasek_ladowania(100, znaki=100)
    time.sleep(0.1)
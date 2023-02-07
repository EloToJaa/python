liczba = int(input("Podaj liczbę: "))
for a in range(liczba):
    print(f"a = {a}")
    if a > 4:
        break
else:
    print("Pętla wykonała się bez instrukcji break")
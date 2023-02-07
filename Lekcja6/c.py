wyraz = input("Podaj testowany wyraz: ")

print(type(wyraz))

if "a" in wyraz or "d" in wyraz or "as" in wyraz or "test" in wyraz:
    print("Znalazłem odpowiedni znak")
else:
    print("Nie znalazłem odpowiedniego znaku")
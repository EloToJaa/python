print("Cześć, jestem Python\nA Ty jak masz imię?")
imie = input()
print(f"Cześć {imie} miło Cię poznać")

print("Ja w powstałem w 1991 roku, dzięki pracy programisty Guido von Rossuma")
rok_urodzenia = input("A kiedy ty się urodziłeś? ")
wiek = 2022 - int(rok_urodzenia)
print(f'Wow to już masz {wiek} lat')

kolor = input("Jaki jest Twój ulubiony kolory? ")
print(f"Moim ulubionym kolorem jest {kolor}")

print("Z jakiego miasta pochodzisz? ", end='')
miasto = input()
print(f"Jesteś z {miasto}")

print(f"Witaj {imie}, urodziłeś się w {rok_urodzenia} roku i masz {wiek} lat.\nTwój ulubiony kolor to {kolor}.\nMieszkasz w {miasto}.")
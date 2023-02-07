PIN = "1234"
ROK_URODZENIA = 1998
HASLO = "qwerty"

while True:
    pin = input("PIN: ")
    if pin != PIN:
        print("Niepoprawny PIN")
        continue

    rok_urodzenia = int(input("Rok urodzenia: "))
    if rok_urodzenia != ROK_URODZENIA:
        print("Niepoprawny rok urodzenia")
        continue

    haslo = input("Hasło: ")
    if haslo != HASLO:
        print("Niepoprawne hasło")
        continue

    print("Zalogowano poprawnie")
    break

print("Odpalił się tajny kod")
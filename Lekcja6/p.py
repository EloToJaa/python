from getpass import getpass

wprowadzone_haslo = getpass("Podaj hasło: ")
poprawne_haslo = "Haslo123"

if wprowadzone_haslo == poprawne_haslo:
    print("Wprowadziłeś poprawne hasło")
else:
    print("Wprowadziłeś niepoprawne hasło")
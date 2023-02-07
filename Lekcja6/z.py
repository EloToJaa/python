from getpass import getpass

login = input("Login: ")
haslo = getpass("Hasło: ")

POPRAWNY_LOGIN = "Gigant"
POPRAWNE_HASLO = "qwerty"

if login == POPRAWNY_LOGIN and haslo == POPRAWNE_HASLO:
    print("Poprawne logowanie")
    
else:
    print("Niepoprawne logowanie")
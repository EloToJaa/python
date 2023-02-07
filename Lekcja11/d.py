def komunikat(imie: str, wiek: int, wzrost: float) -> str:
    return f"{imie}, {wiek}, {wzrost:.3f}"

print(komunikat("Tomek", 22, 1.8764))
print(komunikat("Kuba", 16, 1.7654))
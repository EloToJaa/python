liczba = int(input())
if liczba < 0:
    print("Liczba ujemna")
    exit(1)

if liczba == 0 or liczba == 1:
    print(liczba)
    exit(0)

a = 0
b = 1

for i in range(liczba - 1):
    c = a + b
    a, b = b, c

print(c)

a = float(input())
b = float(input())
c = float(input())

# a + b > c and a + c > b and b + c > a

max_bok = max(a, b, c)
min_bok = min(a, b, c)
obwod = a + b + c
sredni_bok = obwod - max_bok - min_bok

if not (max_bok < sredni_bok + min_bok and a > 0 and b > 0 and c > 0):
    print("Podane boki nie utworzą trójkąta")
    exit()

print("Taki trójkąt istnieje")
print(f"Najdłuższy bok trójkąta: {max_bok}")
print(f"Najkrótszy bok trójkąta: {min_bok}")
print(f"Obwód trójkąta: {obwod}")

if a == b == c:
    print("Trójkąt równoboczny")
elif a == b or b == c or a == c:
    print("Trójkąt równoramienny")
else:
    print("Trójkąt różnoboczny")

max_bok_kwadrat = max_bok ** 2
suma_kwadratow = min_bok ** 2 + sredni_bok ** 2

if max_bok_kwadrat == suma_kwadratow:
    print("Trójkąt prostokątny")
elif max_bok_kwadrat > suma_kwadratow:
    print("Trójkąt rozwartokątny")
else:
    print("Trójkąt ostrokątny")


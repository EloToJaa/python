import time

liczba = int(input())

while liczba > 0:
    print(f"Pozostało {liczba} sekund", end='\r')
    time.sleep(2)
    liczba -= 1

print("\nCzas się skończył!")
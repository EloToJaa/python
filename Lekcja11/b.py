def fib(n):
    if n < 1:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    ciag = [0, 1]
    for i in range(n - 2):
        ciag.append(ciag[-1] + ciag[-2])
    
    return ciag

# fib(5) [0, 1, 1, 2, 3]

print(fib(1))
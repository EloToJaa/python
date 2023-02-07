def usun_duplikaty(lista: list[float]) -> list[float]:
    bez_duplikatow = []

    for liczba in lista:
        if liczba not in bez_duplikatow:
            bez_duplikatow.append(liczba)
    
    return bez_duplikatow
    

print(usun_duplikaty([1,2,3,3,3,3,4,5]))
wiek_rocznikowo = int(input("Podaj wiek: "))

for i in range(wiek_rocznikowo + 1):
    rok_kalendarzowy = 2022 - wiek_rocznikowo + i
    print(f"W roku {rok_kalendarzowy} miałeś {i} lat")
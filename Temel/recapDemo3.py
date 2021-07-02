number = int(input("Sayı giriniz: "))
asalMi = True

for i in range(2,number):
    if number%i == 0:
        asalMi = False
        break

if asalMi == True:
    print("Sayı Asal")
else:
    print("Sayı Asal Değil")

    
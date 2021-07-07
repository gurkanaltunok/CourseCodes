number , asalMi = int(input("Sayı giriniz: ")), True
for i in range(2,number):
    if number%i == 0: asalMi = False, print(str(number)+" sayısı Asal Değil, " + str(i) +" sayısına bölünüyor.") ; break
if asalMi == True: print(str(number)+" Sayı Asal")
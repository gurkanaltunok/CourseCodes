number = int(input("Sayı Giriniz: "))

carpim = 1

i = 1

while i <= number:
    carpim = carpim*i
    i = i+1

if number < 0:
    print("Negatif sayıların faktöriyeli hesaplanamaz")

elif number >= 0:
    print(carpim)




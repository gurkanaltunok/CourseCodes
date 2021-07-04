print("1 : Topla")
print("2 : Çıkar")
print("3 : Çarp")
print("4 : Böl")

def Topla(x,y):
    return x+y

def Cikar(x,y):
    return x-y

def Carp(x,y):
    return x*y

def Bol(x,y):
    return x/y

operationNumber = int(input("Operasyon Numarası: "))

isNumberCorrect = True

if operationNumber <= 0:
    isNumberCorrect = False
    print("Hatalı Operasyon Kodu Girdiniz.")
elif operationNumber >=5:
    isNumberCorrect = False
    print("Hatalı Operasyon Kodu Girdiniz.")
else:
    x = int(input("Sayı 1: "))
    y = int(input("Sayı 2: "))

    if operationNumber == 1:
        print("Sonuç = ",Topla(x,y))
    elif operationNumber == 2:
        print("Sonuç = ",Cikar(x,y))
    elif operationNumber == 3:
        print("Sonuç = ",Carp(x,y))
    else:
        print("Sonuç = ",Bol(x,y))

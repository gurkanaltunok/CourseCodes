# -*- coding: utf-8 -*-
#%% For sum
sayilar = [1,4,67,32,24,35,75,34,62,95,37]
toplam = 0
for sayi in sayilar:
    toplam = toplam + sayi
    
print(toplam)


sehirler = ["Ankara","İstanbul","İzmir"]

#%% For intro
for sehir in sehirler:
    if sehir == "Ankara":
        continue
    print(sehir + " için kod = " + sehir[0:3].upper())
    print("********")
    
#%% For range

for x in range(80,100,2):
    print(x+1)
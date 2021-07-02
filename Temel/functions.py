#%%
sehir = "Ankara"

sehir.upper()
print(sehir.endswith("e"))
#%%
def selamVer(name = "Ziyaretçi"):
    print("Merhaba ", name )

selamVer("Gürkan")
selamVer("Ahmet")
selamVer("Mehmet")
selamVer()

def selamVer2(name = "Ziyaretçi", surname = "Kullanıcı"):
    print("Merhaba " + name + " " + surname)

selamVer2()
selamVer2("Gürkan")
selamVer2("Gürkan","Altunok")

def dikUcgenAlaniHesapla(a,b):
    return a*b/2

alan = dikUcgenAlaniHesapla(5,6)
print(alan)

dikUcgenAlaniHesapla2 = lambda a,b : a*b/2

print(dikUcgenAlaniHesapla2(10,8))

print(type(dikUcgenAlaniHesapla))
print(type(dikUcgenAlaniHesapla2))

x = dikUcgenAlaniHesapla2
print(x(9,10))

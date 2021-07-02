# sehir = "Ankara"

# print(sehir.upper())
# print(sehir.endswith("e"))

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


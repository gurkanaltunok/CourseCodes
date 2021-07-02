sozluk = {
    "book" : "kitap",
    "table" : "masa"
    }

sozluk2 = dict(kitap = "book", masa = "table")

sozluk["book"] = "kitap 1"
sozluk["pencil"] = "kalem"
print(sozluk["book"])
print(sozluk)

del(sozluk["book"])
print(sozluk)
print(len(sozluk))

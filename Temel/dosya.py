# r Read, a Append, w Write, x Create

f = open("musteriler.txt")
# print(f.read())
print("**************")

print(f.readline())

for l in f:
    print(l)

f.close()

fileToAppend = open("ogrenciler.txt","w")
fileToAppend.write("\n")
fileToAppend.write("Ahmet")
fileToAppend.close()


import os

if os.path.exists("ogrenciler.txt"):
    os.remove("ogrenciler.txt")
else:
    print("Dosya Yok")

os.rmdir("empty") #deletes folder
studentsSet = {"Gürkan","Oğuz","Engin","Ahmet"}
print(studentsSet)

for student in studentsSet:
    print(student)
    
print("Gürkan" in studentsSet)

if "Ahmet" in studentsSet:
    print("Listede var")
    
studentsSet.remove("Oğuz")
print(studentsSet)

studentsSet.add("Mehmet")
print(studentsSet)

studentsSet.update(["Merve","Mert","Selin"])
print(studentsSet)

print(len(studentsSet))

studentsSet.discard("Murat") #Remove bulamazsa hata verir, discard vermez.

studentsSet.pop() #İlk elemani siliyor. Pek kullanılmaz.
print(studentsSet)

studentsSet.clear()
print(studentsSet)

# del studentsSet
# print(studentsSet)
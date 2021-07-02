# -*- coding: utf-8 -*-

student1 = "Oğuz"
student2 = "Gürkan"
student3 = "Engin"

students = ["Oğuz","Gürkan","Engin"]

print(students)
print(students[1])

for student in students:
    print(student)
    
students.append("Ahmet")
print(students)

students.remove("Oğuz")
print(students)

#list constructor
sehirler = list(("Ankara","İstanbul","Ankara"))
print(sehirler)
print(len(sehirler))

#diğer fonksiyonlar
# print(sehirler.clear())
# print(sehirler)

print("Ankara sayısı = " + str(sehirler.count("Ankara")))
print("Ankara indexi = " + str(sehirler.index("Ankara")))

sehirler.pop(sehirler.index("Ankara"))
sehirler.insert(0, "Tekirdağ")
print(sehirler)      
sehirler.reverse()
print(sehirler)

sehirler3 = sehirler.copy()

sehirler2 = sehirler
sehirler2[0] = "İzmir"
print(sehirler)
print(sehirler3)

sehirler.extend(sehirler3)
sehirler.sort(reverse=True)
print(sehirler)






students = ["Gurkan","Engin","Derin","Salih","Ali","Ayse"]

fileToAppend = open("students.txt","a")

for student in students:
    fileToAppend.write(student)
    fileToAppend.write("\n")

fileToAppend.close()
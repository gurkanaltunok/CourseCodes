# -*- coding: utf-8 -*-

# substring
message = "Hello World"

for letter in message:
    print(letter)
    
newMessage = message[0:4]

print(newMessage)

print(message[:2])

print(message[2:])

# len
newMessage2 = message[len(message)-1:len(message)]
print(newMessage2)

# lower upper
print(message.lower())
print(message.upper())

# replace
print(message.replace("o", "ö"))

print(message.replace("l", "k"))

# split and strip
information = "Gürkan;Altunok;19;Tekirdag".strip()
print(information.split())
print("Name = "+ information.split(";")[0])

# input
name = input("Your Name = ")
print("Hello "+ name)

number1 = input("Üçgenin Taban Alanını Giriniz = ")
number2 = input("Üçgenin Yüksekliğini Giriniz = ")
alan = ((int(number1)*int(number2))/2)
print("Üçgenin Alanı = " + str(alan)gü)




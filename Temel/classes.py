#%%
class Matematik:
    def __init__(self,x,y):
        self.x = x
        self.y =y

    def topla(self):
        return self.x + self.y

    def cikar(self):
        return self.x - self.y

    def carp(self):
        return self.x * self.y

    def bol(self):
        return self.x / self.y

matematik = Matematik(2,78)
matematik2 = Matematik(3,76)

print("Sonuç = ",matematik.topla())

#%% Property
class Person:
    def __init__(self,firstName,lastName,age) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

person1 = Person("Gürkan","Altunok",33)
print(person1.firstName)

class Worker(Person):
    def __init__(self,salary) -> None:
        self.salary = salary

class Customer(Person):
    def __init__(self,creditCardNumber) -> None:
        self.creditCardNumber = creditCardNumber

ahmet = Worker()
mehmet = Customer()
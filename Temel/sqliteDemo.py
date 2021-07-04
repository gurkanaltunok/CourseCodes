import sqlite3
from sqlite3.dbapi2 import connect

def selectOperations():

    connection = sqlite3.connect("chinook.db")

    #cursor = connection.execute("select FirstName,LastName,City from customers where city = 'Prague' or city = 'Berlin' order by FirstName,LastName desc")

    # for row in cursor:
    #     print("First Name = ", row[0])
    #     print("Last Name = ", row[1])
    #     print("City = ", row[2])
    #     print("********************")

    # cursor = connection.execute("select city, count(*) from Customers group by city having count(*)>1 order by city desc")

    # for row in cursor:
    #     print("City = ", row[0])
    #     print("Count = ", row[1])
    #     print("********************")

    cursor = connection.execute("select FirstName,LastName,City from customers where FirstName like '%a' ")

    for row in cursor:
        print("First Name = ", row[0])
        print("Last Name = ", row[1])
        print("City = ", row[2])
        print("********************")
    connection.close()

selectOperations()

def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("insert into customers (firstName ,lastName ,city ,email) values('Gürkan','Altunok','Tekirdağ','oguzgurkan2001@gmail.com')")

    connection.commit()
    connection.close()

#insertCustomer()

def updateCostumer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("update customers set city ='İstanbul' where city = 'Tekirdağ'")

    connection.commit()
    connection.close()

#updateCostumer()

def deleteCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("delete from customers where city = 'İstanbul' ")

    connection.commit()
    connection.close()

#deleteCustomer()



def joinOperations():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("select albums.Title, artists.Name from artists inner join albums on artists.ArtistId = albums.ArtistId")

    for row in cursor:
        print("Title = ", row[0] + " Name = ", row[1])

    connection.close()

joinOperations()
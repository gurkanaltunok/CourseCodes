import sys
from typing_extensions import final

liste = [7,'gurkan',0,3,"6"]

for x in liste:
    try:
        print("Number: " + str(x))
        result = 1/int(x)
        print("Result: " + str(result))
    except ValueError:
        print(str(x) + " bir sayı değil")
    except ZeroDivisionError:
        print(str(x)+ " için sıfıra bölme hatası")
    except:
        print(str(x) + " hesaplanamadı" )
        print("System says: "+ str(sys.exc_info()[0]))
    finally:
        print("İşlemler Bitti")
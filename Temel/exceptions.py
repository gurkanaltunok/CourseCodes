try:
    sayi = int(input("Sayı Giriniz: "))
except ValueError:
    print("Tip uyuşmazlığı : Lütfen sayı giriniz")
except ZeroDivisionError:
    print("Payda sıfır olamaz")
# except ValueError,ZeroDivisionError:
#     print()
except:
    print("Bir hata oluştu")

print("Bitti")
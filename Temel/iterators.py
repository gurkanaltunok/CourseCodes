sehirler = ["Ankara", "İstanbul", "İzmir","Bursa"]

myIterator = iter(sehirler)

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

for sehir in sehirler:
    print(sehir)
setA = {1,2,3,4,5}
setB = {3,4,5,6,7}

#Union = Birleşim - Duplicate
print(setA | setB)
print(setA.union(setB)) #Tam tersi de olabilir.

#Intersection = Kesişim
print(setA & setB)
print(setA.intersection(setB))

#Difference = Fark
print(setA - setB)
print(setA.difference(setB))
print(setB.difference(setA))

#Symmetric = Birleşim - Ortak Küme
print(setA ^ setB)
print(setA.symmetric_difference(setB))
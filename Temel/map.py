numbers = [1,2,3,4,5]

#numbersSquare = []

numbersSquare = list(map(lambda number: number**2, numbers))

# for number in numbers:
#     numbersSquare.append(number**2)

numbersFiltered = list(filter(lambda number : number>2,numbers))

print(numbersSquare)
print(numbersFiltered)

from functools import reduce
numbersFactoriel = reduce(lambda x,y:x*y,numbers)
print(numbersFactoriel)
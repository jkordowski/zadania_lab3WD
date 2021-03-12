import random
lista1 = [random.randint(0, 10) for x in range(10)]

lista2 = [y for y in lista1 if y % 2 == 0]

print(lista1)
print(lista2)
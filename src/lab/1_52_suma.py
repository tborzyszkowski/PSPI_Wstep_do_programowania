# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista = [x**2 for x in [1, 2, 3, 4, 5]]
print(lista)

suma = 0
for x in lista:
    suma += x

print("Suma:", suma)

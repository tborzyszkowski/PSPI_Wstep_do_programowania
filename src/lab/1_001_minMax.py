import random
#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]

lista = [random.randint(1, 1000) for x in range(1000)]
# minimum = lista[0]
# maksimum = lista[0]
# for x in lista:
#     if x < minimum:
#         minimum = x
#     if x > maksimum:
#         maksimum = x
#
# print('Min:', minimum)
# print('Max:', maksimum)
#
n = len(lista)

i = 0
while i < n-1:
    j = i+1
    min_index = j
    while j < n:
        if lista[j] < lista[min_index]:
            min_index = j
        j += 1
    (lista[i], lista[min_index]) = (lista[min_index], lista[i])
    i += 1

print(lista)


lista = [1, 2, 3]

wartosc = 2

limit = len(lista)
indeks = 0
while indeks < limit:
    if lista[indeks] == wartosc:
        print("tak", indeks)
        break
    indeks += 1

if indeks == limit:
    print("nie")
############################


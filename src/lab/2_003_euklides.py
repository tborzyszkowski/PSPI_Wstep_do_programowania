def nwd(a, b):
    if a == b:
        return a
    elif a > b:
        return nwd(a-b, b)
    else:
        return nwd(a, b-a)


def euklides(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def nwd_list(lista):
    dlugosc = len(lista)
    if dlugosc == 0:
        return 0
    elif dlugosc == 1:
        return lista[0]
    else:
        result = nwd(lista[0], lista[1])
        for el in lista[2:]:
            result = nwd(result, el)
        return result


print(nwd_list([9, 12, 3]))
print(nwd_list([6]))

from functools import reduce

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
            b -= a # b = b - a
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


# print(reduce((lambda x, y: x + y), [1, 2, 3, 4] ))

def nwd_list2(*lista):
    return reduce(euklides, lista)


print(nwd_list2(9, 6, 3, 6, 12, 24, 36))
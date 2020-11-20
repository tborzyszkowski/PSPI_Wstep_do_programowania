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


print(nwd(9, 12), euklides(9, 12))
print(nwd(10, 20), euklides(10, 20))
print(nwd(30, 25), euklides(30, 25))

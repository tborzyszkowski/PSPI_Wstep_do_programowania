from functools import reduce


def min2(a, b):
    if a < b:
        return a
    else:
        return b


def minimum(*argumenty):
    return reduce(min2, argumenty)


# print(minimum(2, 5, 7, 1, 2, 0, 8) == 0)
print(min(2, 5, 0, -1, 3) == 0)
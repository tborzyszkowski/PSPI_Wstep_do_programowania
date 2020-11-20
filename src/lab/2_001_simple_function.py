def mniejsze(arg_1, arg_2):
    if arg_1 < arg_2:
        return True
    else:
        return False

#
# print(mniejsze(1, 2))
# print(mniejsze("Ala", "Ola"))
# print(mniejsze(["Ala", "As"], ["Ola", "kot"]))

def suma_while(n):
    result = 0
    element = n
    while element > 0:
        result += element
        element -= 1
    return result


print(suma_while(1))
print(suma_while(2))
print(suma_while(3))
print(suma_while(10))


def suma_for(n):
    result = 0
    for element in range(1, n+1):
        result += element
    return result

print(suma_for(1))
print(suma_for(2))
print(suma_for(3))
print(suma_for(10))

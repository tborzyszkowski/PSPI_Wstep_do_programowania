def czy_pierwsza(n):
    for j in range(2, n + 1):
        if (n % j) == 0:
            return False
    return True


print(czy_pierwsza(13))
print(czy_pierwsza(9))
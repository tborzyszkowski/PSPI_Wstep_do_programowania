def fib_rek(n):
    if 0 <= n <= 1:
        return n
    else:
        return fib_rek(n - 2) + fib_rek(n - 1)


def fib_linear(n):
    f1 = 0
    f2 = 1
    k = n - 2
    if n < 2:
        f2 = n
    else:
        while k >= 0:
            f2, f1, k = f1 + f2, f2, k-1
    return f2



for liczba in range(30):
    print(liczba, fib_linear(liczba))
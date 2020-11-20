def narysuj_trojkat(n):
    for row in range(n):
        for col in range(row + 1):
            print('*', end='')
        print()


narysuj_trojkat(5)

narysuj_trojkat(4)
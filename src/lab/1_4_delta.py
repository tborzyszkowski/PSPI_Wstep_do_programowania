import math

(a, b, c) = (0, 0, 0)

x1 = None
x2 = None
brak = None
wiele = None

if a != 0:
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
    else:
        if delta < 0:
            brak = True
        else:
            x1 = (-b * 1.0) / (2 * a )
else:
    if b != 0:
        x1 = (-c * 1.0) / b
    else:
        if c != 0:
            brak = True
        else:
            wiele = True

if x1 is None:
    print("x1 =", x1)

if x2 is None:
    print("x2 =", x2)

if brak is None:
    print("Brak")

if wiele is None:
    print("Wiele")

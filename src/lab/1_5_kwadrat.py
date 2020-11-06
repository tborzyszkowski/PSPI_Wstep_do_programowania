x = 997
a = 0

while x > a * a:
    if x != a * a:
        a += 1
if x == a * a:
    print("tak")
else:
    print("nie")
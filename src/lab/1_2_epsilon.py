epsilon = 1
epsilon_poprzedni = epsilon

licznik = 0

while epsilon > 0.0:
    epsilon_poprzedni = epsilon
    epsilon = epsilon / 2
    licznik += 1

print("Licznik:", licznik)
print("Epsilon:", epsilon_poprzedni)
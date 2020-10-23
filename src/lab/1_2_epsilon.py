epsilon = 1
epsilon_poprzedni = epsilon

licznik = 0
limit = 10 * 1000

while epsilon > 0.0 and licznik < limit:
    epsilon_poprzedni = epsilon
    epsilon = epsilon / 2
    licznik += 1

print("Licznik:", licznik)
print("Epsilon:", epsilon_poprzedni)
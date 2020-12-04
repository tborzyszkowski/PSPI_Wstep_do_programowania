def statystyka_ocen(dane, opcje):
    wynik = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for wiersz in dane:
        wynik[int(wiersz["ocena"])] += 1
    return wynik

def wypisz_statystyke_ocen(dane, opcje):
    print(statystyka_ocen(dane, opcje))
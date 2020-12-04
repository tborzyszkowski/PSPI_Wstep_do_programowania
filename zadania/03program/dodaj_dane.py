def zapytaj_o_dane():
    pytania = ["przedmiot", "klasa", "uczen", "ocena", "waga"]
    wynik = {"przedmiot": None, "klasa": None, "uczen": None, "ocena": None, "waga": None}
    for pytanie in pytania:
        odpowiedz = input("Podaj %s:" % pytanie)
        if pytanie == "waga":
            odpowiedz = int(odpowiedz)
        elif pytanie == "ocena":
            odpowiedz = float(odpowiedz)
        wynik[pytanie] = odpowiedz
    return wynik


def dodaj_dane(dane, opcje):
    wiersz = zapytaj_o_dane()
    dane.append(wiersz)
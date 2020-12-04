from dane import dane
from statystyka_ocen import wypisz_statystyke_ocen


dane_programu = []


def wczytaj_dane(dane, opcje):
    global dane_programu
    dane_programu = dane
    print("Wczytano: ", len(dane_programu), " wierszy")


def wypisz_dane(dane, opcje):
    print("przedmiot\t kl\t uczen\t ocena\t waga")
    for wiersz in dane:
        print("%s\t %s\t %s\t %s\t %s" % (wiersz["przedmiot"], wiersz["klasa"], wiersz["uczen"], wiersz["ocena"], wiersz["waga"]))


menu = {
    1: {"opis": "Wczytaj dane", "akcja": wczytaj_dane},
    2: {"opis": "Wypisz dane",  "akcja": wypisz_dane},
    3: {"opis": "Stat ocen",    "akcja": wypisz_statystyke_ocen},
    9: {"opis": "KONIEC",  "akcja": exit}
}


def wypisz_menu():
    for opcja in menu:
        print("%d. \t%s" % (opcja, menu[opcja]["opis"]))


def wybierz_opcje():
    wybor = input("Podaj opcje: ")
    wybor_liczba = -1
    try:
        wybor_liczba = int(wybor)
    except ValueError:
        print("Zly wybor")
    if wybor_liczba in menu:
        print("Wybrales opcje nr: %d: %s" % (wybor_liczba, menu[wybor_liczba]["opis"]))
    else:
        print("Nie ma takiej opcji")
    return wybor_liczba


if __name__ == "__main__":
    while True:
        wypisz_menu()
        wybor = wybierz_opcje()
        if wybor in menu:
            if wybor == 9:
                menu[wybor]["akcja"]()
            else:
                menu[wybor]["akcja"](dane, [])
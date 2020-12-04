from dane import dane
from wypisz_menu import wypisz_menu, wybierz_opcje
from statystyka_ocen import wypisz_statystyke_ocen
from sortuj import sortuj

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
    4: {"opis": "Sortowanie",   "akcja": sortuj},
    9: {"opis": "KONIEC",  "akcja": exit}
}


if __name__ == "__main__":
    while True:
        wypisz_menu(menu)
        wybor = wybierz_opcje(menu)
        if wybor in menu:
            if wybor == 9:
                menu[wybor]["akcja"]()
            else:
                menu[wybor]["akcja"](dane, [])
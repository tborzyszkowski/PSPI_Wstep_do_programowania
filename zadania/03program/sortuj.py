from wypisz_menu import wypisz_menu, wybierz_opcje

def kryterium_przedmiot(wiersz):
    return wiersz["przedmiot"]


def kryterium_klasa(wiersz):
    return wiersz["klasa"]

def kryterium_uczen(wiersz):
    return wiersz["uczen"]


menu_sortowanie= {
    1: {"opis": "Po przedmiocie", "kryterium": kryterium_przedmiot},
    2: {"opis": "Po klasie", "kryterium": kryterium_klasa},
    3: {"opis": "Po uczniu", "kryterium": kryterium_uczen}
}

def sortuj_wg_kryterium(dane, kryterium):
    dane.sort(key=kryterium)


def sortuj(dane, opcje):
    wypisz_menu(menu_sortowanie)
    wybor = wybierz_opcje(menu_sortowanie)
    if wybor in menu_sortowanie:
        kryterium = menu_sortowanie[wybor]["kryterium"]
        sortuj_wg_kryterium(dane, kryterium)
        print("--- Posortowane ---")
    else:
        print(" --- Zla opcja sortowania ---")



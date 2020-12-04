from wypisz_menu import wypisz_menu, wybierz_opcje

def kryterium_przedmiot(wiersz1, wiersz2):
    kryterium_po_kolumnie(wiersz1, wiersz2, "przedmiot")


def kryterium_klasa(wiersz1, wiersz2):
    kryterium_po_kolumnie(wiersz1, wiersz2, "klasa")

def kryterium_uczen(wiersz1, wiersz2):
    kryterium_po_kolumnie(wiersz1, wiersz2, "uczen")


def kryterium_po_kolumnie(wiersz1, wiersz2, kolumna):
    if wiersz1[kolumna] < wiersz2[kolumna]:
        return -1
    elif wiersz1[kolumna] > wiersz2[kolumna]:
        return 1
    else:
        return 0


menu_sortowanie= {
    1: {"opis": "Po przedmiocie", "kryterium": kryterium_przedmiot},
    2: {"opis": "Po klasie", "kryterium": kryterium_klasa},
    3: {"opis": "Po uczniu", "kryterium": kryterium_uczen}
}

def sortuj_wg_kryterium(dane, kryterium):
    sorted(dane, cmp=kryterium)


def sortuj(dane, opcje):
    wypisz_menu(menu_sortowanie)
    wybor = wybierz_opcje(menu_sortowanie)
    if wybor in menu_sortowanie:
        kryterium = menu_sortowanie[wybor]["kryterium"]
        sortuj_wg_kryterium(dane, kryterium)
        print("--- Posortowane ---")
    else:
        print(" --- Zla opcja sortowania ---")



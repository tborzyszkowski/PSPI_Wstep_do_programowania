from dane import dane

menu = {
    1: {"opis": "Wczytaj dane", "akcja": (lambda x, y: x)},
    2: {"opis": "Wypisz dane",  "akcja": (lambda x, y: x)},
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
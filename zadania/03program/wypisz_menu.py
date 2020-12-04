
def wypisz_menu(menu):
    for opcja in menu:
        print("%d. \t%s" % (opcja, menu[opcja]["opis"]))


def wybierz_opcje(menu):
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



def czy_wiersz_pasuje_do_kryterium(wiersz1, kryterium):
    pasuje = True
    for kol in kryterium:
        if kryterium[kol] and kol in wiersz1:
            if kryterium[kol] != wiersz1[kol]:
                pasuje = False
    return pasuje


# przyklad kryterium
# kryterium = {"klasa": "1a", "uczen": "Jan"}
def szukaj_po_kryterium(dane, kryterium):
    wynik = []
    for wiersz in dane:
        if czy_wiersz_pasuje_do_kryterium(wiersz, kryterium):
            wynik.append(wiersz)
    return wynik


def usun_wiersze_z_danych(dane, wiersze):
    for wiersz in wiersze:
        dane.remove(wiersz)


def usun_dane(dane, opcje):
    kryterium = {"przedmiot": None, "klasa": None, "uczen": None, "ocena": None, "waga": None}
    for k in kryterium:
        wartosc = input("Podaj kryterium %s: " % k)
        if wartosc and k == "waga":
            wartosc = int(wartosc)
        elif wartosc and k == "ocena":
            wartosc = float(wartosc)
        kryterium[k] = wartosc
    usun_wiersze_z_danych(dane, szukaj_po_kryterium(dane, kryterium))


def aktualizuj_dane(dane, opcje):
    kryterium = {"przedmiot": None, "klasa": None, "uczen": None, "ocena": None, "waga": None}
    for k in kryterium:
        wartosc = input("Podaj kryterium %s: " % k)
        if wartosc and k == "waga":
            wartosc = int(wartosc)
        elif wartosc and k == "ocena":
            wartosc = float(wartosc)
        kryterium[k] = wartosc
    dane_do_zmiany = szukaj_po_kryterium(dane, kryterium)
    for d in dane_do_zmiany:
        if d["ocena"] == 4.0:
            d["ocena"] = 5.0
    #usun_wiersze_z_danych(dane, szukaj_po_kryterium(dane, kryterium))
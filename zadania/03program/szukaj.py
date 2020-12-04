def czy_wiersz_pasuje_do_kryterium(wiersz1, kryterium):
    pasuje = True
    for kol in kryterium:
        if kryterium[kol]:
            if kryterium[kol] != wiersz1[kol]:
                pasuje = False
    return pasuje


# przykłąd kryterium
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
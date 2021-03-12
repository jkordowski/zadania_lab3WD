def zakupy(** zakup):
    licznik = 0
    cena = sum(zakup.values())
    for x in zakup:
        licznik += 1
    return cena



print(zakupy(czekolada = 4, sok = 3.20, woda = 2, banan = 1))


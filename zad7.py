def iloczynC(* liczby):
    if(len(liczby) == 0):
        return 0
    else:
        wynik = liczby[0]
        pom = liczby[0]
        for x in range(liczby[2]-1):
            pom *= liczby[1]
            wynik *= pom
        return wynik


print(iloczynC(1, 2, 5))


slownik = {"Wołowina": "kg", "Bułki": "sztuki", "Woda": "litry", "Ziemniaki": "kg"}

lista = [x for x in slownik if slownik[x] == "sztuki"]
print(lista)

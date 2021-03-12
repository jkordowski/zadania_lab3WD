def iloczynC(a=1,b=4,ile=10):
    wynik = a
    for x in range(ile-1):
        a *= b
        wynik *= a
    return wynik

print(iloczynC())
print(iloczynC(1,2,5))
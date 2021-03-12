def tp(a,b,c):
    if(a > b):
        if(a > c):
            if(a**2 == b**2 + c**2):
                return "Trójkąt jest prostokątny."
            else:
                return "Trójkąt nie jest prostokątny."
        else:
            if(c**2 == a**2 + b**2):
                return "Trójkąt jest prostokątny."
            else:
                return "Trójkąt nie jest prostokątny."
    else:
        if(b > c):
            if(b**2 == a**2 + c**2):
                return "Trójkąt jest prostokątny."
            else:
                return "Trójkąt nie jest prostokątny."
        else:
            if(c**2 == a**2 + b**2):
                return "Trójkąt jest prostokątny."
            else:
                return "Trójkąt nie jest prostokątny."

print(tp(1,1,6))
print(tp(5,4,3))

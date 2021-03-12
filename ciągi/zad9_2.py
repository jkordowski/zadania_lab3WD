def geo_wyraz_n(a,q,n):
    return a*(q**(n-1))

def geo_suma_n(a,q,n):
    if(q==1):
        return a*n
    else:
        return ((1-q**n)/(1-q))*a

# -*- coding: utf-8 -*-

def main():
    niz = []
    n = int(raw_input('Unesite broj elemenata niza: '))
    for i in range(0, n):
        x = int(raw_input('Unesi sledeci element niza: '))
        niz.append(x)
    print(niz)
    print ("Suma elemenata niza je (prvi nacin): %d" %sumaE(n, niz))
    print ("Suma elemenata niza je (drugi nacin): %d" %sumaE2(niz))



def sumaE(n,niz):
    sum = 0
    i=0
    while i < n:
        sum = sum + niz[i]
        i+=1
    return sum

def sumaE2(niz):
    suma = sum(niz)
    return suma
main()


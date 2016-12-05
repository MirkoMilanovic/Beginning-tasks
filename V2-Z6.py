# -*- coding: utf-8 -*-

def main():
    niz = []
    n = int(raw_input('Unesite broj elemenata niza: '))
    for i in range(0, n):
        x = int(raw_input('Unesi sledeci element niza: '))
        niz.append(x)
    print(niz)
    print ("Suma parnih elemenata niza je (prvi nacin): %d" %sumaE(n, niz))
    print ("Suma parnih elemenata niza je (drugi nacin): %d" %sumaE2(niz))



def sumaE(n,niz):
    sum = 0
    i=1
    while i < n:
        sum = sum + niz[i]
        i+=2
    return sum

def sumaE2(niz):
    niz2=niz[1::2]      #niz2=niz[1:len{niz):2]
    suma = sum(niz2)
    return suma
main()


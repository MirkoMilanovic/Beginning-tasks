# -*- coding: utf-8 -*-

def main():
    a = int(input("Unesite prvi broj: "))
    b = int(input("Unesite drugi broj: "))

    niz = []
    niz.append(a)
    niz.append(b)
    z6(niz)
def z6(niz):
    maxim = max(niz)
    minim = min(niz)
    print ("Maksimalna vrednost je: %d" % maxim)
    print ("Minimalna vrednost je: %d" % minim)
main()







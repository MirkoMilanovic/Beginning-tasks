# -*- coding: utf-8 -*-

import math

def main():

    n = int(input("Unesite broj dimenzija vektora: "))
    print ("Intenzitet vektora je: %f" %zbirKvadrata(n))

def zbirKvadrata(n):
    zbir = 0
    while n > 0:
        d = int(input("Unesite vrednost sledece dimenzije vektora: "))
        zbir += d**2
        n -= 1

    intenzitet = math.sqrt(zbir)
    return intenzitet

main()
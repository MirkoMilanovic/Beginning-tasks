# -*- coding: utf-8 -*-

def main():

    n = int(input("Unesite ceo broj za racunanje faktorijela: "))
    print ("Faktorijal unetog broja je: %d" %faktorijel(n))

def faktorijel(n):
    if n == 1:
        return 1
    else:
        return n * faktorijel(n - 1)

main()
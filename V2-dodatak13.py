# -*- coding: utf-8 -*-

def main():
    n = int(input("Unesite broj n: "))
    k = int(input("Unesite broj k: "))
    z13(n,k)
def z13(n,k):
    p = n
    i = 0
    while ((p // k) != 0):
        p = p - k
        i = i + 1

    print "\nBroj k = ", k, " se u broju n = ", n, " pojavljuje ", i, " puta."
main()







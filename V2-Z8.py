# -*- coding: utf-8 -*-

def main():
    niz = []
    n = int(raw_input('Unesite broj elemenata niza: '))
    for i in range(0, n):
        x = int(raw_input('Unesi sledeci element niza: '))
        niz.append(x)
    print(niz)
    print ("Proizvod elemenata niza je: %d" %proizE(n, niz))


def proizE(n,niz):
    pro = 1
    i=0
    while i < n:
        pro = pro * niz[i]
        i+=1
    return pro

main()


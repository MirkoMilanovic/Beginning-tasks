# -*- coding: utf-8 -*-

def main():
    niz1 = []
    niz2 = []
    novi = []
    n = int(raw_input('Unesite broj elemenata niza 1 i 2: '))
    for i in range(0, n):
        x = int(raw_input('Unesi sledeci element niza 1: '))
        niz1.append(x)
    print("Niz1: ")
    print(niz1)
    for i in range(0, n):
        x = int(raw_input('Unesi sledeci element niza 2: '))
        niz2.append(x)
    print("Niz2: ")
    print(niz2)
    prvi = str(raw_input('Unesite P ili D da bi se izlistavao prvo prvi ili drugi element niza: '))
    print ("Dobijen niz sa naizmenicnim pojavljivanjima elemenata je: %s" %naiz(n, niz1, niz2, novi, prvi))


def naiz(n, niz1, niz2, novi, prvi):
    i=0
    if prvi == "P":
        while i<n:
            novi.append(niz1[i])
            novi.append(niz2[i])
            i += 1
        return novi

    elif prvi == "D":
        while i < n:
            novi.append(niz2[i])
            novi.append(niz1[i])
            i += 1
        return novi
    else:
        print ("Greska pri unosu!")

main()


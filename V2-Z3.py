# -*- coding: utf-8 -*-

def main():
    x1 = float(input("Unesite x koordinatu prvog vektora): "))
    y1 = float(input("Unesite y koordinatu prvog vektora): "))
    z1 = float(input("Unesite z koordinatu prvog vektora): "))

    x2 = float(input("Unesite x koordinatu drugog vektora): "))
    y2 = float(input("Unesite y koordinatu drugog vektora): "))
    z2 = float(input("Unesite z koordinatu drugog vektora): "))
    print ("\nSkalarni proizvod ova dva vektora je: %f." % (skalarni(x1, y1, z1, x2, y2, z2)))

def skalarni(x1, y1, z1, x2, y2, z2):
    sp=x1*x2 + y1*y2 + z1*z2
    return sp

main()
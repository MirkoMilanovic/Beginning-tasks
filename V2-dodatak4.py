# -*- coding: utf-8 -*-

def main():
    a = int(input("Unesite prvi cetvorocifreni broj: "))
    b = int(input("Unesite drugi cetvorocifreni broj: "))
    z4(a,b)
def z4(a,b):
    import math
    b1 = math.floor(b / 1000)  # prva cifra b
    b2 = math.floor((b - b1 * 1000) / 100)  # druga cifra b
    b3 = math.floor((b - b1 * 1000 - b2 * 100) / 10)  # treca cifra b
    b4 = math.floor(b - b1 * 1000 - b2 * 100 - b3 * 10)  # cetvrta cifra b
    c = b1 + b2 + b3 + b4
    print("Suma cifara drugog broja je: %d." % (c))
    a1 = math.floor(a / 1000)  # prva cifra a
    a2 = math.floor((a - a1 * 1000) / 100)  # druga cifra a
    a3 = math.floor((a - a1 * 1000 - a2 * 100) / 10)  # treca cifra a
    a4 = math.floor(a - a1 * 1000 - a2 * 100 - a3 * 10)  # cetvrta cifra a
    d = (a2 + a4) - (a1 + a3)
    print("Razlika zbira cifara prvog broja na parnim i neparnim pozicijama: %d." % (d))
main()
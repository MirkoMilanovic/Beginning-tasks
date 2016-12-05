# -*- coding: utf-8 -*-

import math


def main():
    a = float(input("Unesite kvadratni koeficijent: "))
    b = float(input("Unesite linearni koeficijent: "))
    c = float(input("Unesite slobodni clan: "))
    print ("Resenja kvadratne jednacine su: x1=%f, x2=%f." % (kvadratna1(a, b, c), kvadratna2(a, b, c)))

def kvadratna1(a, b, c):
    d = b**2 - 4 * a * c
    x1 = (-b + math.sqrt(d)) / (2 * a)
    return x1


def kvadratna2(a, b, c):
    d = b**2 - 4 * a * c
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return x2


main()

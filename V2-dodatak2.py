# -*- coding: utf-8 -*-

def main():
    a = int(input("Unesite prvi ceo broj: "))
    b = int(input("Unesite drugi ceo broj: "))
    print("Prvi broj je %d a drugi broj je %d.\n" % (a, b))
    z2(a,b)
def z2(a,b):
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    g = a % b
    print("Zbir brojeva je: %d,\nrazlika brojeva je: %d,\nproizvod brojeva je: %d,\n\
ceo deo deljenja prvog broja drugim je: %d,\ndok je ostatak pri deljenju: %d." %(c,d,e,f,g))
main()







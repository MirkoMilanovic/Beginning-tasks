# -*- coding: utf-8 -*-

def main():
    a = int(input("Unesite prvi broj: "))
    b = int(input("Unesite drugi broj: "))
    c = int(input("Unesite treci broj: "))

    z5(a,b,c)
def z5(a,b,c):
    d = abs((a + b + c) / 3)

    print ("Apsolutna vrednost artimetičke sredine je: %.3f" % d)

main()




# -*- coding: utf-8 -*-

def main():
    a = int(input("Unesite prvi ceo broj: "))
    b = int(input("Unesite drugi ceo broj: "))
    c = int(input("Unesite treci ceo broj: "))
    d = int(input("Unesite cetvrti ceo broj: "))

    pozitivni = []

    print ("Zbir unetih pozitivnih brojeva je: %d" %z7(a,b,c,d,pozitivni))

def z7(a,b,c,d,pozitivni):
    if (a > 0):
        pozitivni.append(a)
    if (b > 0):
        pozitivni.append(b)
    if (c > 0):
        pozitivni.append(c)
    if (d > 0):
        pozitivni.append(d)

    s = (sum(pozitivni))
    return s

main()







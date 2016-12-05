# -*- coding: utf-8 -*-

def main():
    a = int(input('Unesite ceo broj: '))
    cifre = []
    z14(a,cifre)
def z14(a,cifre):
    while a > 0:
        cifre.append(a % 10)
        a //= 10

    n = 0
    p = 0
    i = 0
    for cifra in reversed(cifre):
        if i % 2 == 0:
            n += cifra
        else:
            p += cifra
        i += 1

    print 'Suma brojeva na neparnim mestima je: ', n
    print 'Suma brojeva na parnim mestima je: ', p
    print 'Razlika između suma cifara koje se nalaze na parnim i neparnim mestima je: ', p - n
main()







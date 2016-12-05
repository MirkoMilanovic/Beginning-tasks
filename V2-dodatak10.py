# -*- coding: utf-8 -*-

def main():
    a = unicode(raw_input('Unesite pet karaktera: '))
    z10(a)
def z10(a):
    cif = sum(c.isdigit() for c in a)

    print '\nCifre se pojavljuju ', cif, ' puta.'
main()







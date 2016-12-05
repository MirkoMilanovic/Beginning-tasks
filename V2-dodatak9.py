# -*- coding: utf-8 -*-

def main():
    a = unicode(raw_input("Unesite karakter: "))
    z9(a)
def z9(a):
    asc = ord(a)

    print ("Uneti karakter je: %s,\nASCII kod karaktera je: %s" % (a, asc))

    if a.isalpha():
        print "Odgovarajuce malo (veliko) slovo ovog karaktera je: ", a.swapcase()
main()







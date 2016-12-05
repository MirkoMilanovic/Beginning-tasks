# -*- coding: utf-8 -*-

def main():
    a1 = float(input("Broj stepeni prvog pravca): "))
    a2 = float(input("Broj minuta prvog pravca): "))
    a3 = float(input("Broj sekundi prvog pravca): "))

    b1 = float(input("Broj stepeni drugog pravca): "))
    b2 = float(input("Broj minuta drugog pravca): "))
    b3 = float(input("Broj sekundi drugog pravca): "))

    p1 = float(a1 + a2 / 60 + a3 / 3600)  # prvi pravac
    p2 = float(b1 + b2 / 60 + b3 / 3600)  # drugi pravac

    z3(p1,p2)
def z3(p1,p2):
    import math
    u1 = math.floor(p2 - p1)  # broj stepeni ugla
    u2 = math.floor(((p2 - p1) - int(u1)) * 60)  # broj minuta ugla
    u3 = ((p2 - p1) - int(u1) - u2 / 60) * 3600  # broj sekundi ugla

    print("Ugao dobijen razlikom pravaca je: %.0f stepeni, %.0f minuta i %.2f sekundi" % (u1, u2, u3))

main()



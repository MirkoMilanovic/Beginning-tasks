# -*- coding: utf-8 -*-

def main():
    xm = float(input('Unesite x koordinatu tacke M: '))
    ym = float(input('Unesite y koordinatu tacke M: '))
    x1 = float(input('Unesite x koordinatu tacke A: '))
    y1 = float(input('Unesite y koordinatu tacke A: '))
    x2 = float(input('Unesite x koordinatu tacke B: '))
    y2 = float(input('Unesite y koordinatu tacke B: '))
    x3 = float(input('Unesite x koordinatu tacke C: '))
    y3 = float(input('Unesite y koordinatu tacke C: '))
    z11(xm, ym, x1, y1, x2, y2, x3, y3)

def z11(xm,ym,x1,y1,x2,y2,x3,y3):
    import math

    # Direkcioni ugao od A do B
    if (x2 - x1) > 0 and (y2 - y1) > 0:
        Vab = math.atan2((x2 - x1), (y2 - y1))
    elif (x2 - x1) > 0 and (y2 - y1) < 0:
        Vab = math.atan2((y2 - y1), (x2 - x1)) + 90
    elif (x2 - x1) < 0 and (y2 - y1) < 0:
        Vab = math.atan2((x2 - x1), (y2 - y1)) + 180
    else:
        Vab = math.atan2((y2 - y1), (x2 - x1)) + 270

    # Direkcioni ugao od A do C
    if (x3 - x1) > 0 and (y3 - y1) > 0:
        Vac = math.atan2((x3 - x1), (y3 - y1))
    elif (x3 - x1) > 0 and (y3 - y1) < 0:
        Vac = math.atan2((y3 - y1), (x3 - x1)) + 90
    elif (x3 - x1) < 0 and (y3 - y1) < 0:
        Vac = math.atan2((x3 - x1), (y3 - y1)) + 180
    else:
        Vac = math.atan2((y3 - y1), (x3 - x1)) + 270

    # Ugao CAB
    Ucab = Vab - Vac
    if Ucab < 0:
        Ucab = Ucab + 360

    # --------------------------------------
    # Direkcioni ugao od B do C
    if (x3 - x2) > 0 and (y3 - y2) > 0:
        Vbc = math.atan2((x3 - x2), (y3 - y2))
    elif (x3 - x2) > 0 and (y3 - y2) < 0:
        Vbc = math.atan2((y3 - y2), (x3 - x2)) + 90
    elif (x3 - x2) < 0 and (y3 - y2) < 0:
        Vbc = math.atan2((x3 - x2), (y3 - y2)) + 180
    else:
        Vbc = math.atan2((y3 - y2), (x3 - x2)) + 270

    # Direkcioni ugao od B do A
    if Vab < 180:
        Vba = Vab + 180
    else:
        Vba = Vab - 180

    # Ugao ABC
    Uabc = Vbc - Vba
    if Uabc < 0:
        Uabc = Uabc + 360

    # --------------------------------------
    # Direkcioni ugao od A do M
    if (xm - x1) > 0 and (ym - y1) > 0:
        Vam = math.atan2((xm - x1), (ym - y1))
    elif (xm - x1) > 0 and (ym - y1) < 0:
        Vam = math.atan2((ym - y1), (xm - x1)) + 90
    elif (xm - x1) < 0 and (ym - y1) < 0:
        Vam = math.atan2((xm - x1), (ym - y1)) + 180
    else:
        Vam = math.atan2((ym - y1), (xm - x1)) + 270

    # --------------------------------------
    # Direkcioni ugao od B do M
    if (xm - x2) > 0 and (ym - y2) > 0:
        Vbm = math.atan2((xm - x2), (ym - y2))
    elif (xm - x2) > 0 and (ym - y2) < 0:
        Vbm = math.atan2((ym - y2), (xm - x2)) + 90
    elif (xm - x2) < 0 and (ym - y2) < 0:
        Vbm = math.atan2((xm - x2), (ym - y2)) + 180
    else:
        Vbm = math.atan2((ym - y2), (xm - x2)) + 270

    # ---------------------------------------------------------
    # Ugao CAB je zbir uglova CAM i MAB, takodje ugao ABC je zbor uglova ABM i MBC
    # Ako je to ispunjeno, tacka lezi u povrsi trougla.

    # Ugao CAM
    Ucam = Vam - Vac
    if Ucam < 0:
        Ucam = Ucam + 360

    # Ugao MAB
    Umab = Vab - Vam
    if Umab < 0:
        Umab = Umab + 360

    # Ugao ABM
    Uabm = Vbm - Vba
    if Uabm < 0:
        Uabm = Uabm + 360

    # Ugao MBC
    Umbc = Vbc - Vbm
    if Umbc < 0:
        Umbc = Umbc + 360

    if Ucab == (Ucam + Umab) and Uabc == (Uabm + Umbc):
        print "\n DA"
    else:
        print "\n NE"
main()







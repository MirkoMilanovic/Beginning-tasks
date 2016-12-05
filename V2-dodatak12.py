# -*- coding: utf-8 -*-

import sys

def main():
    x = int(input('Unesite cenu: '))
    novcanice = [5000, 2000, 1000, 200, 100, 50, 20, 10, 1]
    rez = min(novcanice, x)
    printaj_rezultat(novcanice, x, rez)

def min(novcanice, x):      # Najmanji broj novčanica pri plaćanju
  rez = None

  if x == 0:
    rez = { }
    for nov in novcanice:
      rez[nov] = 0
  elif len(novcanice) == 0:     # Ako suma je nula ili ne postoji novcanica za tu sumu, rezultat je nula
     rez = None
  else:                         # Ako suma nije nula ili postoje novcaniče za tu sumu
    nov = novcanice[0]
    ostatak = novcanice[1:]

    max_broj = x / nov
    min_broj_novcanice = sys.maxint

    # moguće kombinacije
    for i in range(max_broj + 1):
      trenutrna_vrednost = x - (nov * i)
      ostatak_rez = min(ostatak, trenutrna_vrednost)

      if ostatak_rez != None:
        nova_vrednost = i + sum(ostatak_rez.values())

        if nova_vrednost < min_broj_novcanice:
          min_broj_novcanice = nova_vrednost
          rez = ostatak_rez
          rez[nov] = i

  return rez

def printaj_rezultat(novcanice, x, rez):
  print "Najmanji broj novčanice za ", x, "koristeći novčanice:", novcanice, "je: "
  if rez == None:
    print "  Ne postoji takva novčanica"
  else:
    print "  %d novčanice" % sum(rez.values())
    print "  date redosledom: ", sorted(rez.items())
  print

main()
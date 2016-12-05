# -*- coding: utf-8 -*-

def main():
    a = int(input("Unesite petocifreni broj: "))
    print ("Najveca cifra petocifrenog broja je: %d" % z8(a))
def z8(a):
    max = 0
    for b in str(a):
        i = int(b)
        if i > max:
            max = i
    return max
main()




a = int(input("Unesite petocifreni broj: "))

max = 0

for b in str(a):
    i = int(b)
    if i > max:
        max = i

print ("Najveca cifra petocifrenog broja je: %d" %max)



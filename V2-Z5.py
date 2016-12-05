# -*- coding: utf-8 -*-

def main():
    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]
    Y = [[5, 8, 1, 2],
         [6, 7, 3, 0],
         [4, 5, 9, 1]]
    rez = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

    print ("Proizvod matrica je: %s" %proizvodMat(X,Y,rez))

def proizvodMat(X,Y,rez):


    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                rez[i][j] += X[i][k] * Y[k][j]

    return rez

main()
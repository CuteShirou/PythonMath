from math import *

def produitMatrice(M, N):
    P = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                P[i][j] += M[i][k] * N[k][j]
    return P
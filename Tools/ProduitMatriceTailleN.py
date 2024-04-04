from math import *

def produit_matrice_taille_n(L, M):
    N = []
    for i in range(len(L)):
        N.append([])
        for j in range(len(M[0])):
            N[i].append(0)
            for k in range(len(M)):
                N[i][j] += L[i][k] * M[k][j]
    return N
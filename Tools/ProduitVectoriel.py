from math import *

def produit_vectoriel(U, V):
        return [U[1]*V[2] - U[2]*V[1], U[2]*V[0] - U[0]*V[2], U[0]*V[1] - U[1]*V[0]]

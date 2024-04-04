from math import *

def vect(A, B):
    c = []
    for i in range (len(A)):
        c.append(B[i]-A[i])
    return c
from math import *

def determinant(matrix):
    # Vérifier si la matrice est carrée
    if len(matrix) != len(matrix[0]):
        raise ValueError("La matrice doit être carrée")

    # Cas de base : matrice 2x2
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    sign = 1

    # Parcourir la première ligne de la matrice
    for col in range(len(matrix)):
        # Calculer le cofacteur de chaque élément de la première ligne
        cofactor = sign * matrix[0][col]
        submatrix = []

        # Construire la sous-matrice en enlevant la première ligne et la colonne actuelle
        for i in range(1, len(matrix)):
            row = []
            for j in range(len(matrix)):
                if j != col:
                    row.append(matrix[i][j])
            submatrix.append(row)

        # Récursivement calculer le déterminant de la sous-matrice
        det += cofactor * determinant(submatrix)

        # Changer le signe pour le prochain élément de la première ligne
        sign *= -1

    return det

def norme(a, b, c):
    return (sqrt(a**2 + b**2 + c**2))

def produitMatrice(M, N):
    P = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                P[i][j] += M[i][k] * N[k][j]
    return P

def produit_matrice_taille_n(L, M):
    N = []
    for i in range(len(L)):
        N.append([])
        for j in range(len(M[0])):
            N[i].append(0)
            for k in range(len(M)):
                N[i][j] += L[i][k] * M[k][j]
    return N

def calculer_produit_scalaire(vecteur1, vecteur2):
    produit_scalaire = sum(v1 * v2 for v1, v2 in zip(vecteur1, vecteur2))
    return produit_scalaire

def produit_vectoriel(U, V):
        return [U[1]*V[2] - U[2]*V[1], U[2]*V[0] - U[0]*V[2], U[0]*V[1] - U[1]*V[0]]

def scal(U, V):
    return (U[0] * V[0] + U[1] * V[1] + U[2] * V[2])

def vect(A, B):
    c = []
    for i in range (len(A)):
        c.append(B[i]-A[i])
    return c

def transformation_type(matrix):
    if matrix == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]:
        return "Transformation identité"
    elif matrix == [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]:
        return "Symétrie par rapport à l’origine"
    elif matrix[0][0] == matrix[1][1] == matrix[2][2] == 0:
        return "Symétrie par rapport à une droite"
    elif matrix[0][0] == matrix[1][1] == 0 and matrix[2][2] == 1:
        return "Symétrie par rapport à un plan"
    elif matrix[0][1] == matrix[1][0] != 0 and matrix[0][0] == matrix[1][1] == 0 and matrix[2][2] == 1:
        return "Rotation par rapport à une droite"
    elif matrix[0][1] == -matrix[1][0] != 0 and matrix[0][0] == matrix[1][1] == 0 and matrix[2][2] == 1:
        return "Anti-rotation par rapport à une droite"
    else:
        return "Pas une isométrie vectorielle"
    
def produitMatrice(M, N):
    # Créer une matrice de zéros de la taille appropriée
    result = [[0 for _ in range(len(N[0]))] for _ in range(len(M))]

    # Parcourir chaque ligne de M
    for i in range(len(M)):
        # Parcourir chaque colonne de N
        for j in range(len(N[0])):
            # Parcourir chaque élément de la ligne de M et de la colonne de N
            for k in range(len(N)):
                result[i][j] += M[i][k] * N[k][j]

    return result
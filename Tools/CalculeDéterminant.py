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

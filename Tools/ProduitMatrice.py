# Définition des matrices
matrice1 = [[1, 2, 3], [4, 5, 6]]
matrice2 = [[7, 8], [9, 10], [11, 12]]

# Vérification des dimensions des matrices
if len(matrice1[0]) != len(matrice2):
    print("Impossible de multiplier les matrices. Les dimensions ne sont pas compatibles.")
else:
    # Initialisation de la matrice résultat
    resultat = [[0 for _ in range(len(matrice2[0]))] for _ in range(len(matrice1))]

    # Calcul du produit de matrices
    for i in range(len(matrice1)):
        for j in range(len(matrice2[0])):
            for k in range(len(matrice2)):
                resultat[i][j] += matrice1[i][k] * matrice2[k][j]

    # Affichage du résultat
    print("Produit de matrices :")
    for row in resultat:
        print(row)
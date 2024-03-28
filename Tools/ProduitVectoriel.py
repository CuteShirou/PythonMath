def produit_vectoriel(a, b):
    x = a[1] * b[2] - a[2] * b[1]
    y = a[2] * b[0] - a[0] * b[2]
    z = a[0] * b[1] - a[1] * b[0]
    return [x, y, z]

# Exemple d'utilisation
vecteur1 = [1, 2, 3]
vecteur2 = [4, 5, 6]

resultat = produit_vectoriel(vecteur1, vecteur2)
print(resultat)
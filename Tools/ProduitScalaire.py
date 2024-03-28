def calculer_produit_scalaire(vecteur1, vecteur2):
    produit_scalaire = sum(v1 * v2 for v1, v2 in zip(vecteur1, vecteur2))
    return produit_scalaire

# Exemple d'utilisation
vecteur1 = [1, 2, 3]
vecteur2 = [4, 5, 6]

resultat = calculer_produit_scalaire(vecteur1, vecteur2)
print("Le produit scalaire des vecteurs est :", resultat)

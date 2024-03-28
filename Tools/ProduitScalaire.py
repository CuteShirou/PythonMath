import numpy as np

def calculer_produit_scalaire(vecteur1, vecteur2):
    produit_scalaire = np.dot(vecteur1, vecteur2)
    return produit_scalaire

# Exemple d'utilisation
vecteur1 = np.array([1, 2, 3])
vecteur2 = np.array([4, 5, 6])

resultat = calculer_produit_scalaire(vecteur1, vecteur2)
print("Le produit scalaire des vecteurs est :", resultat)
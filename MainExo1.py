from Tools.MathTools import *
from math import pi

def Exercice1(mat: Matrice3x3):
    if IsOrthogonal(mat):
        if mat == Matrice3x3():
            return "Transfomation identité"
        elif mat == Matrice3x3([-1, 0, 0], [0, -1, 0], [0, 0, -1]):
            return "Symétrie par rapport à l’origine"
        elif IsSymetric(mat):
            if roundfloat(mat.det()) == 1:
                return "Symétrie par rapport à une droite vectorielle "
            else:
                return "Symétrie par rapport à un plan vectoriel"
        else:
            if roundfloat(mat.det()) == 1:
                return "Rotation par rapport à une droite vectorielle"
            else:
                return "Anti-rotation par rapport à une droite vectorielle"
    else:
        return "Pas une isométrie vectorielle"


if __name__ == "__main__":
    print(Exercice1(Matrice3x3([1, 0, 1], [1, 1, 0], [0, 1, 1]))) # pas une isométrie vectorielle

    print(Exercice1(Matrice3x3())) # Transfomation identité
    print(Exercice1(Matrice3x3([-1, 0, 0], [0, -1, 0], [0, 0, -1]))) # Symétrie par rapport à l’origine

    print(Exercice1(Matrice3x3([sqrt(2)/2, 0, sqrt(2)/2], [0,-1,0], [sqrt(2)/2, 0, -sqrt(2)/2]))) # Symétrie par rapport à une droite vectorielle
    print(Exercice1(Matrice3x3([sqrt(2)/2, 0, sqrt(2)/2], [0,1,0], [sqrt(2)/2, 0, -sqrt(2)/2]))) #symétrie sur plan vectoriel
    
    print(Exercice1(Matrice3x3([1, 0, 0], [0, cos(pi/4), sin(pi/4)], [0, -sin(pi/4), cos(pi/4)]))) # Rotation par rapport à une droite vectorielle
    print(Exercice1(Matrice3x3([-1, 0, 0], [0, cos(pi/4), sin(pi/4)], [0, -sin(pi/4), cos(pi/4)]))) # Anti-rotation par rapport à une droite vectorielle
    print()
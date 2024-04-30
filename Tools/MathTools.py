from math import sqrt, cos, sin

class VectorN:
    def __init__(self, *coord):
        self.coords = list(coord)
        self.dimension = len(coord)
    
    def __str__(self):
        chaine = "("
        for i in range(self.dimension):
            chaine += str(self.coords[i])
            if i+1 != self.dimension:
                chaine += ", "
        return chaine + ")"

    def x(self):
        return self.coords[0]
    
    def y(self):
        return self.coords[1]

    def z(self):
        return self.coords[2]
    
    def __add__(self, other):
        assert self.dimension == other.dimension, "dimension differentes"
        return VectorN(*[other.coords[i] + self.coords[i] for i in range(self.dimension)])

    def __sub__(self, other):
        assert self.dimension == other.dimension, "dimension differentes"
        return VectorN(*[self.coords[i] - other.coords[i] for i in range(self.dimension)])

    def __mul__(self, other):
        return VectorN(*[other * self.coords[i] for i in range(self.dimension)])

    def __truediv__(self, other):
        return VectorN(*[self.coords[i] / other for i in range(self.dimension)])

    def magnitude(self):
        return sqrt(sum([self.coords[i]**2 for i in range(self.dimension)]))

    def normalize( self ):
        return self / self.magnitude()


class Matrice3x3:
    def __init__(self, c1 = [1, 0, 0], c2 = [0, 1, 0], c3 = [0, 0, 1]): 
        self.matrix = [c1, c2, c3]
        self.width = 3 
        self.height = 3 
    
    def __str__(self):
        chaine = ""
        for y in range(3):
            chaine += "| "
            for x in range(3):
                chaine += str(self[x][y]) + ' | ' 
            chaine += "\n"
        return chaine
    
    def __add__(self, other):
        return Matrice3x3(
            [self[0, i] + other[0, i] for i in range(3)],
            [self[1, i] + other[1, i] for i in range(3)],
            [self[2, i] + other[2, i] for i in range(3)]
        )

    def __getitem__(self, index):
        return self.matrix[index]

    def __iter__(self):
        return iter(self.matrix)

    def __eq__(self, other):
        return all(self[i] == other[i] for i in range(len(self.matrix)))

    def __mul__(self, other):
        mat = Matrice3x3()
        for x in range(3):
            for y in range(3):
                mat[x][y] = sum([other[i][y] * self[x][i] for i in range(3)])
        return mat
    
    def Tm(self):
        mat = Matrice3x3()
        for x in range(self.width):
            for y in range(self.height):
                mat[y][x] = self[x][y]
        return mat

    def det(self):
        return (
        self[0][0] * (self[1][1] * self[2][2] - self[1][2] * self[2][1]) +
        self[0][1] * (self[1][2] * self[2][0] - self[1][0] * self[2][2]) +
        self[0][2] * (self[1][0] * self[2][1] - self[1][1] * self[2][0])
    )
    
def roundfloat(x):
    return round(x * 10**5) / 10 ** 5

def Dot(v1, v2):
    assert v1.dimension == v2.dimension, "dimension differentes"
    return roundfloat(sum(v1.coords[i] * v2.coords[i] for i in range(v1.dimension)))

def VecProduct(v1, v2):
    assert v1.dimension == 3 and v2.dimension == 3, "veuillez rentrer des vecteurs 3"
    return VectorN(
        v1.y()*v2.z() - v1.z()*v2.y(),
        v1.z()*v2.x() - v1.x()*v2.z(),
        v1.x()*v2.y() - v1.y()*v2.x(),
    )

def ProjectionOrthogonal(v1, base):
    assert all(v1.dimension == elt.dimension for elt in base), "dimension differentes"
    vec = VectorN(*[0 for _ in range(v1.dimension)])
    for ei in base:
        vec += Dot(ei, v1) * ei
    return vec

def IsOrthogonal(mat):
    vecs = [
        VectorN(mat[0][0], mat[1][0], mat[2][0]),
        VectorN(mat[0][1], mat[1][1], mat[2][1]),
        VectorN(mat[0][2], mat[1][2], mat[2][2])
    ]
    for vec in vecs:
        if roundfloat(vec.magnitude()) != 1:
            return False
    return Dot(vecs[0], vecs[1]) == 0 and Dot(vecs[1], vecs[2]) == 0 and Dot(vecs[0], vecs[2]) == 0

def IsSymetric(mat):
    return mat == mat.Tm()

def multMatrixVec(v1, mat):
    assert v1.dimension == 3, "produit non défini"
    return VectorN(
        Dot(v1, VectorN(mat[0][0], mat[1][0], mat[2][0])),
        Dot(v1, VectorN(mat[0][1], mat[1][1], mat[2][1])),
        Dot(v1, VectorN(mat[0][2], mat[1][2], mat[2][2]))
    )

def MatRot(vec, angle):
    X = vec
    Y = VectorN(-vec.y(), vec.x(), 0)
    Y = Y.normalize()
    Z = VecProduct(X, Y)
    transformation = Matrice3x3(X.coords,Y.coords, Z.coords)
    rot = Matrice3x3([1, 0, 0], [0, cos(angle), sin(angle)], [0, -sin(angle), cos(angle)])
    antitransformation = transformation.Tm()
    return (transformation * rot) * antitransformation
            
if __name__ == "__main__":
    mat = Matrice3x3([1, 2, 3], [3, 4, 5], [6, 7, 8])
    mat2 = Matrice3x3([8, 0, 0], [0, 7, 0], [0, 0, 4])
    vect = VectorN(4,5,6)
    print(mat)
    print(mat.det())
    print()
    print(mat2)
    print()
    print(mat * mat2)
    print(mat.Tm())
    print(vect)
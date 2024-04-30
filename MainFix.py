from math import pi, sqrt, sin, cos
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Exercice 1 : Caractériser qualitativement une isométrie

def scal(u, v):
    return sum(u_i * v_i for u_i, v_i in zip(u, v))

def norme(u):
    return sqrt(scal(u, u))

def det(M):
    return M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0]) + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])

def is_identity_matrix(M):
    return all(M[i][j] == 1 if i == j else M[i][j] == 0 for i in range(3) for j in range(3))

def is_symmetry_origin(M):
    return all(M[i][j] == -1 if i == j else M[i][j] == 0 for i in range(3) for j in range(3))

def is_symmetry_plane(M):
    if abs(det(M)) == 1 and sum(M[i][i] for i in range(3)) == 1:
        return True
    return False

def is_rotation_line(M):
    if det(M) == 1 and -1 < sum(M[i][i] for i in range(3)) < 3:
        return True
    return False

def is_anti_rotation_line(M):
    if det(M) == -1 and -3 < sum(M[i][i] for i in range(3)) < 1:
        return True
    return False

def is_symmetry_line(M):
    if det(M) == 1 and sum(M[i][i] for i in range(3)) == -1:
        return True
    return False

def characterize_isometry(M):
    if is_identity_matrix(M):
        return "Transformation identité"
    elif is_symmetry_origin(M):
        return "Symétrie par rapport à l’origine"
    elif is_symmetry_plane(M):
        return "Symétrie par rapport à un plan"
    elif is_rotation_line(M):
        return "Rotation par rapport à une droite"
    elif is_anti_rotation_line(M):
        return "Anti-rotation par rapport à une droite"
    elif is_symmetry_line(M):
        return "Symétrie par rapport à une droite"
    else:
        return "Pas une isométrie vectorielle"

# Example matrices for testing
M_identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
M_sym_origin = [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
M_sym_plane = [[1, 0, 0], [0, -1, 0], [0, 0, -1]]
M_rot_line = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
M_anti_rot_line = [[0, 1, 0], [-1, 0, 0], [0, 0, -1]]
M_sym_line = [[-1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Testing
print(characterize_isometry(M_identity))  # Should print "Transformation identité"
print(characterize_isometry(M_sym_origin))  # Should print "Symétrie par rapport à l’origine"
print(characterize_isometry(M_sym_plane))  # Should print "Symétrie par rapport à un plan"
print(characterize_isometry(M_rot_line))  # Should print "Rotation par rapport à une droite"
print(characterize_isometry(M_anti_rot_line))  # Should print "Anti-rotation par rapport à une droite"
print(characterize_isometry(M_sym_line))  # Should print "Symétrie par rapport à une droite"



# Paramètres de la simulation
ωR = pi / 6  # Vitesse angulaire de la grande roue
ωN = pi / 3  # Vitesse angulaire de la nacelle
T = 20  # Durée totale
num_positions = 1000
dt = T / num_positions

# Position de la base de la grande roue (point fixe)
N0 = [0, 0, 0]

# Rayon de la grande roue
rayon_grande_roue = 10

# Position initiale du point de centre de la nacelle
centre_nacelle_initial = [rayon_grande_roue, 0, 0]

# Longueurs des côtés du rectangle dans la nacelle
longueur_nacelle = 4
largeur_nacelle = 2

# Rotation autour de l'axe z
def rotate_about_z(point, center, theta):
    x, y, z = point[0] - center[0], point[1] - center[1], point[2] - center[2]
    new_x = x * cos(theta) - y * sin(theta)
    new_y = x * sin(theta) + y * cos(theta)
    return [new_x + center[0], new_y + center[1], z + center[2]]

positions_A, positions_B, positions_C, positions_D = [], [], [], []

for i in range(num_positions):
    theta_R = ωR * i * dt  # Angle de rotation de la grande roue
    theta_N = ωN * i * dt  # Angle de rotation de la nacelle

    # Position du centre de la nacelle à un instant donné
    centre_nacelle = rotate_about_z(centre_nacelle_initial, N0, theta_R)

    # Position des coins de la nacelle par rapport au centre de la nacelle
    A0 = [centre_nacelle[0] - longueur_nacelle / 2, centre_nacelle[1] + largeur_nacelle / 2, centre_nacelle[2]]
    B0 = [centre_nacelle[0] - longueur_nacelle / 2, centre_nacelle[1] - largeur_nacelle / 2, centre_nacelle[2]]
    C0 = [centre_nacelle[0] + longueur_nacelle / 2, centre_nacelle[1] - largeur_nacelle / 2, centre_nacelle[2]]
    D0 = [centre_nacelle[0] + longueur_nacelle / 2, centre_nacelle[1] + largeur_nacelle / 2, centre_nacelle[2]]

    # Rotation des coins de la nacelle autour du centre de la nacelle
    new_A = rotate_about_z(A0, centre_nacelle, theta_N)
    new_B = rotate_about_z(B0, centre_nacelle, theta_N)
    new_C = rotate_about_z(C0, centre_nacelle, theta_N)
    new_D = rotate_about_z(D0, centre_nacelle, theta_N)

    positions_A.append(new_A)
    positions_B.append(new_B)
    positions_C.append(new_C)
    positions_D.append(new_D)

# Tracé des positions

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

def transpose_positions(positions):
    return list(zip(*positions))

ax.plot(*transpose_positions(positions_A), label='Trajectoire de A')
ax.plot(*transpose_positions(positions_B), label='Trajectoire de B')
ax.plot(*transpose_positions(positions_C), label='Trajectoire de C')
ax.plot(*transpose_positions(positions_D), label='Trajectoire de D')

ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Trajectoires des coins de la nacelle sur la grande roue')
plt.show()  
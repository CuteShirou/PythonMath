from math import pi, sqrt, sin, cos
import math
import numpy as np
import matplotlib.pyplot as plt

# Exercice 1 : Caractériser qualitativement une isométrie

def scal(u, v):
    return sum(u_i * v_i for u_i, v_i in zip(u, v))

def norme(u):
    return math.sqrt(scal(u, u))

def det(M):
    return np.linalg.det(M)

def is_identity_matrix(M):
    return np.allclose(M, np.eye(3))

def is_symmetry_origin(M):
    return np.allclose(M, -np.eye(3))

def is_symmetry_plane(M):
    if np.allclose(np.abs(det(M)), 1) and np.trace(M) == 1:
        return True
    return False

def is_rotation_line(M):
    if np.allclose(det(M), 1) and np.trace(M) > -1 and np.trace(M) < 3:
        return True
    return False

def is_anti_rotation_line(M):
    if np.allclose(det(M), -1) and np.trace(M) > -3 and np.trace(M) < 1:
        return True
    return False

def is_symmetry_line(M):
    if np.allclose(det(M), 1) and np.trace(M) == -1:
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
M_identity = np.eye(3)
M_sym_origin = -np.eye(3)
M_sym_plane = np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]])
M_rot_line = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
M_anti_rot_line = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, -1]])
M_sym_line = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])

# Testing
print(characterize_isometry(M_identity))  # Should print "Transformation identité"
print(characterize_isometry(M_sym_origin))  # Should print "Symétrie par rapport à l’origine"
print(characterize_isometry(M_sym_plane))  # Should print "Symétrie par rapport à un plan"
print(characterize_isometry(M_rot_line))  # Should print "Rotation par rapport à une droite"
print(characterize_isometry(M_anti_rot_line))  # Should print "Anti-rotation par rapport à une droite"
print(characterize_isometry(M_sym_line))  # Should print "Symétrie par rapport à une droite"

# Exercice 2 : Rotation dans la nacelle d’une grande roue.

# Paramètres de la simulation
ωR = np.pi / 6  # Vitesse angulaire de la grande roue
ωN = np.pi / 3  # Vitesse angulaire de la nacelle
T = 20  # Durée totale
num_positions = 1000
dt = T / num_positions

# Positions initiales pour un rectangle
N0 = np.array([20, 0, 10])
# Longueurs des côtés du rectangle (différentes pour former un rectangle et non un carré)
longueur = 4  # Longueur du côté plus long du rectangle
largeur = 2   # Longueur du côté plus court du rectangle

A0 = N0 + np.array([-longueur/2, largeur/2, 0])
B0 = N0 + np.array([-longueur/2, -largeur/2, 0])
C0 = N0 + np.array([longueur/2, -largeur/2, 0])
D0 = N0 + np.array([longueur/2, largeur/2, 0])

# Rotation autour de l'axe z
def rotate_about_z(point, theta):
    Rz = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])
    return Rz.dot(point - N0) + N0

positions_A, positions_B, positions_C, positions_D = [], [], [], []

for i in range(num_positions):
    theta_R = ωR * i * dt
    theta_N = ωN * i * dt

    new_A = rotate_about_z(A0, theta_R + theta_N)
    new_B = rotate_about_z(B0, theta_R + theta_N)
    new_C = rotate_about_z(C0, theta_R + theta_N)
    new_D = rotate_about_z(D0, theta_R + theta_N)

    positions_A.append(new_A)
    positions_B.append(new_B)
    positions_C.append(new_C)
    positions_D.append(new_D)

# Tracé des positions
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(*np.transpose(positions_A), label='Trajectoire de A')
ax.plot(*np.transpose(positions_B), label='Trajectoire de B')
ax.plot(*np.transpose(positions_C), label='Trajectoire de C')
ax.plot(*np.transpose(positions_D), label='Trajectoire de D')

# Ajouter les points de départ pour clarifier le rectangle initial
ax.scatter(*A0, color='blue', s=100, label='Départ A')
ax.scatter(*B0, color='red', s=100, label='Départ B')
ax.scatter(*C0, color='green', s=100, label='Départ C')
ax.scatter(*D0, color='purple', s=100, label='Départ D')

ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Trajectoires et points de départ sur la grande roue')
plt.show()
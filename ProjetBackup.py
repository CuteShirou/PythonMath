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

def rotation_matrix(d, theta):
    d = np.array(d, dtype='float64')
    d /= np.linalg.norm(d)  # Normalize vector
    cos_theta = cos(theta)
    sin_theta = sin(theta)
    d_x, d_y, d_z = d
    R = np.array([
        [cos_theta + d_x**2 * (1 - cos_theta), d_x * d_y * (1 - cos_theta) - d_z * sin_theta, d_x * d_z * (1 - cos_theta) + d_y * sin_theta],
        [d_y * d_x * (1 - cos_theta) + d_z * sin_theta, cos_theta + d_y**2 * (1 - cos_theta), d_y * d_z * (1 - cos_theta) - d_x * sin_theta],
        [d_z * d_x * (1 - cos_theta) - d_y * sin_theta, d_z * d_y * (1 - cos_theta) + d_x * sin_theta, cos_theta + d_z**2 * (1 - cos_theta)]
    ])
    return R

def simulate_full_seat_motion(omega_R, omega_N, duration, steps):
    t = np.linspace(0, duration, steps)
    theta_R = omega_R * t
    theta_N = omega_N * t
    
    # Initial positions of points based on the seat being a square
    N0 = np.array([10, 0, 0])
    A0 = np.array([10 - 2 * sqrt(2), 2 * sqrt(2), 0])
    B0 = np.array([10 + 2 * sqrt(2), 2 * sqrt(2), 0])
    C0 = np.array([10 + 2 * sqrt(2), -2 * sqrt(2), 0])
    D0 = np.array([10 - 2 * sqrt(2), -2 * sqrt(2), 0])
    
    A_positions, B_positions, C_positions, D_positions = [], [], [], []

    for theta_r, theta_n in zip(theta_R, theta_N):
        R_R = rotation_matrix([0, 0, 1], theta_r)
        R_N = rotation_matrix([0, 0, 1], theta_n)
        
        N_t = R_R @ N0
        A_positions.append(N_t + R_N @ (A0 - N0))
        B_positions.append(N_t + R_N @ (B0 - N0))
        C_positions.append(N_t + R_N @ (C0 - N0))
        D_positions.append(N_t + R_N @ (D0 - N0))

    return np.array(A_positions), np.array(B_positions), np.array(C_positions), np.array(D_positions)
import matplotlib.pyplot as plt


# Constants
omega_R = pi / 6  # Angular velocity of Ferris wheel
omega_N = pi / 3  # Angular velocity of nacelle
duration = 20  # Total time in seconds
steps = 1000  # Number of steps in simulation

# Run the simulation
A_positions, B_positions, C_positions, D_positions = simulate_full_seat_motion(omega_R, omega_N, duration, steps)

# Plotting all seat points
plt.figure(figsize=(10, 8))
plt.plot(A_positions[:, 0], A_positions[:, 1], 'b-', label="Path of A")
plt.plot(B_positions[:, 0], B_positions[:, 1], 'r-', label="Path of B")
plt.plot(C_positions[:, 0], C_positions[:, 1], 'g-', label="Path of C")
plt.plot(D_positions[:, 0], D_positions[:, 1], 'k-', label="Path of D")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.title("Motion of Seat on Ferris Wheel and Nacelle")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
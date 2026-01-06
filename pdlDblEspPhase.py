import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# =========================
# Paramètres physiques
# =========================
g = 9.81
L1 = L2 = 1.0
m1 = m2 = 1.0

# =========================
# Paramètres numériques
# =========================
dt = 0.01
t_max = 20
N = int(t_max / dt)

# =========================
# Conditions initiales
# =========================
theta1 = np.zeros(N)
theta2 = np.zeros(N)
omega1 = np.zeros(N)
omega2 = np.zeros(N)

theta1[0] = np.pi / 2
theta2[0] = np.pi / 2 + 0.01
omega1[0] = 0.0
omega2[0] = 0.0

# =========================
# Équations du mouvement
# =========================
def derivatives(t1, t2, w1, w2):
    delta = t2 - t1

    den1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta)**2
    den2 = (L2 / L1) * den1

    dw1 = (m2 * L1 * w1**2 * np.sin(delta) * np.cos(delta)
           + m2 * g * np.sin(t2) * np.cos(delta)
           + m2 * L2 * w2**2 * np.sin(delta)
           - (m1 + m2) * g * np.sin(t1)) / den1

    dw2 = (-m2 * L2 * w2**2 * np.sin(delta) * np.cos(delta)
           + (m1 + m2) * g * np.sin(t1) * np.cos(delta)
           - (m1 + m2) * L1 * w1**2 * np.sin(delta)
           - (m1 + m2) * g * np.sin(t2)) / den2

    return dw1, dw2

# =========================
# Intégration numérique
# (Euler semi-implicite)
# =========================
for i in range(N - 1):
    dw1, dw2 = derivatives(theta1[i], theta2[i], omega1[i], omega2[i])

    omega1[i+1] = omega1[i] + dw1 * dt
    omega2[i+1] = omega2[i] + dw2 * dt

    theta1[i+1] = theta1[i] + omega1[i+1] * dt
    theta2[i+1] = theta2[i] + omega2[i+1] * dt

# =========================
# Coordonnées cartésiennes
# =========================
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)

x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

# =========================
# Figure
# =========================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))

# ----- Espace réel -----
ax1.set_xlim(-2.2, 2.2)
ax1.set_ylim(-2.2, 2.2)
ax1.set_aspect('equal')
ax1.set_title("Pendule double — espace réel")

line, = ax1.plot([], [], 'o-', lw=2)
trace, = ax1.plot([], [], lw=1, alpha=0.4)

# ----- Espace des phases -----
ax2.set_xlim(-np.pi, np.pi)
ax2.set_ylim(-8, 8)
ax2.set_title("Espace des phases $(\\theta_1,\\omega_1)$")
ax2.set_xlabel(r"$\theta_1$")
ax2.set_ylabel(r"$\omega_1$")

phase, = ax2.plot([], [], lw=1)

# =========================
# Animation
# =========================
def update(frame):
    line.set_data([0, x1[frame], x2[frame]],
                  [0, y1[frame], y2[frame]])

    trace.set_data(x2[:frame], y2[:frame])
    phase.set_data(theta1[:frame], omega1[:frame])

    return line, trace, phase

ani = FuncAnimation(fig, update, frames=N, interval=dt*1000)

plt.tight_layout()
plt.show()

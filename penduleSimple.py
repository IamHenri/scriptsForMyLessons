import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# =========================
# Paramètres physiques
# =========================
g = 9.81        # gravité (m/s^2)
L = 1.0         # longueur du pendule (m)

# =========================
# Paramètres numériques
# =========================
dt = 0.02       # pas de temps
t_max = 20      # durée de la simulation
N = int(t_max / dt)

# =========================
# Conditions initiales
# =========================
theta0 = np.pi / 2     # angle initial (rad)
omega0 = 0.0           # vitesse angulaire initiale

# =========================
# Tableaux
# =========================
theta = np.zeros(N)
omega = np.zeros(N)
time = np.linspace(0, t_max, N)

theta[0] = theta0
omega[0] = omega0

# =========================
# Intégration numérique
# (Euler semi-implicite)
# =========================
for i in range(N - 1):
    omega[i+1] = omega[i] - (g / L) * np.sin(theta[i]) * dt
    theta[i+1] = theta[i] + omega[i+1] * dt

# =========================
# Coordonnées cartésiennes
# =========================
x = L * np.sin(theta)
y = -L * np.cos(theta)

# =========================
# Création de la figure
# =========================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# ----- Pendule -----
ax1.set_xlim(-L-0.2, L+0.2)
ax1.set_ylim(-L-0.2, L+0.2)
ax1.set_aspect('equal')
ax1.set_title("Pendule simple sans frottement")

line, = ax1.plot([], [], 'o-', lw=2)
trace, = ax1.plot([], [], '-', lw=1, alpha=0.5)

# ----- Espace des phases -----
ax2.set_xlim(-np.pi, np.pi)
ax2.set_ylim(-4, 4)
ax2.set_title("Espace des phases")
ax2.set_xlabel(r"$\theta$")
ax2.set_ylabel(r"$\omega$")

phase, = ax2.plot([], [], lw=1)

# =========================
# Animation
# =========================
def update(frame):
    # Pendule
    line.set_data([0, x[frame]], [0, y[frame]])
    trace.set_data(x[:frame], y[:frame])

    # Espace des phases
    phase.set_data(theta[:frame], omega[:frame])

    return line, trace, phase

ani = FuncAnimation(fig, update, frames=N, interval=dt*1000)

plt.tight_layout()
plt.show()

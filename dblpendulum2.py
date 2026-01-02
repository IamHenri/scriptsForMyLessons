import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# -------------------------------
# Paramètres physiques
# -------------------------------
g = 9.81        # gravité
L1, L2 = 1.0, 1.0
m1, m2 = 1.0, 1.0

# -------------------------------
# Équations du pendule double
# -------------------------------
def double_pendulum(t, y):
    th1, w1, th2, w2 = y
    delta = th2 - th1

    den1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta)**2
    den2 = (L2 / L1) * den1

    dth1 = w1
    dth2 = w2

    dw1 = (
        m2 * L1 * w1**2 * np.sin(delta) * np.cos(delta)
        + m2 * g * np.sin(th2) * np.cos(delta)
        + m2 * L2 * w2**2 * np.sin(delta)
        - (m1 + m2) * g * np.sin(th1)
    ) / den1

    dw2 = (
        -m2 * L2 * w2**2 * np.sin(delta) * np.cos(delta)
        + (m1 + m2) * g * np.sin(th1) * np.cos(delta)
        - (m1 + m2) * L1 * w1**2 * np.sin(delta)
        - (m1 + m2) * g * np.sin(th2)
    ) / den2

    return [dth1, dw1, dth2, dw2]

# -------------------------------
# Conditions initiales
# -------------------------------
state = np.array([np.pi/2, 0.0, np.pi/2, 0.0])
dt = 0.03  # pas de temps par simulation

# -------------------------------
# Initialisation animation
# -------------------------------
plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
# Trace du second pendule
trace_x, trace_y = [], []
TRACE_LENGTH = 1500
trace, = ax.plot([], [], '-', lw=1, alpha=0.4)

# -------------------------------
# Boucle infinie de simulation
# -------------------------------
while plt.fignum_exists(fig.number):

    # Intégration pour un pas
    sol = solve_ivp(
        double_pendulum,
        [0, dt],
        state,
        t_eval=[dt]
    )
    state = sol.y[:, -1]

    th1, _, th2, _ = state

    # Coordonnées cartésiennes
    x1 = L1 * np.sin(th1)
    y1 = -L1 * np.cos(th1)
    x2 = x1 + L2 * np.sin(th2)
    y2 = y1 - L2 * np.cos(th2)

    # Mise à jour pendule
    line.set_data([0, x1, x2], [0, y1, y2])

    # Mise à jour trace
    trace_x.append(x2)
    trace_y.append(y2)
    if len(trace_x) > TRACE_LENGTH:
        trace_x.pop(0)
        trace_y.pop(0)
    trace.set_data(trace_x, trace_y)

    # Pause pour animation
    plt.pause(dt)

plt.ioff()



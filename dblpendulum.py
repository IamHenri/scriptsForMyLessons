import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------------------
# Paramètres physiques
# -------------------------------
g = 9.81      # gravité
L1 = 1.0      # longueur pendule 1
L2 = 1.0      # longueur pendule 2
m1 = 1.0      # masse pendule 1
m2 = 1.0      # masse pendule 2

# -------------------------------
# Équations du pendule double
# -------------------------------
def double_pendulum(t, y):
    theta1, omega1, theta2, omega2 = y

    delta = theta2 - theta1

    den1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta)**2
    den2 = (L2 / L1) * den1

    dtheta1 = omega1
    dtheta2 = omega2

    domega1 = (
        m2 * L1 * omega1**2 * np.sin(delta) * np.cos(delta)
        + m2 * g * np.sin(theta2) * np.cos(delta)
        + m2 * L2 * omega2**2 * np.sin(delta)
        - (m1 + m2) * g * np.sin(theta1)
    ) / den1

    domega2 = (
        -m2 * L2 * omega2**2 * np.sin(delta) * np.cos(delta)
        + (m1 + m2) * g * np.sin(theta1) * np.cos(delta)
        - (m1 + m2) * L1 * omega1**2 * np.sin(delta)
        - (m1 + m2) * g * np.sin(theta2)
    ) / den2

    return [dtheta1, domega1, dtheta2, domega2]

# -------------------------------
# Conditions initiales
# -------------------------------
y0 = [
    np.pi / 2,  # theta1
    0.000001,        # omega1
    np.pi / 2,  # theta2
    0.0         # omega2
]

# Temps
t_span = (0, 20)
t_eval = np.linspace(*t_span, 2000)

# -------------------------------
# Résolution numérique
# -------------------------------
sol = solve_ivp(double_pendulum, t_span, y0, t_eval=t_eval)

theta1 = sol.y[0]
theta2 = sol.y[2]

# -------------------------------
# Conversion en coordonnées cartésiennes
# -------------------------------
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)

x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

# -------------------------------
# Animation
# -------------------------------
fig, ax = plt.subplots()
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], '-', lw=1, alpha=0.5)

trace_x, trace_y = [], []

def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    line.set_data(thisx, thisy)

    trace_x.append(x2[i])
    trace_y.append(y2[i])
    trace.set_data(trace_x, trace_y)

    return line, trace

ani = FuncAnimation(
    fig, animate, frames=len(t_eval),
    interval=20, blit=True
)

plt.title("Pendule double — dynamique chaotique")
plt.show()



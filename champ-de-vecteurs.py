import numpy as np
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(12,9))
a, b = 10, 10
x, y = np.linspace(-5, a, 500), np.linspace(-5, b, 500)
X, Y = np.meshgrid(x, y)
#
#U = -2*Y/(X*X+Y*Y)
#V = X/(X*X+Y*Y)
#
#
U = np.sin(X)-np.sin(Y)
V = np.sin(X)+np.sin(Y)
#
#
#U = 2*np.log(X)
#V = 1/Y
#
#U = 2*X-3*Y
#V = 2*X+3*Y
#
#U = np.cos(X)
#V = np.sin(Y)
#
#U = X
#V = np.exp(Y)
#
#U = X**2
#V = Y**2

plt.streamplot(X, Y, U, V)
plt.show()

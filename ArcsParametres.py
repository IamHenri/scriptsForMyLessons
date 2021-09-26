import numpy as np
import matplotlib.pyplot as plt
def x(t) :
    return np.cos(2*t)
    #return t**2+t-1
def y(t) :
    return np.sin(3*t)
    #return t**2-t+1
#T = np.arange(0, 2*np.pi, 0.01)
T = np.arange(-100, 100, 0.01)
X = x(T)
Y = y(T)
plt.axis('equal')
plt.plot(X, Y)
plt.show()

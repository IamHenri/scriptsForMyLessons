#source : https://www.developpez.net/forums/d1560556/autres-langages/python/general-python/rotation-quaternions/
import time
from numpy import sin,cos
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("auto")
ax.set_autoscale_on(True)
 
def q_conj(q):
    ''' Renvoie le conjugué d'un quaternion '''
    w, x, y, z = q
    return (w, -x, -y, -z)
 
def normalise(v, tolerance=0.00001):
    ''' Normalise un quaternion'''
    mag2 = sum(n * n for n in v)
    if abs(mag2 - 1.0) > tolerance:
        mag = np.sqrt(mag2)
        v = tuple(n / mag for n in v)
    return v
 
def axeangle_to_q(v, theta):
    ''' Renvoie le quaternion associé à une rotation d'un angle theta et autour de l'axe v '''
    v = normalise(v)
    x, y, z = v
    theta /= 2
    w = cos(theta)
    x = x * sin(theta)
    y = y * sin(theta)
    z = z * sin(theta)
    return w, x, y, z
 
def q_to_axeangle(q):
    ''' Renvoie l'axe et l'angle de rotation associé à un quaternion '''
    w, v = q[0], q[1:]
    theta = np.arccos(w) * 2.0
    return normalise(v), theta
 
def q_mult(q1, q2):
    ''' Multiplie 2 quaternions ensemble (attention à la non-commutativité) '''
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return w, x, y, z
 
def qv_mult(q1, v1):
    ''' Applique le procédé de conjugaison pour réaliser une rotation '''
    q2 = (0.0,) + v1
    return q_mult(q_mult(q1, q2), q_conj(q1))[1:]  
 
def array_to_tuple(v):
    x = v[0]
    y = v[1]
    z = v[2]
    return x,y,z
 
def dessiner_cube_quaternion(q):
    r = [-10, 10]
    for s, e in combinations(np.array(list(product(r,r,r))), 2):
        if np.sum(np.abs(s-e)) == r[1]-r[0]:
            s_rotated=qv_mult(q,array_to_tuple(s))
            e_rotated=qv_mult(q,array_to_tuple(e))
            ax.plot3D(*zip(s_rotated,e_rotated), color="b")
 
theta=np.radians(45)
q=axeangle_to_q((0,0,1),theta)
dessiner_cube_quaternion(q)
 
plt.show()

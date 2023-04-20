# -*- coding: utf-8 -*-
"""
@author: Delphine
source : http://culturesciencesphysique.ens-lyon.fr/ressource/chute-libre-python-1.xml
DESCRIPTION

Ce code propose une résolution numérique, basée sur la méthode d'Euler, d'un problème de chute libre d'une balle sans prendre en compte les frottements de l'air.
La trajectoire et la vitesse sont calculées jusqu'à ce que la balle touche le sol.
"""

"""
BIBLIOTHEQUES
"""
# import de la bibliothèque numpy (gestion de matrices et routines mathématiques) en lui donnant le surnom np
import numpy as np
# import de la bibliothèque matplotlib (graphiques) en lui donnant le surnom plt
import matplotlib.pyplot as plt



""" INITIALISATION ET DEFINITION DES PARAMETRES DE SIMULATION"""
# accélération de la pesanteur 9,81 N.m-2
g = 9.81

# définition du pas de temps = 0,001 seconde
dt = 0.001

# rayon de la balle (en m)
r = 0.03
# ordonnée initiale du corps (en m)    
y_0 = 1.5
# vitesse verticale initiale du corps (en m/s)
vy_0 = 0

"""
INITIALISATION DES VARIABLES DE CALCUL
"""
# ordonnée initiale = y0
y = y_0
# on crée un vecteur qui va contenir toutes les positions successives au cours du mouvement
position_y=[y]
# vitesse verticale initiale = vy_0
vy = vy_0
# on crée un vecteur qui va contenir toutes les vitesses successives au cours du mouvement
vitesse_y=[vy]

"""
CALCUL DU MOUVEMENT
"""
i = 0        # indice de la boucle

# La boucle est exécutée tant que le corps n'a pas touché le sol :
# (tant que la position y de son centre d'inertie est supérieure à son rayon)
while (y > r) :
    vy = vy - g*dt
    vitesse_y = vitesse_y+ [vy]

    y = y + vy*dt
    position_y = position_y+ [y]
    
    i = i + 1

temps = np.linspace(0,i,i+1)*dt    
print("La balle a atteint le sol en",round(temps[i],3), "s")
print("Le calcul a réalisé",i,"itérations avec un pas de temps de",dt,"s")

"""
TRACE DE LA VITESSE

"""
# Représentation graphique de la vitesse
plt.plot(temps,vitesse_y,"bo",label="résolution numérique")

# Résolution analytique
nb_pts = int(1000/temps[i])
temps_analyt = np.linspace(0,temps[i],nb_pts)
vy_analyt = - g * temps_analyt + vy_0 

plt.plot(temps_analyt,vy_analyt,"-r", lw=2.5, label="résolution analytique")
plt.legend()
plt.title("Vitesse verticale de la balle au cours du temps")
plt.xlabel("temps (s)")  
plt.ylabel("vitesse (m/s)")
plt.grid(True)
plt.show() 



"""
TRACE DE LA TRAJECTOIRE
"""
# Représentation graphique de la trajectoire
plt.plot(temps,position_y,"bo",label="résolution numérique")

# Résolution analytique
nb_pts = int(1000/temps[i])
temps_analyt = np.linspace(0,temps[i],nb_pts)
y_analyt = - 1/2 * g * temps_analyt **2 + vy_0 * temps_analyt + y_0

plt.plot(temps_analyt,y_analyt,"-r", lw=2.5, label="résolution analytique")
plt.legend()
plt.title("Position verticale de la balle au cours du temps")
plt.xlabel("temps (s)")  
plt.ylabel("position (m)")
plt.grid(True)
plt.show() 

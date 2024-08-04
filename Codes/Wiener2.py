import numpy as np
import matplotlib.pyplot as plt

# Paramètres
T = 1.0  # Temps total
N = 1000  # Nombre de pas de temps
dt = T / N  # Pas de temps
mu = 0  # Drift
sigma = 1  # Volatilité

# Génération du processus de Wiener
t = np.linspace(0, T, N+1)  # Vecteur de temps

# Simulation des processus de Wiener
nb_trajectories = 3  # Nombre de trajectoires à tracer
W_trajectories = np.zeros((nb_trajectories, N+1))  # Matrice pour stocker les trajectoires

# Générer les trajectoires de Wiener
for i in range(nb_trajectories):
    dW = np.random.normal(loc=0, scale=np.sqrt(dt), size=N)  # Incréments de Wiener
    W_trajectories[i, 1:] = np.cumsum(dW)  # Calcul des valeurs du processus de Wiener

# Tracé des trajectoires de Wiener
plt.figure(figsize=(10, 6))
for i in range(nb_trajectories):
    plt.plot(t, W_trajectories[i], label=f'Trajectoire {i+1}')

plt.title('Processus de Wiener en 1D')
plt.xlabel('Temps')
plt.ylabel('Valeur')
plt.legend()
plt.grid(True)
plt.show()

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
W = np.zeros(N+1)  # Vecteur pour stocker les valeurs du processus de Wiener
W[0] = 0  # Condition initiale

# Simulation du processus de Wiener
for i in range(1, N+1):
    dW = np.random.normal(loc=0, scale=np.sqrt(dt))  # Incrément de Wiener
    W[i] = W[i-1] + mu*dt + sigma*dW  # Équation du processus de Wiener

# Tracé du processus de Wiener
plt.plot(t, W)
plt.title('Processus de Wiener en 1D')
plt.xlabel('Temps')
plt.ylabel('Valeur')
plt.grid(True)
plt.show()

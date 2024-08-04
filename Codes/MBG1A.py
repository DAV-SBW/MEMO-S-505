import numpy as np
import matplotlib.pyplot as plt

# Paramètres
prix_initial = 0.21  # Prix initial de l'électricité en euros par kWh
alpha = 0.02  # Paramètre de tendance
sigma = 0.22  # Paramètre de volatilité
temps_simulation_annees = 10  # Durée de la simulation en années
nb_points = 1000  # Nombre de points pour la simulation

# Tracé du graphe
plt.figure(figsize=(10, 6))
plt.title("Simulation de l'évolution des prix de l'électricité")
plt.xlabel('Temps (années)')
plt.ylabel('Prix de l\'électricité (€/kWh)')
plt.axhline(y=prix_initial, color='r', linestyle='--', label='Prix initial')
plt.grid(True)

# Répétition de l'expérience 3 fois
for _ in range(3):
    # Simulation du mouvement brownien géométrique
    temps_simulation = np.linspace(0, temps_simulation_annees, nb_points)
    delta_t = temps_simulation[1] - temps_simulation[0]
    brownian_motion = np.random.standard_normal(size=nb_points)
    log_prix = np.zeros_like(temps_simulation)
    log_prix[0] = np.log(prix_initial)

    for i in range(1, nb_points):
        drift = (alpha - 0.5 * sigma**2) * delta_t
        diffusion = sigma * np.sqrt(delta_t) * brownian_motion[i]
        log_prix[i] = log_prix[i-1] + drift + diffusion

    # Transformation logarithmique inverse pour obtenir les prix
    prix_simulation = np.exp(log_prix)

    # Tracé de la simulation
    plt.plot(temps_simulation, prix_simulation, label='Simulation GBM')

plt.legend()
plt.show()

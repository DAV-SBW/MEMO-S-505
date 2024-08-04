import numpy as np
import matplotlib.pyplot as plt

# Paramètres
prix_initial = 0.21  # Prix initial de l'électricité en euros par kWh
alpha = 0.02  # Paramètre de tendance
sigma = 0.12  # Paramètre de volatilité
temps_simulation_annees = 30  # Durée de la simulation en années
nb_points = 3000  # Nombre de points pour la simulation

# Simulation du mouvement brownien géométrique
temps_simulation = np.linspace(0, temps_simulation_annees, nb_points+1)
delta_t = temps_simulation[1] - temps_simulation[0]
brownian_motion = np.random.standard_normal(size=nb_points)
log_prix = np.zeros_like(temps_simulation)
log_prix[0] = np.log(prix_initial)

for i in range(1, nb_points+1):
    drift = (alpha - 0.5 * sigma**2) * delta_t
    diffusion = sigma * np.sqrt(delta_t) * brownian_motion[i-1]
    log_prix[i] = log_prix[i-1] + drift + diffusion

# Transformation logarithmique inverse pour obtenir les prix
prix_simulation = np.exp(log_prix)

# Séparation des données par années
prix_par_annee = np.array_split(prix_simulation, temps_simulation_annees)

# Calcul des moyennes et des écarts types par année
moyennes_annee = [np.mean(annee) for annee in prix_par_annee]
ecarts_types_annee = [np.std(annee) for annee in prix_par_annee]

# Tracé des graphiques
plt.figure(figsize=(14, 6))
plt.subplot(1, 3, 1)
plt.plot(temps_simulation, prix_simulation, label='Simulation GBM')
plt.title("Évolution des prix de l'électricité (30 ans)")
plt.xlabel('Temps (années)')
plt.ylabel('Prix de l\'électricité (€/kWh)')
plt.axhline(y=prix_initial, color='r', linestyle='--', label='Prix initial')
plt.legend()
plt.grid(True)

plt.subplot(1, 3, 2)
plt.plot(np.arange(0, temps_simulation_annees), moyennes_annee, marker='o', color='b', linestyle='-')
plt.title('Prix moyen annuel')
plt.xlabel('Année')
plt.ylabel('Prix moyen (€/kWh)')
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(np.arange(0, temps_simulation_annees), ecarts_types_annee, marker='o', color='g', linestyle='-')
plt.title('Écart type annuel')
plt.xlabel('Année')
plt.ylabel('Écart type (€/kWh)')
plt.grid(True)

plt.tight_layout()
plt.show()

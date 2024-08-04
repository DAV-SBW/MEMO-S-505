import numpy as np
import matplotlib.pyplot as plt

# Paramètres
prix_initial = 0.21  # Prix initial de l'électricité en euros par kWh
moyenne = 0.21  # Moyenne de réversion à la moyenne
theta = 0.5  # Coefficient de réversion à la moyenne
sigma = 0.11  # Paramètre de volatilité
temps_simulation_annees = 30  # Durée de la simulation en années
nb_points = 3000  # Nombre de points pour la simulation
nb_repetitions = 100  # Nombre de répétitions de l'expérience

# Préparation des tableaux pour stocker les résultats des différentes expériences
prix_simulations = []

# Répétition de l'expérience
for _ in range(nb_repetitions):
    # Simulation du modèle de réversion à la moyenne
    temps_simulation = np.linspace(0, temps_simulation_annees, nb_points + 1)
    delta_t = temps_simulation[1] - temps_simulation[0]
    brownian_motion = np.random.standard_normal(size=nb_points)
    prix = np.zeros_like(temps_simulation)
    prix[0] = prix_initial

    for i in range(1, nb_points + 1):
        drift = theta * (moyenne - prix[i - 1]) * delta_t
        diffusion = sigma * np.sqrt(delta_t) * brownian_motion[i - 1]
        prix[i] = prix[i - 1] + drift + diffusion

    # Stockage du résultat de cette expérience
    prix_simulations.append(prix)

# Calcul des prix moyens et des écarts types pour chaque année sur les différentes simulations
prix_moyens = np.mean(prix_simulations, axis=0)
prix_ecarts_types = np.std(prix_simulations, axis=0)

# Calcul de la moyenne et de la variance des prix finaux
prix_finaux = np.array([sim[-1] for sim in prix_simulations])
moyenne_prix_final = np.mean(prix_finaux)
variance_prix_final = np.var(prix_finaux)

# Tracé des graphiques
plt.figure(figsize=(18, 12))

# Graphique 1 : Évolution des prix de l'électricité
plt.subplot(2, 2, 1)
for i in range(nb_repetitions):
    plt.plot(temps_simulation, prix_simulations[i])
plt.title("Évolution des prix de l'électricité (30 ans)")
plt.xlabel('Temps (années)')
plt.ylabel('Prix de l\'électricité (€/kWh)')
plt.axhline(y=prix_initial, color='r', linestyle='--', label='Prix initial')
plt.legend()
plt.grid(True)

# Graphique 2 : Prix moyen annuel
plt.subplot(2, 2, 2)
plt.plot(np.arange(0, temps_simulation_annees + 1), prix_moyens[:temps_simulation_annees + 1], marker='o', color='dodgerblue',
         linestyle='-')
plt.title('Prix moyen annuel')
plt.xlabel('Année')
plt.ylabel('Prix moyen (€/kWh)')
plt.grid(True)

# Graphique 3 : Écart type annuel
plt.subplot(2, 2, 3)
plt.plot(np.arange(0, temps_simulation_annees + 1), prix_ecarts_types[:temps_simulation_annees + 1], marker='o',
         color='g', linestyle='-')
plt.title('Écart type annuel')
plt.xlabel('Année')
plt.ylabel('Écart type (€/kWh)')
plt.grid(True)

# Graphique 4 : Histogramme des prix de fin de période
plt.subplot(2, 2, 4)
plt.hist(prix_finaux, bins=50, color='skyblue', edgecolor='black', alpha=0.7, density=True, label='Distribution des prix finaux')
plt.title('Histogramme des prix de fin de période')
plt.xlabel('Prix de fin de période (€/kWh)')
plt.ylabel('Densité de probabilité')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

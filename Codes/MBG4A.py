import numpy as np
import matplotlib.pyplot as plt

# Paramètres
prix_initial = 0.21  # Prix initial de l'électricité en euros par kWh
alpha = 0.01  # Paramètre de tendance
sigma = 0.11  # Paramètre de volatilité
temps_simulation_annees = 30  # Durée de la simulation en années
nb_points = 3000  # Nombre de points pour la simulation
nb_repetitions = 5  # Nombre de répétitions de l'expérience

# Préparation des tableaux pour stocker les résultats des différentes expériences
prix_simulations = []

# Répétition de l'expérience
for _ in range(nb_repetitions):
    # Simulation du mouvement brownien géométrique
    temps_simulation = np.linspace(0, temps_simulation_annees, nb_points + 1)
    delta_t = temps_simulation[1] - temps_simulation[0]
    brownian_motion = np.random.standard_normal(size=nb_points)
    log_prix = np.zeros_like(temps_simulation)
    log_prix[0] = np.log(prix_initial)

    for i in range(1, nb_points + 1):
        drift = (alpha - 0.5 * sigma ** 2) * delta_t
        diffusion = sigma * np.sqrt(delta_t) * brownian_motion[i - 1]
        log_prix[i] = log_prix[i - 1] + drift + diffusion

    # Transformation logarithmique inverse pour obtenir les prix
    prix_simulation = np.exp(log_prix)

    # Stockage du résultat de cette expérience
    prix_simulations.append(prix_simulation)

# Calcul des prix moyens et des écarts types pour chaque année sur les différentes simulations
prix_moyens = np.mean(prix_simulations, axis=0)
prix_ecarts_types = np.std(prix_simulations, axis=0)

# Tracé des graphiques
plt.figure(figsize=(18, 6))

# Graphique 1 : Évolution des prix de l'électricité
plt.subplot(1, 4, 1)
for i in range(nb_repetitions):
    plt.plot(temps_simulation, prix_simulations[i], label=f'Simulation {i + 1}')
plt.title("Évolution des prix de l'électricité (30 ans)")
plt.xlabel('Temps (années)')
plt.ylabel('Prix de l\'électricité (€/kWh)')
plt.axhline(y=prix_initial, color='r', linestyle='--', label='Prix initial')
plt.legend()
plt.grid(True)

# Graphique 2 : Prix moyen annuel
plt.subplot(1, 4, 2)
plt.plot(np.arange(0, temps_simulation_annees + 1), prix_moyens[:temps_simulation_annees + 1], marker='o', color='dodgerblue',
         linestyle='-')
plt.title('Prix moyen annuel')
plt.xlabel('Année')
plt.ylabel('Prix moyen (€/kWh)')
plt.grid(True)

# Graphique 3 : Écart type annuel
plt.subplot(1, 4, 3)
plt.plot(np.arange(0, temps_simulation_annees + 1), prix_ecarts_types[:temps_simulation_annees + 1], marker='o',
         color='g', linestyle='-')
plt.title('Écart type annuel')
plt.xlabel('Année')
plt.ylabel('Écart type (€/kWh)')
plt.grid(True)

# Graphique 4 : Histogramme des prix de fin de période
# Récupération des données de fin de période
prix_fin_periode = [sim[-1] for sim in prix_simulations]

# Détermination du nombre d'intervalles
nb_intervals = 50
interval_size = (max(prix_fin_periode) - min(prix_fin_periode)) / nb_intervals

# Création des intervalles
intervals = [(min(prix_fin_periode) + i * interval_size, min(prix_fin_periode) + (i + 1) * interval_size) for i in range(nb_intervals)]

# Comptage des occurrences dans chaque intervalle
occurrences_par_intervalle = [0] * nb_intervals
for prix in prix_fin_periode:
    for i, (min_interval, max_interval) in enumerate(intervals):
        if min_interval <= prix < max_interval:
            occurrences_par_intervalle[i] += 1
            break

# Tracé de l'histogramme
plt.subplot(1, 4, 4)
plt.bar(range(nb_intervals), occurrences_par_intervalle, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Histogramme des prix de fin de période')
plt.xlabel('Intervalles de prix de fin de période (€/kWh)')
plt.ylabel('Nombre de simulations')
plt.xticks(range(0, nb_intervals, 5), [f'{intervals[i][0]:.2f} - {intervals[i][1]:.2f}' for i in range(0, nb_intervals, 5)], rotation=45, ha='right')
plt.grid(True)

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

# Paramètres
prix_initial = 0.21  # Prix initial de l'électricité en euros par kWh
alpha = 0.01  # Paramètre de tendance
sigma = 0.11  # Paramètre de volatilité
temps_simulation_annees = 30  # Durée de la simulation en années
nb_points = 3000  # Nombre de points pour la simulation
nb_repetitions = 2500  # Nombre de répétitions de l'expérience

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

# Calcul de la moyenne et de la variance des prix finaux
prix_finaux = np.array([sim[-1] for sim in prix_simulations])
moyenne_prix_final = np.mean(prix_finaux)
variance_prix_final = np.var(prix_finaux)

# Tracé de l'histogramme des prix de fin de période
plt.figure(figsize=(10, 6))
plt.hist(prix_finaux, bins=50, color='skyblue', edgecolor='black', alpha=0.7, density=True, label='Distribution des prix finaux')

# Superposition de la fonction de densité de probabilité de la distribution lognormale
x = np.linspace(min(prix_finaux), max(prix_finaux), 1000)
pdf_lognormale = lognorm.pdf(x, s=np.sqrt(np.log(1 + variance_prix_final / moyenne_prix_final**2)), scale=moyenne_prix_final)
plt.plot(x, pdf_lognormale, 'r-', lw=2, label='Distribution lognormale')

plt.title('Histogramme des prix de fin de période avec distribution lognormale')
plt.xlabel('Prix de fin de période (€/kWh)')
plt.ylabel('Densité de probabilité')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

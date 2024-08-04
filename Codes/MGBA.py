import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fonction pour simuler un GBM
def simulate_gbm(S0, mu, sigma, T, n_simulations=10000, n_steps=1000):
    dt = T / n_steps
    prices = np.zeros((n_simulations, n_steps + 1))
    prices[:, 0] = S0
    for t in range(1, n_steps + 1):
        Z = np.random.standard_normal(n_simulations)
        prices[:, t] = prices[:, t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
    return prices[:, -1]

# Paramètres de base
S0_base = 100
mu_base = 0.05
sigma_base = 0.2
T = 30

# Variations des paramètres
S0_values = [80, 120]
mu_values = [0.03, 0.07]
sigma_values = [0.15, 0.25]

# Simulations pour les paramètres de base
base_price = simulate_gbm(S0_base, mu_base, sigma_base, T).mean()

# Simulations pour les variations des paramètres
results = {
    'Paramètre': [],
    'Valeur de base': [],
    'Variation': [],
    'Prix attendu après 30 ans': []
}

# Variation de S0
for S0 in S0_values:
    price = simulate_gbm(S0, mu_base, sigma_base, T).mean()
    results['Paramètre'].append('S0')
    results['Valeur de base'].append(S0_base)
    results['Variation'].append(S0)
    results['Prix attendu après 30 ans'].append(price)

# Variation de mu
for mu in mu_values:
    price = simulate_gbm(S0_base, mu, sigma_base, T).mean()
    results['Paramètre'].append('mu')
    results['Valeur de base'].append(mu_base)
    results['Variation'].append(mu)
    results['Prix attendu après 30 ans'].append(price)

# Variation de sigma
for sigma in sigma_values:
    price = simulate_gbm(S0_base, mu_base, sigma, T).mean()
    results['Paramètre'].append('sigma')
    results['Valeur de base'].append(sigma_base)
    results['Variation'].append(sigma)
    results['Prix attendu après 30 ans'].append(price)

# Création du DataFrame
df_results = pd.DataFrame(results)

# Affichage du tableau
print(df_results)

# Optionnel: Visualisation des résultats
plt.figure(figsize=(10, 6))
plt.plot(df_results['Variation'], df_results['Prix attendu après 30 ans'], 'o-', label='Variation')
plt.title('Analyse de Sensibilité du Mouvement Brownien Géométrique')
plt.xlabel('Variation des Paramètres')
plt.ylabel('Prix Attendu après 30 ans')
plt.legend()
plt.grid(True)
plt.show()

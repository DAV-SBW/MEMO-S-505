import pandas as pd
import matplotlib.pyplot as plt

# Données extraites de la carte
data = {
    'Pays': ['Cap Vert', 'Gambie', 'Sénégal', 'Ghana', 'Nigéria', 'Côte d\'Ivoire', 'Togo', 'Cameroun', 'Ouganda', 'Kenya',
             'Rwanda', 'Tanzanie', 'Zambie', 'Namibie', 'Afrique du Sud', 'Eswatini', 'Zimbabwe', 'Mozambique',
             'Madagascar', 'Maurice'],
    'Capacité installée (GW)': [0.1, 0.1, 0.9, 3.8, 4.9, 1.9, 0.2, 1.3, 0.9, 2.2, 0.2, 1.6, 2.6, 0.6, 50.2, 0.2, 2.1, 0.5,
                                0.5, 0.8],
    'Part des IPPs (%)': [20, 43, 32, 18, 31, 52, 49, 24, 19, 25, 34, 19, 11, 23, 11, 23, 9, 10, 10, 39]
}

# Création du DataFrame
df = pd.DataFrame(data)

# Tracé du graphique
fig, ax1 = plt.subplots(figsize=(14, 8))

color = 'tab:blue'
ax1.set_xlabel('Pays')
ax1.set_ylabel('Capacité installée (GW)', color=color)
ax1.bar(df['Pays'], df['Capacité installée (GW)'], color=color, alpha=0.6, label='Capacité installée (GW)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticklabels(df['Pays'], rotation=90)

ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('Part des IPPs (%)', color=color)
ax2.plot(df['Pays'], df['Part des IPPs (%)'], color=color, marker='o', label='Part des IPPs (%)')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Capacité installée et part des IPPs en Afrique')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Données de consommation d'électricité nationale pour chaque pays africain
data_electricity_consumption = {
    'Country': [
        'Cap Vert', 'Gambie', 'Sénégal', 'Ghana', 'Nigéria', 'Côte d\'Ivoire', 'Togo', 'Cameroun',
        'Ouganda', 'Kenya', 'Rwanda', 'Tanzanie', 'Zambie', 'Namibie', 'Afrique du Sud', 'Eswatini',
        'Zimbabwe', 'Mozambique', 'Madagascar', 'Maurice', 'Algérie', 'Angola', 'Bénin', 'Botswana',
        'Burkina Faso', 'Burundi', 'Comores', 'RD Congo', 'Djibouti', 'Égypte', 'Érythrée', 'Ethiopie',
        'Gabon', 'Guinée', 'Lesotho', 'Libéria', 'Libye', 'Mali', 'Mauritanie', 'Maroc', 'Niger',
        'Sao Tomé-et-Principe', 'Seychelles', 'Sierra Leone', 'Somalie', 'Soudan', 'Swaziland', 'Tunisie'
    ],
    'Electricity Consumption (TWh)': [
        0.25, 0.12, 3.6, 15, 34, 9, 0.9, 5.4, 2.6, 11, 0.6, 7, 11, 2.8, 207, 1.3,
        9, 3, 2, 1.2, 55, 9, 1.8, 4.5, 2.1, 0.2, 0.1, 8, 0.3, 162, 0.1, 12, 3.6,
        1.4, 1, 0.4, 6.5, 2.2, 0.6, 36, 0.7, 0.15, 0.1, 0.4, 0.05, 4, 1.1, 16
    ]
}

# Données du pourcentage des IPP pour chaque pays
part_IPP = {
    'Cap Vert': 20, 'Gambie': 43, 'Sénégal': 32, 'Ghana': 18, 'Nigéria': 31,
    'Côte d\'Ivoire': 52, 'Togo': 49, 'Cameroun': 24, 'Ouganda': 19, 'Kenya': 25,
    'Rwanda': 34, 'Tanzanie': 19, 'Zambie': 11, 'Namibie': 23, 'Afrique du Sud': 11,
    'Eswatini': 23, 'Zimbabwe': 9, 'Mozambique': 10, 'Madagascar': 10, 'Maurice': 39,
    'Algérie': 0, 'Angola': 0, 'Bénin': 3, 'Botswana': 1, 'Burkina Faso': 3,
    'Burundi': 2, 'Comores': 4, 'RD Congo': 3, 'Djibouti': 0, 'Égypte': 0,
    'Érythrée': 0, 'Ethiopie': 0, 'Gabon': 0, 'Guinée': 0, 'Lesotho': 0,
    'Libéria': 0, 'Libye': 0, 'Mali': 4, 'Mauritanie': 0, 'Maroc': 0,
    'Niger': 0, 'Sao Tomé-et-Principe': 0, 'Seychelles': 0, 'Sierra Leone': 0,
    'Somalie': 0, 'Soudan': 0, 'Swaziland': 0, 'Tunisie': 0, 'Ouganda': 19
}

# Création des DataFrames
df_electricity_consumption = pd.DataFrame(data_electricity_consumption)
df_ipp_corrected = pd.DataFrame(list(part_IPP.items()), columns=['Country', 'IPP Share (%)'])

# Fusionner les DataFrames sur la colonne 'Country'
df_combined_corrected = pd.merge(df_electricity_consumption, df_ipp_corrected, on='Country')

# Traçage du graphique
fig, ax = plt.subplots(figsize=(14, 8))

ax.set_title('Consommation d\'électricité en fonction de la part des IPPs')
ax.set_xlabel('Part des IPPs (%)')
ax.set_ylabel('Consommation d\'électricité (TWh)')

# Tracé du scatter plot
ax.scatter(df_combined_corrected['IPP Share (%)'], df_combined_corrected['Electricity Consumption (TWh)'], color='b', label='Pays Africains')

# Ajout des labels pour chaque point
for i, row in df_combined_corrected.iterrows():
    ax.text(row['IPP Share (%)'], row['Electricity Consumption (TWh)'], row['Country'], fontsize=8)

# Légende
ax.legend(loc='upper left')

# Définir la couleur de fond en blanc pour l'ensemble du graphique
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Grille
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Affichage du graphique
plt.tight_layout()
plt.show()

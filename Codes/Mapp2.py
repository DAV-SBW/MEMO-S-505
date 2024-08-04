import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Données d'accès à l'électricité en milieu rural (2022) - Données fictives pour cet exemple
acces_electricite_rural = {
    'Botswana': 25.0, 'République du Congo': 12.4, 'Lesotho': 37.7, 'Madagascar': 10.9, 'Malawi': 5.6,
    'Mozambique': 5.0, 'Namibie': 33.2, 'Niger': 7.7, 'Rwanda': 38.2, 'Tanzanie': 36.0,
    'Comores': 82.9, 'Gabon': 29.0, 'Libéria': 14.9, 'Mauritanie': 0.8, 'Nigéria': 27.0,
    'Eswatini': 81.6, 'Afrique du Sud': 93.4, 'Cap-Vert': 96.9, 'Côte d\'Ivoire': 45.3, 'Ouganda': 35.9,
    'Tchad': 1.3, 'Bénin': 45.5, 'Burkina Faso': 3.4, 'Cameroun': 25.0, 'Ghana': 71.6,
    'Zambie': 14.5, 'Zimbabwe': 33.7, 'Burundi': 1.7, 'Guinée': 21.3, 'Kenya': 65.6,
    'Sao Tomé-et-Principe': 73.7, 'Sénégal': 43.4, 'Sierra Leone': 5.0, 'Mali': 18.3,
    'Gambie': 31.2, 'Togo': 25.0, 'Seychelles': 100.0, 'Éthiopie': 43.0, 'Maurice': 100.0,
    'RD Congo': 1.0
}

# Données du nombre de blocs de consommation selon Briceño-Garmendia & Shkaratan (2011)
blocs_consommation = {
    'Botswana': 1, 'République du Congo': 1, 'Lesotho': 1, 'Madagascar': 1, 'Malawi': 1,
    'Mozambique': 1, 'Namibie': 1, 'Niger': 1, 'Rwanda': 1, 'Tanzanie': 1,
    'Comores': 1, 'Gabon': 1, 'Libéria': 1, 'Mauritanie': 1, 'Nigéria': 1,
    'Eswatini': 1, 'Afrique du Sud': 2, 'Cap-Vert': 2, 'Côte d\'Ivoire': 2, 'Ouganda': 2,
    'Tchad': 3, 'Bénin': 3, 'Burkina Faso': 3, 'Cameroun': 3, 'Ghana': 3,
    'Zambie': 3, 'Zimbabwe': 3, 'Burundi': 3, 'Guinée': 3, 'Kenya': 4,
    'Sao Tomé-et-Principe': 3, 'Sénégal': 3, 'Sierra Leone': 3, 'Mali': 4,
    'Gambie': 4, 'Togo': 4, 'Seychelles': 5, 'Éthiopie': 7, 'Maurice': 8,
    'RD Congo': 11
}

# Combiner les données dans un DataFrame
donnees = {
    'Pays': list(acces_electricite_rural.keys()),
    'Accès à l\'électricité en milieu rural (%)': list(acces_electricite_rural.values()),
    'Blocs de consommation': [blocs_consommation[pays] for pays in acces_electricite_rural.keys()]
}
df = pd.DataFrame(donnees)

# Tracer les données
plt.figure(figsize=(14, 8))
for i, row in df.iterrows():
    plt.scatter(row['Blocs de consommation'], row['Accès à l\'électricité en milieu rural (%)'], label=row['Pays'])

plt.xlabel('Nombre de blocs de consommation')
plt.ylabel('Accès à l\'électricité en milieu rural (%)')
plt.grid(True)

# Annoter chaque point avec le nom du pays
for i, row in df.iterrows():
    plt.annotate(row['Pays'], (row['Blocs de consommation'], row['Accès à l\'électricité en milieu rural (%)']),
                 textcoords="offset points", xytext=(0,10), ha='center')

# Tracer la droite de régression
X = df['Blocs de consommation']
Y = df['Accès à l\'électricité en milieu rural (%)']
m, b = np.polyfit(X, Y, 1)
plt.plot(X, m*X + b, color='red', linestyle='--', linewidth=2)

# Calculer le coefficient de détermination R²
Y_pred = m*X + b
ss_res = np.sum((Y - Y_pred) ** 2)
ss_tot = np.sum((Y - np.mean(Y)) ** 2)
r2 = 1 - (ss_res / ss_tot)

# Titre avec le coefficient de détermination R²
plt.title(f'Accès à l\'électricité en milieu rural vs. Nombre de blocs de consommation (R² = {r2:.2f})')

# Sauvegarder le graphique dans un fichier
plt.savefig("acces_electricite_vs_blocs_consommation.png")

# Afficher le graphique
plt.show()

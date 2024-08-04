import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Données d'accès à l'électricité en milieu urbain (2022) - Données fictives pour cet exemple
acces_electricite_urbain = {
    'Botswana': 71.1, 'République du Congo': 67.5, 'Lesotho': 83.6, 'Madagascar': 71.6, 'Malawi': 54.0,
    'Mozambique': 79.4, 'Namibie': 74.8, 'Niger': 66.1, 'Rwanda': 98.0, 'Tanzanie': 74.7,
    'Comores': 100.0, 'Gabon': 98.5, 'Libéria': 53.7, 'Mauritanie': 91.6, 'Nigéria': 89.0,
    'Eswatini': 86.1, 'Afrique du Sud': 87.1, 'Cap-Vert': 95.3, 'Côte d\'Ivoire': 95.0, 'Ouganda': 72.0,
    'Tchad': 46.3, 'Bénin': 71.1, 'Burkina Faso': 60.5, 'Cameroun': 94.0, 'Ghana': 95.0,
    'Zambie': 87.0, 'Zimbabwe': 89.0, 'Burundi': 64.0, 'Guinée': 91.0, 'Kenya': 98.0,
    'Sao Tomé-et-Principe': 80.0, 'Sénégal': 96.6, 'Sierra Leone': 55.3, 'Mali': 99.7,
    'Gambie': 82.8, 'Togo': 96.5, 'Seychelles': 100.0, 'Éthiopie': 94.0, 'Maurice': 99.0,
    'RD Congo': 45.3
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
    'Pays': list(acces_electricite_urbain.keys()),
    'Accès à l\'électricité en milieu urbain (%)': list(acces_electricite_urbain.values()),
    'Blocs de consommation': [blocs_consommation[pays] for pays in acces_electricite_urbain.keys()]
}
df = pd.DataFrame(donnees)

# Tracer les données
plt.figure(figsize=(14, 8))
for i, row in df.iterrows():
    plt.scatter(row['Blocs de consommation'], row['Accès à l\'électricité en milieu urbain (%)'], label=row['Pays'])

plt.xlabel('Nombre de blocs de consommation')
plt.ylabel('Accès à l\'électricité en milieu urbain (%)')
plt.grid(True)

# Annoter chaque point avec le nom du pays
for i, row in df.iterrows():
    plt.annotate(row['Pays'], (row['Blocs de consommation'], row['Accès à l\'électricité en milieu urbain (%)']),
                 textcoords="offset points", xytext=(0,10), ha='center')

# Tracer la droite de régression
X = df['Blocs de consommation']
Y = df['Accès à l\'électricité en milieu urbain (%)']
m, b = np.polyfit(X, Y, 1)
plt.plot(X, m*X + b, color='red', linestyle='--', linewidth=2)

# Calculer le coefficient de détermination R²
Y_pred = m*X + b
ss_res = np.sum((Y - Y_pred) ** 2)
ss_tot = np.sum((Y - np.mean(Y)) ** 2)
r2 = 1 - (ss_res / ss_tot)

# Titre avec le coefficient de détermination R²
plt.title(f'Accès à l\'électricité en milieu urbain vs. Nombre de blocs de consommation (R² = {r2:.2f})')

# Sauvegarder le graphique dans un fichier
plt.savefig("acces_electricite_vs_blocs_consommation.png")

# Afficher le graphique
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Données réelles pour les taux d'accès à l'électricité en milieu rural (2020)
acces_electricite_rural = {
    'Tanzanie': 22.0, 'Chad': 1.6, 'Togo': 24.3, 'Lesotho': 35.2, 'Liberia': 8.1,
    'Sierra Leone': 4.7, 'Senegal': 38.6, 'Sao Tome and Principe': 71.0, 'Comores': 80.1,
    'Congo, Dem. Rep.': 1.0, 'Central African Republic': 1.9, 'Congo, Rep.': 11.8, 'Cameroon': 24.2,
    'Cote d\'Ivoire': 43.7, 'Nigeria': 24.6, 'Niger': 9.7, 'Gabon': 24.7, 'Mozambique': 4.6,
    'Kenya': 62.7, 'Rwanda': 34.9, 'Zambia': 14.0, 'Zimbabwe': 37.1, 'Botswana': 26.2,
    'Burundi': 0.9, 'Ethiopia': 39.4, 'Guinea': 19.3, 'Malawi': 3.5, 'Mali': 16.8, 'Mauritania': 0.8,
    'South Sudan': 5.4, 'Uganda': 32.8
}

# Données réelles pour les superficies (en km²)
superficie = {
    'Tanzanie': 945087, 'Chad': 1284000, 'Togo': 56785, 'Lesotho': 30355, 'Liberia': 111369,
    'Sierra Leone': 71740, 'Senegal': 196722, 'Sao Tome and Principe': 964, 'Comores': 2235,
    'Congo, Dem. Rep.': 2344858, 'Central African Republic': 622984, 'Congo, Rep.': 342000, 'Cameroon': 475442,
    'Cote d\'Ivoire': 322463, 'Nigeria': 923768, 'Niger': 1267000, 'Gabon': 267668, 'Mozambique': 801590,
    'Kenya': 580367, 'Rwanda': 26338, 'Zambia': 752612, 'Zimbabwe': 390757, 'Botswana': 581730,
    'Burundi': 27834, 'Ethiopia': 1104300, 'Guinea': 245857, 'Malawi': 118484, 'Mali': 1240192, 'Mauritania': 1030700,
    'South Sudan': 619745, 'Uganda': 241038
}

# Combiner les données dans un DataFrame
donnees = {
    'Pays': list(acces_electricite_rural.keys()),
    'Accès à l\'électricité en milieu rural (%)': list(acces_electricite_rural.values()),
    'Superficie (km²)': [superficie[pays] for pays in acces_electricite_rural.keys()]
}
df = pd.DataFrame(donnees)

# Tracé du graphique
plt.figure(figsize=(14, 8))
plt.scatter(df['Superficie (km²)'], df['Accès à l\'électricité en milieu rural (%)'], color='blue', marker='x')

# Annoter chaque point avec le nom du pays
for i, row in df.iterrows():
    plt.annotate(row['Pays'], (row['Superficie (km²)'], row['Accès à l\'électricité en milieu rural (%)']),
                 textcoords="offset points", xytext=(0,10), ha='center')

# Tracer la droite de régression
X = df['Superficie (km²)']
Y = df['Accès à l\'électricité en milieu rural (%)']
m, b = np.polyfit(X, Y, 1)
plt.plot(X, m*X + b, color='red', linestyle='--', linewidth=0.8)

# Calculer le coefficient de détermination R²
Y_pred = m*X + b
ss_res = np.sum((Y - Y_pred) ** 2)
ss_tot = np.sum((Y - np.mean(Y)) ** 2)
r2 = 1 - (ss_res / ss_tot)

# Titre avec le coefficient de détermination R²
plt.xlabel('Superficie (km²)')
plt.ylabel('Accès à l\'électricité en milieu rural (%)')
plt.title(f'Taux d\'accès à l\'électricité en milieu rural vs Superficie (R² = {r2:.2f})')
plt.grid(True)
plt.show()

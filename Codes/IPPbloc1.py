import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Données disponibles pour les taux d'accès à l'électricité en milieu rural
acces_electricite_rural = {
    'RC (Brazaville)': 12.4, 'Lesotho': 37.7, 'Madagascar': 10.9, 'Sénégal': 43.4,
    'Botswana': 25.0, 'Ouganda': 35.9, 'Bénin': 45.5, 'Nigéria': 27.0,
    'Tchad': 1.3, 'Malawi': 5.6, 'Cap-Vert': 96.9, 'Côte d’Ivoire': 45.3,
    'Burkina Faso': 3.4, 'Cameroun': 12.4, 'Ethiopie': 43.0,
    'Ghana': 71.6, 'Kenya': 65.6, 'Tanzanie': 36.0, 'Zimbabwe': 33.7,
    'Mozambique': 5.0, 'RDC (Kinshasa)': 1.0, 'Zambie': 14.5, 'Mali': 18.3
}

# Données de l'écart entre le premier et le dernier bloc de consommation (%)
ecart_blocs = {
    'RC (Brazaville)': 0, 'Lesotho': 0, 'Madagascar': 0, 'Sénégal': 10,
    'Botswana': 0, 'Ouganda': 585, 'Bénin': 70, 'Nigéria': 622,
    'Tchad': 143, 'Malawi': 105, 'Cap-Vert': 24, 'Côte d’Ivoire': 106,
    'Burkina Faso': 13, 'Cameroun': 40, 'Ethiopie': 150,
    'Ghana': 101, 'Kenya': 798, 'Tanzanie': 622, 'Zimbabwe': 2159,
    'Mozambique': 203, 'RDC (Kinshasa)': 114, 'Zambie': 131, 'Mali': 0
}

# Création du DataFrame
donnees = {
    'Pays': list(acces_electricite_rural.keys()),
    'Accès à l\'électricité en milieu rural (%)': list(acces_electricite_rural.values()),
    'Écart entre le premier et le dernier bloc (%)': list(ecart_blocs.values())
}
df = pd.DataFrame(donnees)

# Tracé du graphique
plt.figure(figsize=(14, 8))
plt.scatter(df['Écart entre le premier et le dernier bloc (%)'], df['Accès à l\'électricité en milieu rural (%)'], color='blue', marker='x')

# Annoter chaque point avec le nom du pays
for i, row in df.iterrows():
    plt.annotate(row['Pays'], (row['Écart entre le premier et le dernier bloc (%)'], row['Accès à l\'électricité en milieu rural (%)']),
                 textcoords="offset points", xytext=(0,10), ha='center')

# Tracer la droite de régression
X = df['Écart entre le premier et le dernier bloc (%)']
Y = df['Accès à l\'électricité en milieu rural (%)']
m, b = np.polyfit(X, Y, 1)
plt.plot(X, m*X + b, color='red', linestyle='--', linewidth=0.8)

# Calculer le coefficient de détermination R²
Y_pred = m*X + b
ss_res = np.sum((Y - Y_pred) ** 2)
ss_tot = np.sum((Y - np.mean(Y)) ** 2)
r2 = 1 - (ss_res / ss_tot)

# Titre avec le coefficient de détermination R²
plt.xlabel('Écart entre le premier et le dernier bloc (%)')
plt.ylabel('Accès à l\'électricité en milieu rural (%)')
plt.title(f'Taux d\'accès à l\'électricité en milieu rural en fonction de l\'écart entre le premier et le dernier bloc (R² = {r2:.2f})')
plt.grid(True)
plt.show()

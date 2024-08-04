import pandas as pd
import matplotlib.pyplot as plt

# Données disponibles pour les taux d'accès à l'électricité en milieu rural
acces_electricite_rural = {
    'Cap Vert': 96.9, 'Gambie': 31.2, 'Sénégal': 43.4, 'Ghana': 71.6, 'Nigéria': 27.0,
    'Côte d\'Ivoire': 45.3, 'Togo': 25.0, 'Cameroun': 12.4, 'Ouganda': 35.9, 'Kenya': 65.6,
    'Rwanda': 38.2, 'Tanzanie': 36.0, 'Zambie': 14.5, 'Namibie': 33.2, 'Afrique du Sud': 93.4,
    'Eswatini': 81.6, 'Zimbabwe': 33.7, 'Mozambique': 5.0, 'Madagascar': 10.9, 'Maurice': 100.0
}

# Données du pourcentage des IPP pour chaque pays
part_IPP = {
    'Cap Vert': 20, 'Gambie': 43, 'Sénégal': 32, 'Ghana': 18, 'Nigéria': 31,
    'Côte d\'Ivoire': 52, 'Togo': 49, 'Cameroun': 24, 'Ouganda': 19, 'Kenya': 25,
    'Rwanda': 34, 'Tanzanie': 19, 'Zambie': 11, 'Namibie': 23, 'Afrique du Sud': 11,
    'Eswatini': 23, 'Zimbabwe': 9, 'Mozambique': 10, 'Madagascar': 10, 'Maurice': 39
}

# Création du DataFrame
donnees = {
    'Pays': list(acces_electricite_rural.keys()),
    'Accès à l\'électricité en milieu rural (%)': list(acces_electricite_rural.values()),
    'Part des IPPs (%)': list(part_IPP.values())
}
df = pd.DataFrame(donnees)

# Tracé du graphique
plt.figure(figsize=(14, 8))
plt.scatter(df['Part des IPPs (%)'], df['Accès à l\'électricité en milieu rural (%)'], color='blue', marker='x')

# Annoter chaque point avec le nom du pays
for i, row in df.iterrows():
    plt.annotate(row['Pays'], (row['Part des IPPs (%)'], row['Accès à l\'électricité en milieu rural (%)']),
                 textcoords="offset points", xytext=(0,10), ha='center')

plt.xlabel('Part des IPPs (%)')
plt.ylabel('Accès à l\'électricité en milieu rural (%)')
plt.title('Taux d\'accès à l\'électricité en milieu rural en fonction de la part des IPPs')
plt.grid(True)
plt.show()

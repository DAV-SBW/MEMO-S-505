import matplotlib.pyplot as plt
import numpy as np

# Données d'accès à l'électricité
acces_electricite_rural = {
    'Tanzanie': 22.0, 'Chad': 1.6, 'Togo': 24.3, 'Lesotho': 35.2, 'Liberia': 8.1,
    'Sierra Leone': 4.7, 'Senegal': 38.6, 'Sao Tome and Principe': 71.0, 'Comores': 80.1,
    'Congo, Dem. Rep.': 1.0, 'Central African Republic': 1.9, 'Congo, Rep.': 11.8, 'Cameroon': 24.2,
    'Cote d\'Ivoire': 43.7, 'Nigeria': 24.6, 'Niger': 9.7, 'Gabon': 24.7, 'Mozambique': 4.6,
    'Kenya': 62.7, 'Rwanda': 34.9, 'Zambia': 14.0, 'Zimbabwe': 37.1, 'Botswana': 26.2,
    'Burundi': 0.9, 'Ethiopia': 39.4, 'Guinea': 19.3, 'Malawi': 3.5, 'Mali': 16.8, 'Mauritania': 0.8,
    'South Sudan': 5.4, 'Uganda': 32.8
}

acces_electricite_urbain = {
    'Botswana': 71.1, 'République du Congo': 67.5, 'Lesotho': 83.6, 'Madagascar': 71.6, 'Malawi': 54.0,
    'Mozambique': 79.4, 'Namibie': 74.8, 'Niger': 66.1, 'Rwanda': 98.0, 'Tanzanie': 74.7,
    'Comores': 100.0, 'Gabon': 98.5, 'Libéria': 53.7, 'Mauritanie': 91.6, 'Nigéria': 89.0,
    'Eswatini': 86.1, 'Afrique Du Sud': 87.1, 'Cap-Vert': 95.3, 'Côte d\'Ivoire': 95.0, 'Ouganda': 72.0,
    'Tchad': 46.3, 'Bénin': 71.1, 'Burkina Faso': 60.5, 'Cameroun': 94.0, 'Ghana': 95.0,
    'Zambie': 87.0, 'Zimbabwe': 89.0, 'Burundi': 64.0, 'Guinée': 91.0, 'Kenya': 98.0,
    'Sao Tomé-et-Principe': 80.0, 'Sénégal': 96.6, 'Sierra Leone': 55.3, 'Mali': 99.7,
    'Gambie': 82.8, 'Togo': 96.5, 'Seychelles': 100.0, 'Éthiopie': 94.0, 'Maurice': 99.0,
    'RD Congo': 45.3
}

# Nouvelles données de PIB par habitant (en USD)
pib_habitant = {
    'Seychelles': 16715, 'Île Maurice': 11319, 'Libye': 9861, 'Botswana': 6708, 'Gabon': 6655,
    'Afrique Du Sud': 6006, 'Guinée Équatoriale': 5506, 'Algérie': 4717, 'Namibie': 4512,
    'Égypte': 4178, 'Swaziland': 4175, 'Tunisie': 3902, 'Cap-Vert': 3700, 'Maroc': 3371,
    'Côte d\'Ivoire': 2493, 'Nigeria': 2460, 'Angola': 2334, 'Ghana': 2066, 'Kenya': 1814,
    'République Du Congo': 1698, 'Mauritanie': 1628, 'Sénégal': 1476, 'Cameroun': 1461,
    'Zimbabwe': 1383, 'Comores': 1374, 'Sao Tomé-Et-Principe': 1362, 'Zambie': 1347, 'Bénin': 1300,
    'Tanzanie': 1081, 'Guinée': 1040, 'Rwanda': 994, 'Ouganda': 956, 'Lesotho': 951, 'Togo': 922,
    'Ethiopie': 890, 'Soudan': 879, 'Mali': 763, 'Guinée-Bissau': 752, 'Burkina-Faso': 739,
    'Gambie': 708, 'Libérie': 662, 'Sierra-Leone': 635, 'Mozambique': 603, 'Tchad': 599,
    'Congo': 556, 'Malawi': 549, 'Niger': 541, 'Madagascar': 461, 'République Centrafricaine': 357,
    'Burundi': 262
}

# Extraire les données communes
common_countries = set(acces_electricite_rural.keys()) & set(acces_electricite_urbain.keys()) & set(pib_habitant.keys())

# Ajouter les Seychelles
acces_electricite_rural['Seychelles'] = 100.0
acces_electricite_urbain['Seychelles'] = 100.0
common_countries.add('Seychelles')

# Préparer les données pour la régression
x = []
y_rural = []
y_urbain = []
countries = []

for country in common_countries:
    x.append(pib_habitant[country])
    y_rural.append(acces_electricite_rural[country])
    y_urbain.append(acces_electricite_urbain[country])
    countries.append(country)

# Convertir en numpy array
x = np.array(x)
y_rural = np.array(y_rural)
y_urbain = np.array(y_urbain)

# Droite de régression pour les zones rurales
coef_rural = np.polyfit(x, y_rural, 1)
poly1d_fn_rural = np.poly1d(coef_rural)

# Droite de régression pour les zones urbaines
coef_urbain = np.polyfit(x, y_urbain, 1)
poly1d_fn_urbain = np.poly1d(coef_urbain)

# Tracer les données et les droites de régression
plt.figure(figsize=(14, 7))

plt.scatter(x, y_rural, color='blue', label='Rural', marker='x')
plt.plot(x, poly1d_fn_rural(x), '--b', label='Régression Rural')

plt.scatter(x, y_urbain, color='red', label='Urbain', marker='x')
plt.plot(x, poly1d_fn_urbain(x), '--r', label='Régression Urbain')

for i, country in enumerate(countries):
    plt.annotate(country, (x[i], y_rural[i]), fontsize=8, color='blue', alpha=0.7)
    plt.annotate(country, (x[i], y_urbain[i]), fontsize=8, color='red', alpha=0.7)

plt.xlabel('PIB par habitant (USD)')
plt.ylabel('Accès à l\'électricité (%)')
plt.title('Accès à l\'électricité en milieu rural et urbain par rapport au PIB par habitant')
plt.legend()
plt.grid(True)
plt.show()

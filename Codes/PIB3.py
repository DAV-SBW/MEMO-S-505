# Filtrer les pays avec PIB > 4000 USD
filtered_countries = {country: pib for country, pib in pib_habitant.items() if 1000 <= pib < 4000}
common_countries = set(acces_electricite_rural.keys()) & set(acces_electricite_urbain.keys()) & set(filtered_countries.keys())

# Préparer les données pour la régression
x = []
y_rural = []
y_urbain = []
countries = []

for country in common_countries:
    x.append(filtered_countries[country])
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
r2_rural = r2_score(y_rural, poly1d_fn_rural(x))

# Droite de régression pour les zones urbaines
coef_urbain = np.polyfit(x, y_urbain, 1)
poly1d_fn_urbain = np.poly1d(coef_urbain)
r2_urbain = r2_score(y_urbain, poly1d_fn_urbain(x))

# Tracer les données et les droites de régression
plt.figure(figsize=(14, 7))

plt.scatter(x, y_rural, color='blue', label='Rural', marker='x')
plt.plot(x, poly1d_fn_rural(x), '--b', label=f'Rural: pente={coef_rural[0]:.2f}, R²={r2_rural:.2f}')

plt.scatter(x, y_urbain, color='red', label='Urbain', marker='x')
plt.plot(x, poly1d_fn_urbain(x), '--r', label=f'Urbain: pente={coef_urbain[0]:.2f}, R²={r2_urbain:.2f}')

for i, country in enumerate(countries):
    plt.annotate(country, (x[i], y_rural[i]), fontsize=8, color='blue', alpha=0.7)
    plt.annotate(country, (x[i], y_urbain[i]), fontsize=8, color='red', alpha=0.7)

plt.xlabel('PIB par habitant (USD)')
plt.ylabel('Accès à l\'électricité (%)')
plt.title('Accès à l\'électricité en milieu rural et urbain par rapport au PIB par habitant')
plt.legend()
plt.grid(True)
plt.show()

# Afficher le nombre de pays inclus
len(common_countries)

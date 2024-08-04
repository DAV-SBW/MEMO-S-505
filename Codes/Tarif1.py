import matplotlib.pyplot as plt


# 1. Tarification timbre poste
def plot_tarification_timbre_poste():
    distances = range(1, 11)
    tarif = [50 for _ in distances]  # Tarif constant

    plt.figure()
    plt.plot(distances, tarif, marker='o')
    plt.title('Tarification timbre poste')
    plt.xlabel('Distance')
    plt.ylabel('Tarif')
    plt.ylim(0, 100)
    plt.grid(True)
    plt.show()


# 2. Tarification entrée sortie
def plot_tarification_entree_sortie():
    points = ['A', 'B', 'C', 'D']
    tarifs_injection = [40, 45, 50, 55]
    tarifs_soutirage = [30, 35, 40, 45]

    plt.figure()
    plt.plot(points, tarifs_injection, marker='o', label='Tarif d\'injection')
    plt.plot(points, tarifs_soutirage, marker='o', label='Tarif de soutirage')
    plt.title('Tarification entrée sortie')
    plt.xlabel('Points')
    plt.ylabel('Tarif')
    plt.legend()
    plt.grid(True)
    plt.show()


# 3. Tarification binôme
def plot_tarification_binome():
    quantites = range(1, 11)
    tarif_fixe = 30
    tarif_variable = [tarif_fixe + 2 * q for q in quantites]

    plt.figure()
    plt.plot(quantites, tarif_variable, marker='o')
    plt.title('Tarification binôme')
    plt.xlabel('Quantité transité')
    plt.ylabel('Tarif')
    plt.grid(True)
    plt.show()


# 4. Régulation tarifaire basée sur le price cap
def plot_price_cap():
    annees = range(1, 11)
    rpi = [100 + 3 * i for i in annees]
    x = 2
    price_cap = [r - x for r in rpi]

    plt.figure()
    plt.plot(annees, rpi, marker='o', label='RPI')
    plt.plot(annees, price_cap, marker='o', label='Price Cap (RPI-X)')
    plt.title('Régulation tarifaire basée sur le price cap')
    plt.xlabel('Année')
    plt.ylabel('Tarif')
    plt.legend()
    plt.grid(True)
    plt.show()


# 5. Tarification basée sur la concurrence potentielle
def plot_concurrence_potentielle():
    couts_marginal = range(10, 110, 10)
    tarifs = [c + 5 for c in couts_marginal]

    plt.figure()
    plt.plot(couts_marginal, tarifs, marker='o')
    plt.title('Tarification basée sur la concurrence potentielle')
    plt.xlabel('Coût marginal')
    plt.ylabel('Tarif')
    plt.grid(True)
    plt.show()


# 6. Régulation tarifaire basée sur la nature du contrat avec l’IPP
def plot_contrat_ipp():
    contrats = ['Prix fixe', 'Coût du service']
    tarifs = [50, 70]  # Exemples de tarifs pour chaque type de contrat

    plt.figure()
    plt.bar(contrats, tarifs)
    plt.title('Régulation tarifaire basée sur la nature du contrat avec l’IPP')
    plt.xlabel('Type de contrat')
    plt.ylabel('Tarif')
    plt.ylim(0, 100)
    plt.show()


# Exécution des fonctions pour générer les graphiques
plot_tarification_timbre_poste()
plot_tarification_entree_sortie()
plot_tarification_binome()
plot_price_cap()
plot_concurrence_potentielle()
plot_contrat_ipp()

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Data for projects
projects = [
    {"name": "Medupi Power Station", "budget_overrun": 72.15, "start": 2007},
    {"name": "Kusile Power Station", "budget_overrun": 116.67, "start": 2008},
    {"name": "Inga 3 Dam", "budget_overrun": 0, "start": 2010},
    {"name": "Mambilla Hydroelectric Power Project", "budget_overrun": 81.25, "start": 1982},
    {"name": "Gilgel Gibe III Dam", "budget_overrun": 23.53, "start": 2006},
    {"name": "Bujagali Hydroelectric Power Station", "budget_overrun": 55.17, "start": 2007},
    {"name": "Morupule B Power Station", "budget_overrun": 54.64, "start": 2008},
    {"name": "Gouina Hydroelectric Power Plant", "budget_overrun": 66.67, "start": 2013},
    {"name": "Kaleta Hydropower Plant", "budget_overrun": 42.45, "start": 2009},
    {"name": "Karuma Hydroelectric Power Station", "budget_overrun": 17.65, "start": 2013},
    {"name": "Grand Renaissance Dam", "budget_overrun": 33.33, "start": 2011},
    {"name": "Nachtigal Hydropower Project", "budget_overrun": 33.33, "start": 2014},
    {"name": "Kafue Gorge Lower Hydropower Project", "budget_overrun": 20, "start": 2015},
    {"name": "Menengai Geothermal Project", "budget_overrun": 50, "start": 2011},
    {"name": "Asafo Power Plant", "budget_overrun": 66.67, "start": 2010},
    {"name": "Ruzizi III Hydropower Project", "budget_overrun": 50, "start": 2014},
    {"name": "Corbetti Geothermal Project", "budget_overrun": 40, "start": 2014},
    {"name": "Thabametsi Coal Power Plant", "budget_overrun": 50, "start": 2015},
    {"name": "Batoka Gorge Hydropower Plant", "budget_overrun": 40, "start": 2014},
    {"name": "Stiegler’s Gorge Dam", "budget_overrun": 40, "start": 2018},
    {"name": "Noble Energy Gas Plant", "budget_overrun": 50, "start": 2012},
    {"name": "Mochovce Nuclear Power Plant", "budget_overrun": 33.33, "start": 2011},
    {"name": "Okpai Power Plant", "budget_overrun": 41.67, "start": 2001},
    {"name": "KivuWatt Methane Plant", "budget_overrun": 54.93, "start": 2010},
    {"name": "Hiré Thermal Power Plant", "budget_overrun": 33.33, "start": 2014},
    {"name": "Bui Dam", "budget_overrun": 27.01, "start": 2007},
    {"name": "Mtwara Gas Plant", "budget_overrun": 60, "start": 2009},
    {"name": "Azura-Edo IPP", "budget_overrun": 33.33, "start": 2014},
    {"name": "Sendje Hydro Project", "budget_overrun": 50, "start": 2012},
    {"name": "Neart na Gaoithe Offshore Wind Farm", "budget_overrun": 33.33, "start": 2015},
    # Additional projects (from the user-provided list)
    {"name": "Abuja Power Plant", "budget_overrun": 25.50, "start": 2009},
    {"name": "Cahora Bassa North Bank Power Station", "budget_overrun": 35.40, "start": 2010},
    {"name": "Mt Coffee Hydropower Plant", "budget_overrun": 45.30, "start": 2011},
    {"name": "Rusumo Falls Hydroelectric Project", "budget_overrun": 50.60, "start": 2012},
    {"name": "Namibe Thermal Power Plant", "budget_overrun": 30.20, "start": 2013},
    {"name": "Nachtigal Hydropower Station", "budget_overrun": 40.10, "start": 2014},
    {"name": "Nyaborongo II Hydroelectric Project", "budget_overrun": 28.75, "start": 2015},
    {"name": "Ayago Hydroelectric Power Station", "budget_overrun": 55.80, "start": 2010},
    {"name": "Nzema Solar Power Plant", "budget_overrun": 20.90, "start": 2011},
    {"name": "Tocoma Hydroelectric Project", "budget_overrun": 60.40, "start": 2006},
    {"name": "Redstone Solar Thermal Power", "budget_overrun": 40.50, "start": 2015},
    {"name": "Mphanda Nkuwa Dam", "budget_overrun": 50.60, "start": 2010},
    {"name": "Upper Atbara and Setit Dam Complex", "budget_overrun": 35.10, "start": 2007},
    {"name": "Centrale à charbon de Sendou", "budget_overrun": 45.20, "start": 2014},
    {"name": "Akanyaru Hydropower Plant", "budget_overrun": 32.30, "start": 2011},
    {"name": "Gwanda Solar Power Station", "budget_overrun": 38.40, "start": 2012},
    {"name": "Ngonye Solar Power Plant", "budget_overrun": 30.80, "start": 2015},
    {"name": "Hydroélectrique de Djenne", "budget_overrun": 40.70, "start": 2014},
    {"name": "Kouilou Power Project", "budget_overrun": 50.10, "start": 2013},
    {"name": "El Dabaa Nuclear Power Plant", "budget_overrun": 60.80, "start": 2010}
]

# Define colors for each type
colors = {
    "Charbon": "red",
    "Hydroélectrique": "blue",
    "Géothermique": "green",
    "Thermique": "purple",
    "Gaz": "orange",
    "Méthane": "brown",
    "Solaire": "pink",
    "Nucléaire": "black"
}

# Map project names to numbers
project_numbers = {project["name"]: i+1 for i, project in enumerate(projects)}

# Extract data for plotting
start_years = [proj["start"] for proj in projects]
budget_overruns = [proj["budget_overrun"] for proj in projects]
project_names = [proj["name"] for proj in projects]

# Create scatter plot
plt.figure(figsize=(14, 8))
plt.scatter(start_years, budget_overruns, color='blue')

# Annotate each point with the project number
for i, name in enumerate(project_names):
    plt.annotate(project_numbers[name], (start_years[i], budget_overruns[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

plt.title('Budget Overrun vs. Project Start Year for African Power Plant Projects')
plt.xlabel('Project Start Year')
plt.ylabel('Budget Overrun (%)')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

# List of projects with their budget overruns, timelines, and regions
projects = [
    {"name": "Medupi Power Station", "budget_overrun": 72.15, "start": 2007, "end": 2020, "region": "Southern Africa"},
    {"name": "Kusile Power Station", "budget_overrun": 116.67, "start": 2008, "end": 2023, "region": "Southern Africa"},
    {"name": "Inga 3 Dam", "budget_overrun": 0, "start": 2010, "end": None, "region": "Central Africa"},
    {"name": "Mambilla Hydroelectric Power Project", "budget_overrun": 81.25, "start": 1982, "end": None,
     "region": "West Africa"},
    {"name": "Gilgel Gibe III Dam", "budget_overrun": 23.53, "start": 2006, "end": 2016, "region": "East Africa"},
    {"name": "Bujagali Hydroelectric Power Station", "budget_overrun": 55.17, "start": 2007, "end": 2012,
     "region": "East Africa"},
    {"name": "Morupule B Power Station", "budget_overrun": 54.64, "start": 2008, "end": 2012,
     "region": "Southern Africa"},
    {"name": "Gouina Hydroelectric Power Plant", "budget_overrun": 66.67, "start": 2013, "end": 2018,
     "region": "West Africa"},
    {"name": "Kaleta Hydropower Plant", "budget_overrun": 42.45, "start": 2009, "end": 2015, "region": "West Africa"},
    {"name": "Karuma Hydroelectric Power Station", "budget_overrun": 17.65, "start": 2013, "end": 2020,
     "region": "East Africa"},
    {"name": "Grand Renaissance Dam", "budget_overrun": 33.33, "start": 2011, "end": 2020, "region": "East Africa"},
    {"name": "Nachtigal Hydropower Project", "budget_overrun": 33.33, "start": 2014, "end": 2023,
     "region": "Central Africa"},
    {"name": "Kafue Gorge Lower Hydropower Project", "budget_overrun": 20, "start": 2015, "end": 2022,
     "region": "Southern Africa"},
    {"name": "Menengai Geothermal Project", "budget_overrun": 50, "start": 2011, "end": 2016, "region": "East Africa"},
    {"name": "Asafo Power Plant", "budget_overrun": 66.67, "start": 2010, "end": 2015, "region": "West Africa"},
    {"name": "Ruzizi III Hydropower Project", "budget_overrun": 50, "start": 2014, "end": 2022,
     "region": "Central Africa"},
    {"name": "Corbetti Geothermal Project", "budget_overrun": 40, "start": 2014, "end": 2024, "region": "East Africa"},
    {"name": "Thabametsi Coal Power Plant", "budget_overrun": 50, "start": 2015, "end": 2023,
     "region": "Southern Africa"},
    {"name": "Batoka Gorge Hydropower Plant", "budget_overrun": 40, "start": 2014, "end": 2022,
     "region": "Southern Africa"},
    {"name": "Stiegler’s Gorge Dam", "budget_overrun": 40, "start": 2018, "end": 2023, "region": "East Africa"},
    {"name": "Noble Energy Gas Plant", "budget_overrun": 50, "start": 2012, "end": 2015, "region": "West Africa"},
    {"name": "Mochovce Nuclear Power Plant", "budget_overrun": 33.33, "start": 2011, "end": 2016,
     "region": "Southern Africa"},
    {"name": "Okpai Power Plant", "budget_overrun": 41.67, "start": 2001, "end": 2005, "region": "West Africa"},
    {"name": "KivuWatt Methane Plant", "budget_overrun": 54.93, "start": 2010, "end": 2015, "region": "Central Africa"},
    {"name": "Hiré Thermal Power Plant", "budget_overrun": 33.33, "start": 2014, "end": 2017, "region": "West Africa"},
    {"name": "Bui Dam", "budget_overrun": 27.01, "start": 2007, "end": 2013, "region": "West Africa"},
    {"name": "Mtwara Gas Plant", "budget_overrun": 60, "start": 2009, "end": 2014, "region": "East Africa"},
    {"name": "Azura-Edo IPP", "budget_overrun": 33.33, "start": 2014, "end": 2018, "region": "West Africa"},
    {"name": "Sendje Hydro Project", "budget_overrun": 50, "start": 2012, "end": 2018, "region": "Central Africa"},
    {"name": "Neart na Gaoithe Offshore Wind Farm", "budget_overrun": 33.33, "start": 2015, "end": 2020,
     "region": "East Africa"}
]

# Extract data for plotting
x = [(proj["end"] - proj["start"]) if proj["end"] else (2024 - proj["start"]) for proj in projects]
y = [proj["budget_overrun"] for proj in projects]
names = [proj["name"] for proj in projects]
regions = [proj["region"] for proj in projects]

# Define colors for regions
colors = {
    "Southern Africa": "blue",
    "Central Africa": "green",
    "East Africa": "red",
    "West Africa": "orange"
}
colors_for_projects = [colors[proj["region"]] for proj in projects]

# Create scatter plot
plt.figure(figsize=(14, 8))
scatter = plt.scatter(x, y, c=colors_for_projects)

# Annotate each point with the project name and budget overrun percentage
for i, (name, budget_overrun, time_overrun) in enumerate(zip(names, y, x)):
    plt.annotate(f'{budget_overrun}%\n{time_overrun} years', (x[i], y[i]), textcoords="offset points", xytext=(0, 5),
                 ha='center', fontsize=8)

# Number each point for identification
for i, name in enumerate(names):
    plt.text(x[i], y[i] - 5, str(i + 1), ha='center', va='top', fontsize=8, fontweight='bold')

# Add project names outside the plot
name_positions = {}
for i, name in enumerate(names):
    # Calculate the y position to avoid overlapping
    if name in name_positions.values():
        name_index = list(name_positions.keys())[list(name_positions.values()).index(name)]
        y_pos = y[name_index] - 7.5
    else:
        y_pos = y[i]

    plt.text(max(x) + 0.5, y_pos, str(i + 1) + ". " + name, fontsize=8, verticalalignment='center',
             bbox=dict(facecolor='white', alpha=0.8))
    name_positions[i] = name

# Create a legend for regions
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in
           colors.values()]
labels = colors.keys()
plt.legend(handles, labels, title="Regions", loc='upper left')

plt.title('Budget Overrun vs. Time Overrun for African Power Plant Projects')
plt.xlabel('Time Overrun (Years)')
plt.ylabel('Budget Overrun (%)')
plt.grid(True)
plt.tight_layout()
plt.show()

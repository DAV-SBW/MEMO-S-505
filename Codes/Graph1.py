import matplotlib.pyplot as plt

# List of projects with their budget overruns and timelines
projects = [
    {"name": "Medupi Power Station", "budget_overrun": 72.15, "start": 2007, "end": 2020},
    {"name": "Kusile Power Station", "budget_overrun": 116.67, "start": 2008, "end": 2023},
    {"name": "Inga 3 Dam", "budget_overrun": 0, "start": 2010, "end": None},
    {"name": "Mambilla Hydroelectric Power Project", "budget_overrun": 81.25, "start": 1982, "end": None},
    {"name": "Gilgel Gibe III Dam", "budget_overrun": 23.53, "start": 2006, "end": 2016},
    {"name": "Bujagali Hydroelectric Power Station", "budget_overrun": 55.17, "start": 2007, "end": 2012},
    {"name": "Morupule B Power Station", "budget_overrun": 54.64, "start": 2008, "end": 2012},
    {"name": "Gouina Hydroelectric Power Plant", "budget_overrun": 66.67, "start": 2013, "end": 2018},
    {"name": "Kaleta Hydropower Plant", "budget_overrun": 42.45, "start": 2009, "end": 2015},
    {"name": "Karuma Hydroelectric Power Station", "budget_overrun": 17.65, "start": 2013, "end": 2020},
    {"name": "Grand Renaissance Dam", "budget_overrun": 33.33, "start": 2011, "end": 2020},
    {"name": "Nachtigal Hydropower Project", "budget_overrun": 33.33, "start": 2014, "end": 2023},
    {"name": "Kafue Gorge Lower Hydropower Project", "budget_overrun": 20, "start": 2015, "end": 2022},
    {"name": "Menengai Geothermal Project", "budget_overrun": 50, "start": 2011, "end": 2016},
    {"name": "Asafo Power Plant", "budget_overrun": 66.67, "start": 2010, "end": 2015},
    {"name": "Ruzizi III Hydropower Project", "budget_overrun": 50, "start": 2014, "end": 2022},
    {"name": "Corbetti Geothermal Project", "budget_overrun": 40, "start": 2014, "end": 2024},
    {"name": "Thabametsi Coal Power Plant", "budget_overrun": 50, "start": 2015, "end": 2023},
    {"name": "Batoka Gorge Hydropower Plant", "budget_overrun": 40, "start": 2014, "end": 2022},
    {"name": "Stiegler’s Gorge Dam", "budget_overrun": 40, "start": 2018, "end": 2023},
    {"name": "Noble Energy Gas Plant", "budget_overrun": 50, "start": 2012, "end": 2015},
    {"name": "Mochovce Nuclear Power Plant", "budget_overrun": 33.33, "start": 2011, "end": 2016},
    {"name": "Okpai Power Plant", "budget_overrun": 41.67, "start": 2001, "end": 2005},
    {"name": "KivuWatt Methane Plant", "budget_overrun": 54.93, "start": 2010, "end": 2015},
    {"name": "Hiré Thermal Power Plant", "budget_overrun": 33.33, "start": 2014, "end": 2017},
    {"name": "Bui Dam", "budget_overrun": 27.01, "start": 2007, "end": 2013},
    {"name": "Mtwara Gas Plant", "budget_overrun": 60, "start": 2009, "end": 2014},
    {"name": "Azura-Edo IPP", "budget_overrun": 33.33, "start": 2014, "end": 2018},
    {"name": "Sendje Hydro Project", "budget_overrun": 50, "start": 2012, "end": 2018},
    {"name": "Neart na Gaoithe Offshore Wind Farm", "budget_overrun": 33.33, "start": 2015, "end": 2020}
]

# Extract data for plotting
x = [(proj["end"] - proj["start"]) if proj["end"] else (2024 - proj["start"]) for proj in projects]
y = [proj["budget_overrun"] for proj in projects]
names = [proj["name"] for proj in projects]

# Create scatter plot
plt.figure(figsize=(14, 8))
plt.scatter(x, y, color='blue')

# Annotate each point with the project name
for i, name in enumerate(names):
    plt.annotate(name, (x[i], y[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

plt.title('Budget Overrun vs. Time Overrun for African Power Plant Projects')
plt.xlabel('Time Overrun (Years)')
plt.ylabel('Budget Overrun (%)')
plt.grid(True)
plt.show()

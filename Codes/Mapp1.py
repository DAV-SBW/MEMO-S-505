import pandas as pd
import matplotlib.pyplot as plt

# Data for electricity access in rural areas (2022) - Mock data for the sake of this example
electricity_access_rural = {
    'Botswana': 25.0, 'Republic of Congo': 12.4, 'Lesotho': 37.7, 'Madagascar': 10.9, 'Malawi': 5.6,
    'Mozambique': 5.0, 'Namibia': 33.2, 'Niger': 7.7, 'Rwanda': 38.2, 'Tanzania': 36.0,
    'Comoros': 82.9, 'Gabon': 29.0, 'Liberia': 14.9, 'Mauritania': 0.8, 'Nigeria': 27.0,
    'Swaziland': 81.6, 'South Africa': 93.4, 'Cape Verde': 96.9, 'Ivory Coast': 45.3, 'Uganda': 35.9,
    'Chad': 1.3, 'Benin': 45.5, 'Burkina Faso': 3.4, 'Cameroon': 25.0, 'Ghana': 71.6,
    'Zambia': 14.5, 'Zimbabwe': 33.7, 'Burundi': 1.7, 'Guinea': 21.3, 'Kenya': 65.6,
    'Sao Tome and Principe': 73.7, 'Senegal': 43.4, 'Sierra Leone': 5.0, 'Mali': 18.3,
    'Gambia': 31.2, 'Togo': 25.0, 'Seychelles': 100.0, 'Ethiopia': 43.0, 'Mauritius': 100.0,
    'DR Congo': 1.0
}

# Data for number of consumption blocks according to Briceño-Garmendia & Shkaratan (2011)
consumption_blocks = {
    'Botswana': 1, 'Republic of Congo': 1, 'Lesotho': 1, 'Madagascar': 1, 'Malawi': 1,
    'Mozambique': 1, 'Namibia': 1, 'Niger': 1, 'Rwanda': 1, 'Tanzania': 1,
    'Comoros': 1, 'Gabon': 1, 'Liberia': 1, 'Mauritania': 1, 'Nigeria': 1,
    'Swaziland': 1, 'South Africa': 2, 'Cape Verde': 2, 'Ivory Coast': 2, 'Uganda': 2,
    'Chad': 3, 'Benin': 3, 'Burkina Faso': 3, 'Cameroon': 3, 'Ghana': 3,
    'Zambia': 3, 'Zimbabwe': 3, 'Burundi': 3, 'Guinea': 3, 'Kenya': 4,
    'Sao Tome and Principe': 3, 'Senegal': 3, 'Sierra Leone': 3, 'Mali': 4,
    'Gambia': 4, 'Togo': 4, 'Seychelles': 5, 'Ethiopia': 7, 'Mauritius': 8,
    'DR Congo': 11
}

# Combine data into a DataFrame
data = {
    'Country': list(electricity_access_rural.keys()),
    'Rural Electricity Access (%)': list(electricity_access_rural.values()),
    'Consumption Blocks': [consumption_blocks[country] for country in electricity_access_rural.keys()]
}
df = pd.DataFrame(data)

# Plotting the data
plt.figure(figsize=(14, 8))
for i, row in df.iterrows():
    plt.scatter(row['Consumption Blocks'], row['Rural Electricity Access (%)'], label=row['Country'])

plt.xlabel('Number of Consumption Blocks')
plt.ylabel('Rural Electricity Access (%)')
plt.title('Rural Electricity Access vs. Number of Consumption Blocks')
plt.grid(True)

# Annotate each point with the country name
for i, row in df.iterrows():
    plt.annotate(row['Country'], (row['Consumption Blocks'], row['Rural Electricity Access (%)']),
                 textcoords="offset points", xytext=(0,10), ha='center')

# Save plot to file
plt.savefig("electricity_access_vs_consumption_blocks.png")

# Show the plot
plt.show()


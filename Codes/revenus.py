import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data extracted from the graph
data = {
    'Country': ['Gabon', 'South Africa', 'Ghana', 'Cote d\'Ivoire', 'Senegal', 'Mali', 'Angola', 'Tanzania', 'Kenya', 'Mozambique', 'Namibia', 'Malawi', 'Burkina Faso', 'Niger', 'Nigeria', 'Cameroon', 'Uganda', 'Ethiopia', 'Sudan', 'Zimbabwe', 'Liberia', 'RDC', 'Central African Republic', 'Madagascar', 'Tchad', 'Burundi', 'Rwanda', 'Lesotho'],
    'Access (%)': [88, 85, 85, 75, 75, 75, 45, 25, 20, 18, 50, 35, 30, 15, 40, 50, 15, 45, 40, 10, 3, 5, 2, 6, 1, 1, 15, 25],
    'Income (%)': [4, 5, 5, 6, 6, 6, 5, 5, 6, 7, 5, 6, 5, 6, 10, 8, 9, 8, 10, 12, 16, 14, 14, 12, 15, 13, 9, 8]
}

df = pd.DataFrame(data)

# Plotting the data
plt.figure(figsize=(14, 8))
plt.scatter(df['Income (%)'], df['Access (%)'], color='blue', label='Countries')

# Annotate each point with the country name
for i, row in df.iterrows():
    plt.annotate(row['Country'], (row['Income (%)'], row['Access (%)']), textcoords="offset points", xytext=(0,10), ha='center')

# Regression line
X = df['Income (%)']
Y = df['Access (%)']
m, b = np.polyfit(X, Y, 1)
plt.plot(X, m*X + b, color='red', linestyle='--', linewidth=1)

# Calculate R²
Y_pred = m*X + b
ss_res = np.sum((Y - Y_pred) ** 2)
ss_tot = np.sum((Y - np.mean(Y)) ** 2)
r2 = 1 - (ss_res / ss_tot)

# Adding title and labels
plt.title(f'Taux d\'accès à l\'électricité vs Part du revenu consacré à l\'électricité (R² = {r2:.2f})')
plt.xlabel('Part du revenu consacré à l\'électricité (%)')
plt.ylabel('Taux d\'accès à l\'électricité (%)')
plt.grid(True)
plt.legend()

# Display the plot
plt.show()

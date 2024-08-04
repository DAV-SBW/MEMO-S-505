import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data for all African countries (fictional values for illustration)
data = {
    'Country': [
        'Gabon', 'South Africa', 'Ghana', 'Cote d\'Ivoire', 'Senegal', 'Mali', 'Angola', 'Tanzania',
        'Kenya', 'Mozambique', 'Namibia', 'Malawi', 'Burkina Faso', 'Niger', 'Nigeria', 'Cameroon',
        'Uganda', 'Ethiopia', 'Sudan', 'Zimbabwe', 'Liberia', 'RDC', 'Central African Republic',
        'Madagascar', 'Tchad', 'Burundi', 'Rwanda', 'Lesotho', 'Botswana', 'Comoros', 'Congo',
        'Djibouti', 'Egypt', 'Eswatini', 'Gambia', 'Guinea', 'Mauritania', 'Morocco', 'Sao Tome',
        'Seychelles', 'Sierra Leone', 'Somalia', 'South Sudan', 'Tunisia', 'Zambia', 'Algeria',
        'Benin', 'Cape Verde', 'Eritrea', 'Libya', 'Mauritius', 'Nigeria', 'Senegal'
    ],
    'Access (%)': [
        88, 85, 85, 75, 75, 75, 45, 25, 20, 18, 50, 35, 30, 15, 40, 50, 15, 45, 40, 10, 3, 5, 2, 6,
        1, 1, 15, 25, 26.2, 80.1, 11.8, 35.8, 100.0, 76.1, 31.0, 19.3, 0.8, 100.0, 71.0, 100.0, 4.7,
        32.3, 5.4, 99.7, 14.0, 99.1, 17.4, 92.7, 34.1, 0.8, 99.5, 60.5, 96.6
    ],
    'Income (%)': [
        4, 5, 5, 6, 6, 6, 5, 5, 6, 7, 5, 6, 5, 6, 10, 8, 9, 8, 10, 12, 16, 14, 14, 12, 15, 13, 9, 8,
        4.5, 9.2, 5.8, 6.1, 7.0, 5.5, 8.3, 7.1, 6.5, 4.0, 9.7, 5.5, 6.9, 10.2, 8.1, 7.8, 4.3, 6.2,
        6.4, 5.2, 5.0, 5.9, 6.0, 8.8, 9.1
    ]
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

# Save and show the plot
plt.show()

import matplotlib.pyplot as plt

# Reducing the values for better visualization
projects_capacity_data = {
    "Project Number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                       21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                       41, 42, 43, 44, 45, 46, 47],
    "Capacity (MW)": [4800, 4800, 4800, 3050, 1870, 250, 600, 140, 240, 600, 6450, 420, 750, 35, 200, 147, 520, 1200, 2400,
                      2100, 400, 450, 25, 200, 400, 300, 450, 200, 400, 1500, 88, 80, 200, 420, 120, 840, 155, 100, 1500,
                      320, 125, 43, 50, 54, 54, 400, 1000],
    "Investment (MUC)": [13.75, 10.44, 8.51, 5.79, 1.85, 0.90, 1.60,
                         1.21, 1.26, 2.25, 4.82, 1.57, 2.03, 0.51, 0.46,
                         0.48, 0.51, 2.07, 3.05, 2.98, 0.51, 1.23, 0.24,
                         0.35, 0.78, 0.34, 0.88, 0.63, 1.15, 1.57, 0.35,
                         0.47, 0.27, 1.28, 0.36, 1.57, 0.40, 0.76, 2.46,
                         1.27, 0.95, 0.27, 0.35, 0.40, 0.50, 0.61, 8.07]
}

# Extract data for plotting
project_numbers = projects_capacity_data["Project Number"]
investments = projects_capacity_data["Investment (MUC)"]
capacities = projects_capacity_data["Capacity (MW)"]

# Create scatter plot with project numbers instead of points
plt.figure(figsize=(14, 8))
for i in range(len(project_numbers)):
    plt.text(capacities[i], investments[i], str(project_numbers[i]), fontsize=9, ha='center')

plt.title('Investments in MUC vs. Production Capacity in MW for Power Plant Projects')
plt.xlabel('Production Capacity (MW)')
plt.ylabel('Investment (MUC)')
plt.grid(True)
plt.show()
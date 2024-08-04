import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.arima.model import ARIMA

# Paramètres du modèle ARIMA
mu = 0.21  # Moyenne des prix
phi = 0.9  # Coefficient de réversion à la moyenne

# Génération des données avec un modèle ARMA
np.random.seed(42)
ar = np.array([1, -phi])
ma = np.array([1])
arma_process = ArmaProcess(ar, ma)
simulated_data = arma_process.generate_sample(nsample=100)

# Ajustement du modèle ARIMA
model = ARIMA(simulated_data, order=(1, 0, 0))  # ARIMA(p, d, q)
fit_model = model.fit()

# Simulation des prix avec le modèle ajusté
simulated_prices = fit_model.fittedvalues + mu

# Tracé de l'évolution des prix
plt.figure(figsize=(10, 6))
plt.plot(simulated_prices, color='blue', label='Simulated Prices')
plt.axhline(y=mu, color='red', linestyle='--', label='Mean Price')
plt.xlabel('Time')
plt.ylabel('Price ($/kWh)')
plt.title('Evolution of Prices with Mean Reversion Model')
plt.legend()
plt.grid(True)
plt.show()

import numpy as np
energy_consumption = np.array([15.5, 16.2, 14.8, 18.0])  # kWh/100km
avg_consumption = energy_consumption.mean()
estimated_range = 60 / avg_consumption * 100  # 60 kWh battery

print("Average consumption:", avg_consumption)
print("Estimated range (km):", estimated_range)

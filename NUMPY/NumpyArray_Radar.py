# Simulated radar sensor signals(distance readings) in meters
import numpy as np
distance=np.array([1.2, 3.5, 8.0, 0.9, 12.5, 5.0])

critical_obstacles=distance[distance<1.5]
caution_obstacles=distance[(distance>=1.5) & (distance<=6)]
safe_obstacles=distance[distance>6]

print("Alert: ",critical_obstacles)
print("Caution: ",caution_obstacles)
print("Can Move: ",safe_obstacles)

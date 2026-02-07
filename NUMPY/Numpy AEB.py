# Numpy AEB

import numpy as np

distance = np.array([35.0, 18.0, 9.5, 22.0, 4.0])      # meters
relative_speed = np.array([-5.0, -3.0, -1.2, 2.0, -0.8])  # m/s

# Identify approaching objects
approaching = relative_speed < 0

# Compute TTC only for approaching objects
ttc = np.full_like(distance, np.inf)
ttc[approaching] = distance[approaching] / (-relative_speed[approaching])

# AEB decision
AEB_THRESHOLD = 2.0  # seconds

if np.any(ttc < AEB_THRESHOLD):
    print("AEB ACTIVATED")
    print("Minimum TTC:", np.min(ttc))
else:
    print("No Emergency Braking Required")
    print("All objects safe")
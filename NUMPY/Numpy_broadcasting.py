# Numpy broadcasting
# Vehicle coordination system_Radar points & Sensor offset

import numpy as np
radar_points=np.array([
                       [2.9, 3.5],
                       [3.5, 5.7],
                       [1.5,-0.3],
                       [1.0, 4.2],
                       [8.9, 0.6]
                       ])
sensor_offset=[1.2,0.5]
vehicle_points=radar_points+sensor_offset
print(vehicle_points)
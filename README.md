# Matplotlib & Pandas.

import matplotlib.pyplot as plt                             # Visual analytics for comparing sensor usage patterns
import pandas as pd                                         # Tabular data processing & aggregation

df=pd.read_csv("C:\\Users\\ILANGOVAN\\Documents\\MAP\\PYTHON\\av_sensor_log.csv") # Loading sensor event logs for analysis


sensor_type_count=df["sensor_type"].value_counts()          # Identify which perception sensors generate the highest numbers of events
plt.bar(sensor_type_count.index,sensor_type_count.values)   # For visual compare- sensor utilization frequency

plt.xlabel("Sensor type",color="red")
plt.ylabel("Number of events",color="blue")
plt.title("AV Sensor usage distribution")
plt.tight_layout()
plt.show()


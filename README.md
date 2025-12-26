# Matplotlib & Pandas

import matplotlib.pyplot as plt                             # Importing matplotlib
import pandas as pd                                         # Importing pandas

df=pd.read_csv("C:\\Users\\ILANGOVAN\\Documents\\MAP\\PYTHON\\av_sensor_log.csv") # Importing CSV file



sensor_type_count=df["sensor_type"].value_counts()          # Built-in function
plt.bar(sensor_type_count.index,sensor_type_count.values)

plt.xlabel("Sensor type",color="red")
plt.ylabel("Counts",color="blue")
plt.title("AV Sensor detail")
plt.tight_layout()
plt.show()

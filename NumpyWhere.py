# Numpy Filtering_Where function
import numpy as np
cell_voltage=np.array([[3.1, 3.2, 3.5, 2.5],
                      [3.6, 3.1, 2.9,3.8]])
cell_status=np.where(cell_voltage>=3.1,cell_voltage,"LOW VOLTAGE")

print("Test Report: ",cell_status)
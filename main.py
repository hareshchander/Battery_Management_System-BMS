import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bms_functions import check_battery_status

# Load sample battery data
battery_data = pd.read_csv("data/battery_data.csv")

# Run BMS status check
for index, row in battery_data.iterrows():
    status = check_battery_status(row['voltage'], row['temperature'])
    print(f"Battery Status: {status}")

# Plot battery voltage levels
plt.plot(battery_data['time'], battery_data['voltage'])
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('Battery Voltage Over Time')
plt.show()

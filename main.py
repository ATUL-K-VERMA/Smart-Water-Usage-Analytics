import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Hostel information
hostel_names = ['NC(1,2,3)', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
tank_capacity = [92000, 80000, 76000, 72000, 60000, 54000, 38000, 78000, 86000, 120000, 140000, 360000]
water_usage_per_day = [52000, 48000, 41000, 47000, 38000, 35000, 28000, 59000, 67000, 92000, 120000, 270000]
total_rooms = [90, 70, 72, 72, 63, 45, 34, 72, 75, 144, 75, 220]
total_students = [270, 210, 216, 220, 210, 225, 102, 216, 205, 432, 318, 880]

# Water quality parameters
water_quality_parameters = {
    "pH": (6.5, 8.5),
    "Turbidity": (1, 5),
    "TDS": (500, 2000),
    "Hardness": (200, 600),
    "Iron": (0.3, 0.3),
    "Chlorides": (250, 1000),
    "Residual Chlorine": (0.2, 0.2),
    "Fluoride": (1, 1.5),
    "Sulfate": (200, 400),
    "Nitrates": (45, 45),
    "Chloramines": (4, 4),
    "Alkalinity": (200, 600),
    "Coliform Bacteria": (0, 0)
}

# Generate data for each day from January 1, 2019, to August 3, 2024
start_date = datetime(2019, 1, 1)
end_date = datetime(2024, 8, 3)
num_days = (end_date - start_date).days + 1
dates = [start_date + timedelta(days=i) for i in range(num_days)]

# Function to generate random water quality values
def generate_water_quality():
    return {param: random.uniform(values[0], values[1]) for param, values in water_quality_parameters.items()}

# Function to simulate daily water usage and tank levels
def simulate_water_usage():
    data = []
    for date in dates:
        for i, hostel in enumerate(hostel_names):
            usage = max(0, water_usage_per_day[i] + random.randint(-5000, 5000))
            tank_level = max(0, tank_capacity[i] - usage)
            water_quality = generate_water_quality()
            data.append([
                date, hostel, usage, tank_capacity[i], tank_level, total_rooms[i], total_students[i],
                water_quality['pH'], water_quality['Turbidity'], water_quality['TDS'], water_quality['Hardness'],
                water_quality['Iron'], water_quality['Chlorides'], water_quality['Residual Chlorine'],
                water_quality['Fluoride'], water_quality['Sulfate'], water_quality['Nitrates'],
                water_quality['Chloramines'], water_quality['Alkalinity'], water_quality['Coliform Bacteria']
            ])
            tank_capacity[i] = tank_level  # Update tank capacity for next day
            if tank_capacity[i] < 0.2 * tank_capacity[i]:  # Refill tank if below 20%
                tank_capacity[i] = tank_capacity[i]
    return data

# Generate the data
data = simulate_water_usage()

# Create a DataFrame
columns = [
    'Date', 'Hostel', 'Water Usage (Liters)', 'Tank Capacity (Liters)', 'Tank Level (Liters)',
    'Total Rooms', 'Total Students', 'pH', 'Turbidity', 'TDS', 'Hardness', 'Iron', 'Chlorides',
    'Residual Chlorine', 'Fluoride', 'Sulfate', 'Nitrates', 'Chloramines', 'Alkalinity', 'Coliform Bacteria'
]
df = pd.DataFrame(data, columns=columns)

# Save the Data to CSV
df.to_csv('water_usage_dataset.csv', index=False)

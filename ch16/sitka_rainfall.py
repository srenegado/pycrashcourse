# Ex 16-1

import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Extract and read data.
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get date and daily rainfall.
    dates, rainfall = [], []
    for row in reader:
        try:
            daily_rainfall = float(row[3])
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
        except ValueError:
            print(f'Missing data for {current_date}.')
        else:
            rainfall.append(daily_rainfall)
            dates.append(current_date)

# Plot the daily rainfall amounts.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, c='blue', linewidth=0.7)

# Set title and label axis.
plt.title('Daily rainfall in Sitka Airport, AK, 2018', fontsize=16)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate
plt.ylabel('Precipitation (in.)', fontsize=14)
plt.tick_params(axis='both', which='both', labelsize=12)

plt.show()
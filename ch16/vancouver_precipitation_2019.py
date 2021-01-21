# Ex 16-5

import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Extract and read data.
filename = 'data/vancouver_precipitation_simple_2019.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get column indices.
    indices = {}
    header_names = ['DATE', 'PRCP', 'SNOW']
    for index, header in enumerate(header_row):
        if header in header_names:
            indices[header] = index

    # Get dates, and daily rainfall and snowfall.
    dates, daily_rainfall, daily_snowfall = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[indices['DATE']], '%Y-%m-%d')
        try:
            rainfall = float(row[indices['PRCP']])
            snowfall = float(row[indices['SNOW']])
        except ValueError:
            print(f'Missing data for {current_date}.')
        else:
            daily_rainfall.append(rainfall)
            daily_snowfall.append(snowfall)
            dates.append(current_date)

# Plot data.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, daily_rainfall, c='blue', linewidth=1.3, label='rainfall')
ax.plot(dates, daily_snowfall, c='cyan', linewidth=1.3, label='snowfall')

# Set title and label axes.
title = 'Daily precipitation in \nVancouver, BC, 2019'
plt.title(title, fontsize=16)
plt.xlabel('Date (YY/MM)', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Precipitation (mm)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.legend()
plt.savefig('vancouver_precipitation_2019')
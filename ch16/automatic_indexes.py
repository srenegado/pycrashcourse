# Ex 16-4
# Built to handle any dataset by using the header row to
# determine the indices corresponding to whichever column
# specificed (e.g. DATE, NAME, TMAX, etc.).

import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Extract and read data.
#filename = 'data/sitka_weather_2018_simple.csv'
#filename = 'data/death_valley_2018_simple.csv'
filename = 'data/san_francisco_weather_2018.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get column indices.
    header_names = ['NAME', 'DATE', 'TMAX', 'TMIN']
    indices = {}
    for index, header in enumerate(header_row):
        if header in header_names:
            indices[header] = index

    # Get station name, dates, and high and low temperatures from this file. 
    dates, highs, lows = [], [], []
    got_name = False
    for row in reader:
        if got_name:
            current_date = datetime.strptime(row[indices['DATE']], '%Y-%m-%d')
            try:
                high = int(row[indices['TMAX']])
                low = int(row[indices['TMIN']])
            except ValueError:
                print(f"Missing data for {current_date}.")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
        else:
            name = row[indices['NAME']].title()
            got_name = True
        
# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', linewidth=1.5, alpha=0.5, label='high temperatures')
ax.plot(dates, lows, c='blue', linewidth=1.5, alpha=0.5, label='low temperatures')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = f'Daily high and low temperatures in \n{name}, 2018'
plt.title(title, fontsize=16)
plt.xlabel('Date (YY/MM)', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=12)

# Determine a suitable y-axis.
tmax = max(highs)
plt.yticks(list(range(0,tmax+20,20)))

plt.legend()
plt.show()
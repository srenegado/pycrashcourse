# Ex 16-3

import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Read and extract data.
filename = 'data/san_francisco_weather_2018.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures.
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}.")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot data.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5, label='high temperatures')
ax.plot(dates, lows, c='blue', alpha=0.5, label='low temperatures')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Set title and format axis.
title = 'Daily high and low temperatures in San Francisco, CA, 2018'
plt.title(title, fontsize=16)
plt.xlabel('Date (YY/MM)',fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)

plt.yticks(list(range(0, 160, 20)))
plt.tick_params(axis='both', which='major', labelsize='12')

plt.legend()
plt.savefig('san_francisco_highs_lows.png')
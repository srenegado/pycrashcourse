import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data\sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates, and high and low temperatures from this file. 
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        
# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', linewidth=1.5, alpha=0.5, 
    label='high temperatures')
ax.plot(dates, lows, c='blue', linewidth=1.5, alpha=0.5,
    label='low temperatures')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = 'Daily high and low temperatures in Sitka Airport, AK, 2018'
plt.title(title, fontsize=16)
plt.xlabel('Date (YY/MM)', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)

plt.yticks(list(range(0, 160, 20)))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.legend()
plt.savefig('sitka_highs_lows')
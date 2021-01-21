import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Extract all data.
# For most up-to-date data, go to 
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
filename = 'data/1.0_month.json'
with open(filename, encoding='utf8') as f:
    all_eq_data = json.load(f)

# Get earthquakes, and their magnitude, longitude, and latitude.
all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dicts in all_eq_dicts:
    mags.append(eq_dicts['properties']['mag'])
    lons.append(eq_dicts['geometry']['coordinates'][0])
    lats.append(eq_dicts['geometry']['coordinates'][1])
    hover_texts.append(eq_dicts['properties']['title'])

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'YlOrRd',
        'colorbar': {'title': 'Magnitude'}
    }
}]
title = all_eq_data['metadata']['title']
my_layout = Layout(title=title, title_x=0.5)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
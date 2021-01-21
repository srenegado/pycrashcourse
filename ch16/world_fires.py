# Ex 16-9

import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Extract data.
# For most up-to-date data, go to
# https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data/
filename = 'data/J1_VIIRS_C2_Global_24h.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get indices for latitude, longitude, and brightness.
    selected_headers = ['latitude', 'longitude', 'bright_ti4']
    indices = {}
    for index, header in enumerate(header_row):
        if header in selected_headers:
            indices[header] = index

    # Get latitude, longitude, and brightness of each fire.
    lats, lons, brights = [], [], []
    for row in reader:
        lats.append(float(row[ indices['latitude'] ]))
        lons.append(float(row[ indices['longitude'] ]))
        brights.append(float(row[ indices['bright_ti4'] ]))

# Map data.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [bright/15 for bright in brights],
        'color': brights,
        'colorscale': 'YlOrRd',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'}
    }
}]

my_layout = Layout(title='VIIRS 375 m (NOAA-20) World Fires, Past 24 Hours', title_x=0.5)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')

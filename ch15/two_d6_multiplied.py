# Ex 15-8

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die()

# Roll two D6's, multiply the two rolled numbers, and record the result.
results = []
for nth_roll in range(10000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze results.
frequencies = []
max_roll = die_1.num_sides * die_2.num_sides
for value in range(1,max_roll+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize results.
x_values = list(range(1,max_roll+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title="Results of multiplying two rolled numbers from two "
    "D6's 10,000 times", title_x=0.5, xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='two_d6_multiplied.html')
# Ex 15-7

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls and record the results.
results = [die_1.roll() + die_2.roll() + die_3.roll() for nth_roll 
    in range(10000)]

# Analyze results.
max_roll = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3,max_roll+1)]

# Visualize results.
x_values = list(range(3,max_roll+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title="Results of rolling three D6's 10,000 times",
    title_x=0.5, xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='three_d6.html')
# Ex 15-10

import matplotlib.pyplot as plt
from die import Die

die_1 = Die(8)
die_2 = Die(8)

# Make some rolls and store results.
results = [die_1.roll() + die_2.roll() for nth_roll in range(10000)]

# Analyze results.
max_roll = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_roll+1)]

# Visualize results.
x_values = range(2,max_roll+1)

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
ax.bar(x_values, frequencies, tick_label=x_values)

ax.set_title("Results of rolling two D8's 10,000 times", fontsize=16)
ax.set_xlabel('Result', fontsize=14)
ax.set_ylabel('Frequency of Result', fontsize=14)

plt.savefig('two_d8s_with_matplotlib.png')
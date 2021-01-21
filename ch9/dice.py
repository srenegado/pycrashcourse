# Ex 9-13

from die import Die

six_sided_die = Die()
print("Rolling a 6-sided die 10 times:")
for nth_roll in range(10):
    six_sided_die.roll_die()

ten_sided_die = Die(10)
print("Rolling a 10-sided die 10 times:")
for nth_roll in range(10):
    ten_sided_die.roll_die()

twenty_sided_die = Die(20)
print("Rolling a 20-sided die 10 times:")
for nth_roll in range(10):
    twenty_sided_die.roll_die()
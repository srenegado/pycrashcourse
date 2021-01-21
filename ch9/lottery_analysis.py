# Ex 9-15

from lottery import buy_lottery_ticket, get_number_of_tickets_up_until_a_win

pool = [43, 23, 'a', 12, 'g', 31, 4, 1, 't', 15, 25, 'y', 'h', 40, 14]

# Generate a winning lottery ticket
winning_ticket = buy_lottery_ticket(pool)
print(f"The winning lottery sequence is: {winning_ticket}")

# We want to know, on average, how many tickets do we need to buy
# until we win the lottery.

# So, keep buying lottery tickets until we win while
# keeping track of the number of tickets bought.
# Then record that number and repeat this process 10 times.

bought_tickets_average = 0
bought_tickets_data = []
for nth_trial in range(25):
    bought_tickets = get_number_of_tickets_up_until_a_win(pool, winning_ticket)
    # Record the number of bought tickets into our dataset.
    bought_tickets_data.append(bought_tickets)

# Calculate the average bought tickets in order to win the lottery.
for data_entry in bought_tickets_data:    
    bought_tickets_average += data_entry
bought_tickets_average /= len(bought_tickets_data)

print(f"It took, on average, {bought_tickets_average} " 
      f"tickets to win the lottery.")

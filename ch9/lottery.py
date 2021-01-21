# Ex 9-14
from random import randint

def buy_lottery_ticket(pool):
    """
    From a given pool of characters, return
    a 4-character lottery ticket.
    """
    lottery_ticket = []
    for nth_entry in range(4):
        random_index = randint(0,14)
        lottery_ticket.append(pool[random_index])
    return lottery_ticket

def get_number_of_tickets_up_until_a_win(pool, winning_ticket):
    """
    Keep buying lottery tickets until a winning ticket is bought.
    While doing so, keep track of the number of tickets bought and
    return that number.
    """
    not_a_winner = True
    bought_tickets = 0
    while not_a_winner:
        # Buy a ticket and increase the number of bought tickets by 1.
        my_ticket = buy_lottery_ticket(pool)
        bought_tickets += 1

        if my_ticket != winning_ticket:
            # Throw away the losing ticket.
            del my_ticket
            my_ticket = []
        else:
            # We won!
            not_a_winner = False
    return bought_tickets


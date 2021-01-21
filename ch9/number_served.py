# Ex 9-4

from restaurant import Restaurant

restaurant = Restaurant('Thai Son', 'vietnamee')
print(f"Number of customers served today: {restaurant.number_served}\n"
      f"3 hours after opening...")
restaurant.number_served = 20
print(f"Number of customers served today: {restaurant.number_served}\n"
      f"1 hour later...")
restaurant.set_number_served(25)
print(f"Number of customers served today: {restaurant.number_served}\n"
      f"Hours later until closing time...")
restaurant.increment_number_served(25)
print(f"Total number of customers served today: {restaurant.number_served}")

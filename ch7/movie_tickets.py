# Ex 7-5

prompt = "Enter your age.\n(Enter 'quit' when you're done) "
active = True
while active:
    try:
        age = input(prompt)
        if age == 'quit':
            active = False
            break
        age = int(age)
        if age < 3:
            print("Your ticket is free.")
        elif age >=3 and age <= 12:
            print("Your ticket costs $10.")
        elif age > 12:
            print("Your ticket costs $15.")

    except ValueError:
        print("Invalid input. Please try again.")


    
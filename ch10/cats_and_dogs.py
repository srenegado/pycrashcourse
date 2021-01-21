# Ex 10-8

file_name = 'dogs.txt'
try:
    with open(file_name) as f:
        print(f.read())
except:
    print(f"Sorry, I couldn't find {file_name}.")
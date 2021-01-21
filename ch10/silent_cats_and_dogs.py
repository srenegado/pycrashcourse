# Ex 10-9

file_name = 'dogs.txt'
try:
    with open(file_name) as f:
        print(f.read())
except:
    pass
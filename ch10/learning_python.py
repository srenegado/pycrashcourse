# Ex 10-1

# Print by reading the entire file.
with open('learning_python.txt') as file_object:
    contents = file_object.read()
for i in range(3):
    print(contents)

# Print by looping over the file object.
for i in range (3):
    with open('learning_python.txt') as file_object:   
        for line in file_object:
            print(line.rstrip())

# Print by storing the lines in a list and working with that list.
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()
for i in range(3):
    for line in lines:
        print(line.rstrip())
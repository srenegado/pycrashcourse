# Ex 10-2

with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents.replace('Python','C'))
# Ex 6-4

glossary = {
    'if-statement': 'A statement that allows for an action (or actions) '
                    'if a condition is met.',
    'variable': 'A word that stores data.',
    'for-loop': 'A repetitive set of actions that will terminate.',
    'list': 'A ordered set of data values.',
    'method': 'An action that can performed on a piece of data.',
    'exception': 'An error.',
    'list comprehension': 'A one-line abbreivation for creating a list '
                          'using a for-loop.'
}

for term, definition in glossary.items():
    print(f"{term}:\n\t{definition}")
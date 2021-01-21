# Ex 6-3

glossary = {
    'if-statement': 'A statement that allows for an action (or actions) '
                    'if a condition is met.',
    'variable': 'A word that stores data.',
    'for-loop': 'A repetitive set of actions that will terminate.',
    'list': 'A ordered set of data values.',
    'method': 'An action that can performed on a piece of data.'
}

for key in glossary:
    print(f"{key}:\n\t{glossary[key]}")
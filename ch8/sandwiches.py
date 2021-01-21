# Ex 8-12
def make_sandwich(*ingredients):
    """Print a list of ingredients to be used in making a sandwich."""
    print("Sandwich order:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich('lettuce', 'tomato', 'ham', 'mayo', 'mustard')

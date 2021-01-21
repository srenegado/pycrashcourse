# Ex 10-10

texts = [
    'frankenstein_by_mary_shelley.txt',
    'the_adventures_of_sherlock_holmes_by_arthur_conan_doyle.txt',
    'a_tale_of_two_cities_by_charles_dickens.txt']

for text in texts:
    with open(text, encoding='utf8') as f:
        contents = f.read()
    print(f"The word 'the' appears in the file {text} approximately "
          f"{contents.lower().count('the ')} times.")

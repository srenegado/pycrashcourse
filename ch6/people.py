# Ex 6-7
people = {
    'yitadori': {
        'first_name': 'yuuji',
        'last_name': 'itadori',
        'height': 173,
        'school': 'jujutsu high' 
    },

    'mfushiguro': {
        'first_name': 'megumi',
        'last_name': 'fushiguro',
        'height': 175,
        'school': 'jujutsu high'
    },

    'nkugisaki': {
        'first_name': 'nobara',
        'last_name': 'kugisaki',
        'height': 160,
        'school': 'jujutsu high'
    },
}

for person_info in people.values():
    full_name = f"{person_info['first_name']} {person_info['last_name']}"
    print(f"Full name: {full_name.title()}\n"
          f"Height: {person_info['height']} cm\n"
          f"School: {person_info['school'].title()}\n")
    
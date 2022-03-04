favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

take_poll = ['jasmin', 'rudy', 'jen', 'mike', 'phil']

for person in take_poll:
    if person in favorite_languages.keys():
        print(f"{person.title()}, thank you for responding to the poll.")
    else:
        print(f"{person.title()}, please take our poll.")

pet_1 = {
    'kind': 'cat',
    'owner': 'michelle',
    }

pet_2 = {
    'kind': 'dog',
    'owner': 'bruce',
    }

pet_3 = {
    'kind': 'bird',
    'owner': 'zack',
    }

pet_4 = {
    'kind': 'horse',
    'owner': 'nendo',
    }

pet_5 = {
    'kind': 'tiger',
    'owner': 'saiko',
    }

pets =[pet_1, pet_2, pet_3, pet_4, pet_5]

for pet in pets:
    print(f"{pet['kind'].title()} belongs to {pet['owner'].title()}.")
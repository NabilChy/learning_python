favorite_numbers = {
    'tia': [5, 7],
    'rem': [20],
    'jordan': [10, 15],
    'kelly': [6],
    'kush': [70],
    }

print(f"Favorite number of Tia is {favorite_numbers['tia']}.")
print(f"Favorite number of Rem is {favorite_numbers['rem']}.")
print(f"Favorite number of Jordan is {favorite_numbers['jordan']}.")
print(f"Favorite number of Kelly is {favorite_numbers['kelly']}.")
print(f"Favorite number of Kush is {favorite_numbers['kush']}.")

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
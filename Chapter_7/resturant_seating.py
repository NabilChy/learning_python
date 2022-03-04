number_of_people = input("How many people are in your group? ")
number_of_people = int(number_of_people)

if number_of_people > 8:
    print("\nYou will have to wait for a table.")
else:
    print("\nPlease come in, your table is ready.")
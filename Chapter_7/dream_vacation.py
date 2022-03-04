responses = {}

active = True

while active:
    name = input("\nWhat is your name? ")
    prompt = "If you could visit one place in the world,"
    prompt += "\nwhere would you go? "
    vacation_spot = input(prompt)

    #Adding responses to the dictionary
    responses[name] = vacation_spot

    repeat = input("Would you like to continue? (y/n) ")
    if repeat == 'n':
        active = False

for name, vacation_spot in responses.items():
    print(f"\n{name.title()} would like to visit {vacation_spot.title()}.")


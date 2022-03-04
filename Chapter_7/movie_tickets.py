prompt = ("\nPlease enter your age: ")

active = True
count = 0
while active:
    message = input(prompt)
    age = int(message)

    

    if age < 3:
        print("You are free to enter.")
    elif age <= 12:
        print("The ticket costs $10")
    else:
        print("The ticket cost $15.")
    
    count += 1

    if count == 5:
        print("Sorry, we are full.")
        break
    
    
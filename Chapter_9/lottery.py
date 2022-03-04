from random import choice

def get_winning_ticket(numbers):
    '''Returns the winning ticket number'''
    winning_ticket =[]
    while len(winning_ticket) < 4:
        winning_numbers = choice(numbers)

        if winning_numbers not in winning_ticket:
            winning_ticket.append(winning_numbers)
    
    return winning_ticket

def check_ticket(winning_ticket, my_ticket):
    '''Checks to see if I won'''
    for element in winning_ticket:
        if element not in my_ticket:
            return False
        
    return True

lottery_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E')
my_ticket = (0, 6, 'C', 'D')
count = 0
won = False
print("The winning numbers are:")

while not won:
    winning_ticket = get_winning_ticket(lottery_numbers)
    count += 1
    won = check_ticket(winning_ticket, my_ticket)


if won:
    print(f"My ticket : {my_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It took {count} tries.")

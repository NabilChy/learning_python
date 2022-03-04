sandwich_orders = ['pastarami', 'tuna', 'chicken', 'pastarami', 'beef', 'vegetable', 'pastarami']
finished_sandwiches = []

print("Sorry, the deli has run out of pastarami.")
while 'pastarami' in sandwich_orders:
    sandwich_orders.remove('pastarami')


while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

#Printing a list of all finished sandwiches.
print("Finished sandwiches: ")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")
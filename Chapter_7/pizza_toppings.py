prompt = "\nPlease enter your desired toppings."
prompt += "\n(Please enter 'quit' when you are done. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(f"{message.title()} will be added to the pizza.")
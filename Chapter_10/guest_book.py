filename = 'guest_book.txt'
#count = 0
with open(filename, 'w') as file_object:
    
    while True:
        name = input("Please enter your name: ")
        print(f"Welcome to hell {name}")
        file_object.write(f"{name}\n")
        #count += 1
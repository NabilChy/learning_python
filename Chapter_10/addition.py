while True:
    a = input("Enter a number: ")
    b = input("Enter another number: ")

    try:
        a = int(a)
        b = int(b)
        c = a + b
    except ValueError:
        print("Please enter a number, no texts.")
    else:
        print(c)

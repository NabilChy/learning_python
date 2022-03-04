usernames = ['jayden', 'karina', 'admin', 'rikki', 'alu']

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username.title()}, would you like to see a status report?")
        else:
            print(f"Thanks for logging in {username.title()}")
else:
    print("We need to find some users")
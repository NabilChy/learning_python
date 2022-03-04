def print_words(filename):
    '''Prints the words in a file'''
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Sorry, unable to find {filename}.")
        pass
    else:
        words = contents.split()
        for word in words:
            print(word)
    

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print_words(filename)
def count_words(filename):
    '''Count the approximate number of words in a file'''
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        # Count the approximate number of words in the file
        word = input("Enter the word to be searched: ")
        count = contents.lower().count(word)
        print(count)
        
filenames = ['alice.txt']
for filename in filenames:
    count_words(filename)
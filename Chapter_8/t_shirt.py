def make_shirt(size='Large', text='I love python'):
    '''Summarizes the shirt size and message'''
    print(f"\nThe shirt size is {size.title()}.")
    print(f"The message to be printed is '{text.title()}'.")

make_shirt('short', 'life is short, so enjoy it')
make_shirt(size='medium', text='life is short, so destroy it')
make_shirt()
make_shirt('medium')

class Resturant:
    '''An attempt to describe a resturant'''
    
    def __init__(self, resturant_name, cuisine_type):
        '''Innitialize the attributes to represent a resturant.'''
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type


    def describe_resturant(self):
        '''Describes the resturant.'''
        print(f"The resturant's name is {self.resturant_name}")
        print(f"It offers {self.cuisine_type} cuisine.")
    

    def open_resturant(self):
        '''Indicates the state of the resturant.'''
        print(f"{self.resturant_name} is now OPEN!")


resturant = Resturant('Fatafat', 'indian')
resturant.describe_resturant()
resturant.open_resturant()

resturant_1 = Resturant('Saad', 'turkey')
resturant_1.describe_resturant()

resturant_2 = Resturant('Crown', 'street')
resturant_2.describe_resturant()
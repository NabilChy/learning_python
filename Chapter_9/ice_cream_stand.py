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


class IceCreamStand(Resturant):
    '''An attempt to model an Ice cream stand'''

    def __init__(self, resturant_name, cuisine_type):
        super().__init__(resturant_name, cuisine_type)
        self.flavors = ['vanilla', 'butter pecan', 'chocolate', 'mint']
    
    def list_flavors(self):
        '''Prints out the list of flavors available'''
        print("\nThe available flavors are:")
        for flavor in self.flavors:
            print(f"-{flavor.title()}")

my_stand = IceCreamStand('Yippi', 'Ice cream')
my_stand.describe_resturant()
my_stand.list_flavors()
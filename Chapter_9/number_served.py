class Resturant:
    '''An attempt to describe a resturant'''
    
    def __init__(self, resturant_name, cuisine_type):
        '''Innitialize the attributes to represent a resturant.'''
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_resturant(self):
        '''Describes the resturant.'''
        print(f"The resturant's name is {self.resturant_name}")
        print(f"It offers {self.cuisine_type} cuisine.")
        print(f"{self.resturant_name} has served {self.number_served} customers today.")
    

    def open_resturant(self):
        '''Indicates the state of the resturant.'''
        print(f"{self.resturant_name} is now OPEN!")


    def set_number_served(self, number_of_customers):
        '''Updates the number of customers served'''
        self.number_served = number_of_customers


    def increment_number_served(self, number):
        '''Adds the value provided to number_served.'''
        self.number_served += number


resturant = Resturant('Fatafat', 'indian')
resturant.describe_resturant()
resturant.open_resturant()
resturant.set_number_served(100)
resturant.describe_resturant()
resturant.increment_number_served(100)
resturant.describe_resturant()
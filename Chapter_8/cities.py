def describe_city(city_name, country_name='United Kingdom'):
    '''Prints a city's location'''
    print(f"\n{city_name.title()} is in {country_name.title()}.")

describe_city('london')
describe_city('upper darby', 'united states of america')
describe_city('magnolia', 'wizard kingdom')
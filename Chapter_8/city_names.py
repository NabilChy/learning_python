def city_country(city_name, country_name):
    '''Returns a formatted city-country pair'''
    formatted_name = f"\"{city_name}, {country_name}\""
    return formatted_name.title()

location = city_country('santiago', 'chile')
print(location)
location = city_country('pitsburg', 'united states of america')
print(location)
location = city_country('london', 'united kingdom')
print(location)
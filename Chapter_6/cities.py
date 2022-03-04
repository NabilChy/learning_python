cities = {
    'philadelphia': {
        'country': 'united states of america',
        'population': 500,
        'fact': 'city of brotherly love',
        },

    'shire': {
        'country': 'isengard',
        'population': 200,
        'fact': 'shorties live here',
        },
    
    'london': {
        'country': 'united kingdom',
        'population': 600,
        'fact': 'british',
        },

    }

for city, city_information in cities.items():
    print(city.title())
    country = f"{city_information['country']}"
    population = f"{city_information['population']}" 
    fact = f"{city_information['fact']}"

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population.title()}")
    print(f"\tFact: {fact.title()}")

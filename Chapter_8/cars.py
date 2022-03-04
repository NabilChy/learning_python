def make_car(first, last, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['first_name'] = first
    car_info['last_name'] = last
    return car_info

car =  make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
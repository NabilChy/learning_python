def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                              location='princeton',
                              field='physics')


user_profile = build_profile('daiyan', 'chowdhury',
                              height= "5'6",
                              location= 'upper darby',
                              country= 'United states of america',
                              )

print(user_profile)
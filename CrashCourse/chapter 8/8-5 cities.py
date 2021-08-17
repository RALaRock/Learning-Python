# 8-5. Cities:
# Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence,
# such as Reykjavik is in Iceland. Give the parameter for the country
# a default value. Call your function for three different cities, at least
# one of which is not in the default country.


def describe_city(cityname, country="Great Britain"):
    """print a sentence about the city and country"""
    print(f"{cityname.title()} is in the {country.title()}.")


describe_city("london")
describe_city("Manchester")
describe_city("Los Angeles", "USA")

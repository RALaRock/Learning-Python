# 8-6. City Names:
# Write a function called city_country() that takes in the name of a
# city and its country. The function should return a string formatted
# like this: "Santiago, Chile" Call your function with at least three
# city-country pairs, and print the values that are returned.


def city_country(city, country):
    """format a string into 'city, country' and return the string"""
    if city and country:
        string = f"{city}, {country}"
        return string.title()
    else:
        return None


print(city_country("los angeles", "USA"))
print(city_country("Sao Paolo", "Brazil"))
print(city_country("London", "England"))

def get_formatted_city_country(city, country, population=None):
    """
    Returns a formatted City, Country string.
    of the form City, Country – population xxx
    """

    result = f"{city}, {country}"

    if population:
        result = result.title() + f" - population {population}."
    else:
        result = result.title() + "."

    return result

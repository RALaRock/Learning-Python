# make a dictionary of favorite places
# use people names as the key
# for each person store up to three places
# print every person's places

# dictionary containing lists of places for each person
favorite_places = {
    "bill": ["machu pichu", "new york", "mount Everest"],
    "sam": ["london", "", "los angeles"],
    "ellie": ["sao paulo"],
    "don": [],
}

# print(type(favorite_places))
# places = favorite_places.get('bill')
# print(places)

for name, places in favorite_places.items():
    # print the person's name
    print(name.title())
    # print their favorite places
    # don't print unless there is at least one place in the list
    if len(places) > 0:
        # print all places for each person
        for place in places:
            # don't print empty places
            if place != "":
                print(f"\t {place.title()}")

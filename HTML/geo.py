import reverse_geocoder

"""The reverse_geocoder.search function will return a list of dictionaries. Use the first dictionary in the list and display the name, admin1, and cc values as location information for the image. The name will be the name of the nearest city with a population of more than 1000. For the US, admin1 will be the name of a state and for other countries it will be the name of a province or something similar. The cc value is a two-letter country code."""

def findLocation(lati, longi):
    found = reverse_geocoder.search(lati, longi)
    return found.get("name"), found.get("admin1"), found.get("cc")
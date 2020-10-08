from math import radians, cos, sin, asin, sqrt
from uszipcode import SearchEngine


def check_distance(center_lat, center_lng, test_lat, test_lng):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    center_lat, center_lng, test_lat, test_lng = map(
        radians, [center_lat, center_lng, test_lat, test_lng])

    # haversine formula
    dlon = test_lng - center_lng
    dlat = test_lat - center_lat
    a = sin(dlat/2)**2 + cos(center_lat) * cos(test_lat) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 3956  # Radius of earth in miles. Use 6371 for miles
    distance = c * r
    return distance


def check_by_city(city, state):
    search = SearchEngine(simple_zipcode=True)
    city = search.by_city_and_state(city=city, state=state)
    result = city[0].to_dict()
    state = result.get("state")
    lat = result.get("lat")
    lng = result.get("lng")
    return [state, lat, lng]


def check_by_zipcode(zipcode):
    search = SearchEngine(simple_zipcode=True)
    zipcode = search.by_zipcode(zipcode)
    result = zipcode.to_dict()
    state = result.get("state")
    lat = result.get("lat")
    lng = result.get("lng")
    return [state, lat, lng]


def check_by_coordinates(lat, lng):
    search = SearchEngine(simple_zipcode=True)
    coordinates = search.by_coordinates(lat, lng, radius=25)
    result = coordinates[0].to_dict()
    state = result.get("state")
    lat = result.get("lat")
    lng = result.get("lng")
    return [state, lat, lng]

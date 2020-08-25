
import os 
import json
import requests
from urllib.parse import urlencode, urlparse, parse_qsl

# ---------- Results a JSON object of details based place_id -------------------

def search_details(place_id):
    base_endpoint = "https://maps.googleapis.com/maps/api/place/details/json"
    fields = "name,formatted_address,formatted_phone_number,geometry,business_status,url,website,icon,types"
    params = {
        "key": os.environ.get('GOOGLE_API'),
        "place_id": place_id,
        "fields": fields
    }
    params_encoded = urlencode(params)
    url = f"{base_endpoint}?{params_encoded}"
    r = requests.get(url)
    print('search_by_id:', r.status_code)
    return r.json()


# data = search_by_id('ChIJlXOKcDC3j4ARzal-5j-p-FY')
# print(json.dumps(data, indent=4))
# print(data['result'])
# print(data['status'])


# ---------- Results in a list of searches based on category -------------------

def search_nearby(category, lat, lng, miles=25):
    base_endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    fields = "place_id,name,formatted_address,formatted_phone_number,geometry,business_status,url,website,icon,types"
    radius = miles * 0.00062137
    params = {
        "key": os.environ.get('GOOGLE_API'),
        "keyword": category,
        "fields": fields,
        "radius": radius,
        "location": f"{lat},{lng}",
    }
    params_encoded = urlencode(params)
    places_endpoint = f"{base_endpoint}?{params_encoded}"
    r = requests.get(places_endpoint)
    print('search_nearby:', r.status_code)
    return r.json()

# data = search_nearby('Highschool', 40.541497834, -74.140166106)
# print(data)
# print(data['results'])
# print(data['status'])


# ---------- Results in one location matching name -------------------

def search_for_place(place, lat, lng, miles=25):
    base_endpoint_places = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    fields = "place_id,name,formatted_address,geometry,business_status,types"
    radius = miles * 0.00062137
    params = {
        "key": os.environ.get('GOOGLE_API'),
        "input": place,
        "inputtype": "textquery",
        "fields": fields,
        "locationbias": f"circle:{radius}@{lat},{lng}"
    }

    params_encoded = urlencode(params)
    places_endpoint = f"{base_endpoint_places}?{params_encoded}"
    r = requests.get(places_endpoint)
    print('search_for_place:', r.status_code)
    # place_id = r.json()['candidates'][0]['place_id']
    return r.json()


# data = search_for_place('Cardozo High School', 40.541497834, -74.140166106)
# print(json.dumps(data, indent=4))
# print(data['candidates'][0])
# print(data['status'])

# ---------- Google Places API with Geocoding API -------------------

class GooglePlacesAPI(object):
    lat = None
    lng = None
    data_type = 'json'
    location_query = None
    api_key = os.environ.get('GOOGLE_API')

    def __init__(self, location=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.location_query = location
        if self.location_query is not None:
            self.extract_lat_lng()

    def extract_lat_lng(self, location=None):
        loc_query = self.location_query
        if location is not None:
            loc_query = location
            endpoint = f"https://maps.googleapis.com/maps/api/geocode/{self.data_type}"
            params = {
            "address": loc_query,
            "key": self.api_key
        }

        url_params = urlencode(params)
        url = f"{endpoint}?{url_params}"
        r = requests.get(url)
        print("extract_lat_lng:", r.status_code, "=>", r.json()["status"])

        if r.status_code not in range(200, 299):
            return print(url)
        if r.json()["status"] == 'OVER_QUERY_LIMIT':
            raise Exception("Over query limit error")
        latlng = {}
        try:
            latlng = r.json()['results'][0]['geometry']['location']
        except:
            pass
        lat, lng = latlng.get("lat"), latlng.get("lng")
        self.lat = lat
        self.lng = lng
        return lat, lng

    def search_for_place_id(self, place=None, location=None, miles=25):
        lat, lng = self.lat, self.lng
        if location is not None:
            lat, lng = self.extract_lat_lng(location)

        radius = miles * 0.00062137
        endpoint = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/{self.data_type}"
        params = {
            "key": self.api_key,
            "location": f"{lat},{lng}",
            "input": place,
            "inputtype": "textquery",
            "fields": "place_id",
            "locationbias": f"circle:{radius}@{lat},{lng}"
        }

        params_encoded = urlencode(params)
        places_url = f"{endpoint}?{params_encoded}"
        r = requests.get(places_url)
        print("search_for_place_id:", r.status_code, "=>", r.json()["status"])

        if r.json()["status"] == 'ZERO_RESULTS':
            raise Exception ("Zero results")
        try:
            return r.json()['candidates'][0]['place_id']
        except:
            return r.json()

    def details(self, place=None, location=None, miles=25, place_id=None):
        place_id = self.search_for_place_id(place, location)

        fields = "name,formatted_address,formatted_phone_number,geometry,business_status,url,website,icon,types"
        base_endpoint = f"https://maps.googleapis.com/maps/api/place/details/{self.data_type}"

        params = {
            "place_id": f"{place_id}",
            "fields": fields,
            "key": self.api_key
        }

        params_encoded = urlencode(params)
        url = f"{base_endpoint}?{params_encoded}"
        r = requests.get(url)
        result = r.json()
        result["place_id"] = place_id
        print("details:", r.status_code, "=>", r.json()["status"])

        if r.json()["status"] == 'INVALID_REQUEST':
            raise Exception("Place_id might be is missing")
        elif r.json()["status"] == 'NOT_FOUND':
            raise Exception("Referenced location was not found")
        else:
            return result


# api = GooglePlacesAPI()
# place = "Cardozo"
# location = "11360"
# data = api.details(place, location)
# print(json.dumps(data, indent=4))

# place_id = data['place_id']
# business_status = data['result']['business_status']
# icon = data['result']['icon']
# name = data['result']['name']
# lat = data['result']['geometry']['location']['lat']
# lng = data['result']['geometry']['location']['lng']
# address = data['result']['formatted_address']
# phone_number = data['result']['formatted_phone_number']
# url = data['result']['url']
# website = data['result']['website']
# types = data['result']['types']

# print('place_id:', place_id)
# print('business_status:', business_status)
# print('icon:', icon)
# print('name:', name)
# print('lat:', lat)
# print('lng:', lng)
# print('address:', address)
# print('phone_number:', phone_number)
# print('url:', url)
# print('website:', website)
# print('types:', types)

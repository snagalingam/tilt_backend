import json
import requests
from django.conf import settings
from urllib.parse import urlencode


################################################################################
# Returns photo urls
################################################################################
def extract_photo_urls(photos):
    photo_array = []

    for photo in photos:
        url = f"https://maps.googleapis.com/maps/api/place/photo"
        maxwidth = f"?maxwidth={photo['width']}"
        reference = f"&photoreference={photo['photo_reference']}"
        key = f"&key={settings.GOOGLE_API_KEY}"

        photo_url = url + maxwidth + reference + key
        photo_array.append(photo_url)

    return photo_array


################################################################################
# Results a JSON object of details based place_id
################################################################################
def search_place_id(place_id):
    base_endpoint = "https://maps.googleapis.com/maps/api/place/details/json"
    fields = "name,formatted_address,formatted_phone_number,geometry,business_status,url,website,icon,types"
    params = {
        "key": settings.GOOGLE_API_KEY,
        "place_id": place_id,
        "fields": fields
    }
    params_encoded = urlencode(params)
    url = f"{base_endpoint}?{params_encoded}"
    r = requests.get(url)

    return r.json()


################################################################################
# Results in a list of searches based on category
################################################################################
def search_nearby(category, lat, lng, miles=200):
    base_endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    fields = "place_id,name,formatted_address,formatted_phone_number,geometry,business_status,url,website,icon,types"
    radius = miles * 0.00062137
    params = {
        "key": settings.GOOGLE_API_KEY,
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


################################################################################
# Results in one location matching name
################################################################################
def search_for_place(place, lat, lng, miles=200):
    base_endpoint_places = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    fields = "place_id,name,formatted_address,geometry,business_status,types"
    radius = miles * 0.00062137
    params = {
        "key": settings.GOOGLE_API_KEY,
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


################################################################################
# Google Places API with Geocoding API
################################################################################
class GooglePlacesAPI(object):
    lat = None
    lng = None
    data_type = 'json'
    location_query = None
    api_key = settings.GOOGLE_API_KEY
    error = {"errors": {}}

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

        self.error["errors"]["get_location"] = f"{r.status_code} ==>: {r.json()['status']}"
        print(f"get_location ==>: {self.error['errors']['get_location']}")

        latlng = {}

        try:
            latlng = r.json()['results'][0]['geometry']['location']
        except:
            pass

        lat, lng = latlng.get("lat"), latlng.get("lng")
        self.lat = lat
        self.lng = lng

        return lat, lng

    def search_for_place_id(self, place=None, location=None, miles=200):
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

        self.error["errors"]['place_id_search'] = f"{r.status_code} ==>: {r.json()['status']}"
        print(f"place_id_search ==>: {self.error['errors']['place_id_search']}")

        try:
            return r.json()['candidates'][0]['place_id']
        except:
            pass

    def details(self, place=None, location=None, miles=200, place_id=None):

        place_id = self.search_for_place_id(place, location)

        fields = "name,formatted_address,formatted_phone_number,geometry,business_status,url,website,icon,types,photos"
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

        self.error["errors"]["details"] = f"{r.status_code} ==>: {r.json()['status']}"
        print(f"details ==>: {self.error['errors']['details']}")

        if r.json()["status"] == ("INVALID_REQUEST" or "NOT_FOUND"):
            return self.error
        else:
            return result

# ---------- format places data to match model -------------------

# api = GooglePlacesAPI()
# place = "asdfasdg"
# location = "11360"
# data = api.details(place, location)
# print(json.dumps(data, indent=4))
# photos_result = data["result"]["photos"]
# photo_arr = extract_photo_urls(photos_result)

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
# main_photo = photo_arr[0]
# photos = photo_arr
# types = data['result']['types']

# print('place_id:', place_id)
# print('business_status:', business_status)
# print('name:', name)
# print('lat:', lat)
# print('lng:', lng)
# print('address:', address)
# print('phone_number:', phone_number)
# print('url:', url)
# print('website:', website)
# print('main_photo:', main_photo)
# print('photos:', photos)
# print('types:', types)

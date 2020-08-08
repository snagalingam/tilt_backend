import os 
import requests
from urllib.parse import urlencode

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
# print(data['result'])
# print(data['status'])


# ---------- Results in a list of searches based on category -------------------

def search_nearby(category, lat, lng, miles=10):
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

def search_for_place(place, lat, lng, miles=10):
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
    place_id = r.json()['candidates'][0]['place_id']
    return search_details(place_id)


data = search_for_place('Cardozo High School', 40.541497834, -74.140166106)

business_status = data['result']['business_status']
icon = data['result']['icon']
name = data['result']['name']
lat = data['result']['geometry']['location']['lat']
lng = data['result']['geometry']['location']['lng']
address = data['result']['formatted_address']
phone_number = data['result']['formatted_phone_number']
url = data['result']['url']
website = data['result']['website']
types = data['result']['types']

print('business_status:', business_status)
print('icon:', icon)
print('name:', name)
print('lat:', lat)
print('lng:', lng)
print('address:', address)
print('phone_number:', phone_number)
print('url:', url)
print('website:', website)
print('types:', types)
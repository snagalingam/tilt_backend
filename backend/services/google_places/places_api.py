import requests
from urllib.parse import urlencode

lat, lng = 37.42230960000001, -122.0846244
base_endpoint_places = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
params = {
    "key": api_key,
    "input": "Mexican food",
    "inputtype": "textquery",
    "fields": "place_id,formatted_address,name,geometry,permanently_closed"
}
locationbias = f"point:{lat},{lng}"
use_cirular = True
if use_cirular:
    radius = 5000
    locationbias = f"circle:{radius}@{lat},{lng}"

params['locationbias'] = locationbias

params_encoded = urlencode(params)
places_endpoint = f"{base_endpoint_places}?{params_encoded}"
print(places_endpoint)


# https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key=AIzaSyD8PCLxbKHRBrJWg6JYp-YXYz0ph4LKiQw
# &input=Mexican+food 
# &inputtype=textquery
# &fields=place_id%2Cformatted_address%2Cname%2Cgeometry%2Cpermanently_closed
# &locationbias=circle%3A5000%4037.42230960000001%2C-122.0846244


r = requests.get(places_endpoint)
print(r.status_code)


r.json()

#
# {
#     'candidates': [{
#         'formatted_address': '240 Villa St, Mountain View, CA 94041, United States',
#                 'geometry': {
#                     'location': {
#                         'lat': 37.3916289, 
#                         'lng': -122.0728897
#                         },
#                     'viewport': {
#                         'northeast': {
#                             'lat': 37.39290917989273,
#                             'lng': -122.0715766701073
#                             },
#                         'southwest': {
#                             'lat': 37.39020952010728, 
#                             'lng': -122.0742763298927
#                             }
#                         }
#                     },
#                  'name': 'La Fiesta',
#                  'place_id': 'ChIJlXOKcDC3j4ARzal-5j-p-FY'
#                  }],
#     'status': 'OK'
# }
#


# detail_lookup
def google_places_api_call(place_id):
    detail_base_endpoint = "https://maps.googleapis.com/maps/api/place/details/json"
    fields = "name,formatted_address,formatted_phone_number,geo_location,business_status,url,website",
    detail_params = {
        "place_id": f"{place_id}",
        "fields": f"{fields}",
        "key": api_key
    }
    detail_params_encoded = urlencode(detail_params)
    detail_url = f"{detail_base_endpoint}?{detail_params_encoded}"
    r = requests.get(detail_url)
    return r.json()
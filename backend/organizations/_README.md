
## Google Places API

# Status Codes

   `OK`
      indicates that no errors occurred; the place was successfully detected and at least one result was returned.
   `UNKNOWN_ERROR`
      indicates a server-side error; trying again may be successful.
   `ZERO_RESULTS`
      indicates that the referenced location (place_id) was valid but no longer refers to a valid result. This may occur if the establishment is no longer in business.
   `OVER_QUERY_LIMIT`
      indicates any of the following:
         - You have exceeded the QPS limits.
         - Billing has not been enabled on your account.
         - The monthly $200 credit, or a self-imposed usage cap, has been exceeded.
         - The provided method of payment is no longer valid (for example, a credit card has expired).
         - ee the Maps FAQ for more information about how to resolve this error.
   `REQUEST_DENIED`
      indicates that your request was denied, generally because:
         - The request is missing an API key.
         - The key parameter is invalid.
   `INVALID_REQUEST`
      generally indicates that the query (place_id) is missing.
   `NOT_FOUND`
      indicates that the referenced location (place_id) was not found in the Places database.

# Deconstructed Code

lat, lng = 37.42230960000001, -122.0846244
base_endpoint_places = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
params = {
    "key": os.environ.get('GOOGLE_API'),
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
print(places_endpoint) -->

<!-- # https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key=AIzaSyD8PCLxbKHRBrJWg6JYp-YXYz0ph4LKiQw
# &input=Mexican+food 
# &inputtype=textquery
# &fields=place_id%2Cformatted_address%2Cname%2Cgeometry%2Cpermanently_closed
# &locationbias=circle%3A5000%4037.42230960000001%2C-122.0846244 -->

r = requests.get(places_endpoint)
print(r.status_code)
print(r.json())


# Sample JSON (Based on Tilt Request Fields)

<!-- 
result': {
    'business_status': 'OPERATIONAL', 
    'formatted_address': '240 Villa St, Mountain View, CA 94041, USA', 
    'formatted_phone_number': '(650) 968-1364', 
    'geometry': {
        'location': {
            'lat': 37.3916289, 
            'lng': -122.0728897
            }, 
        'viewport': {
            'northeast': {
                'lat': 37.3929083302915, 
                'lng': -122.0715775197085
                }, 
            'southwest': {
                'lat': 37.3902103697085, 
                'lng': -122.0742754802915
                }
            }
        }, 
    'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/restaurant-71.png', 
    'name': 'La Fiesta',    
    'types': ['restaurant', 'food', 'point_of_interest', 'establishment'], 
    'url': 'https://maps.google.com/?cid=6266944973401139661', 
    'website': 'http://www.lafiestamexicancuisine.com/'
    }, 
'status': 'OK'
} -->
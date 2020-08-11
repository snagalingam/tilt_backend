## Google Places API

# Status Codes

`OK`
indicates that no errors occurred; the place was successfully detected and at least one result was returned.
`UNKNOWN_ERROR`
indicates a server-side error; trying again may be successful.
`ZERO_RESULTS`
indicates that the referenced location (place_id) was valid but no longer refers to a valid result. This may occur if the establishment is no longer in business.
`OVER_QUERY_LIMIT`
indicates any of the following: - You have exceeded the QPS limits. - Billing has not been enabled on your account. - The monthly \$200 credit, or a self-imposed usage cap, has been exceeded. - The provided method of payment is no longer valid (for example, a credit card has expired). - ee the Maps FAQ for more information about how to resolve this error.
`REQUEST_DENIED`
indicates that your request was denied, generally because: - The request is missing an API key. - The key parameter is invalid.
`INVALID_REQUEST`
generally indicates that the query (place_id) is missing.
`NOT_FOUND`
indicates that the referenced location (place_id) was not found in the Places database.

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

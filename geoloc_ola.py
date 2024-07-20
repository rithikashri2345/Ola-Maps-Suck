import json
import requests
import string
import random

def get_loc():
    url = f"https://api.olamaps.io/places/v1/reverse-geocode?latlng={generate_random_coordinates()}&api_key=FAzSqWWjO4rvGdZVqhIyX2uMTk4viC1FK3CcTubL"
    N = random.randint(3, 6)
    req_id = ''.join(random.choices(string.ascii_lowercase, k=N))
    payload = {}
    headers = {
    'X-Request-Id': req_id
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    return json.loads(response.text)

def generate_random_coordinates():
    # Define the latitude range (-90 to 90)
    min_latitude = -90
    max_latitude = 90
    
    # Define the longitude range (-180 to 180)
    min_longitude = -180
    max_longitude = 180
    
    base_lat = 12.923946516889448
    base_long = 77.5526110768168
    offset_lat = random.uniform(-2,2)
    offset_long = random.uniform(-2,2)

    # Generate random latitude and longitude
    latitude = base_lat + offset_lat
    longitude = base_long + offset_long
    # print(offset_lat, offset_long)
    # print(f"{latitude},{longitude}")
    return f"{latitude},{longitude}"


get_loc()

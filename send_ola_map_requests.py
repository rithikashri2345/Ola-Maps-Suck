import requests
import json
import string
import random
 
def ola_call():
    # initializing size of string
    N = random.randint(3, 12)
    api_key = ''
    # using random.choices()
    # generating random strings
    req_id = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=N))
    url = f"https://api.olamaps.io/places/v1/autocomplete?input={req_id}&api_key={api_key}"

    payload = {}
    headers = {
    'X-Request-Id': req_id
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)['status']=='ok'

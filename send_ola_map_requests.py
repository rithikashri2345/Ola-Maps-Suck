import requests
import json
import string
import random

 
def ola_call():
    # initializing size of string
    N = random.randint(3, 6)
    api_key = 'FAzSqWWjO4rvGdZVqhIyX2uMTk4viC1FK3CcTubL'
    # using random.choices()
    # generating random strings
    req_id = ''.join(random.choices(string.ascii_lowercase, k=N))
    url = f"https://api.olamaps.io/places/v1/autocomplete?input={form_str(req_id)}&api_key={api_key}"

    payload = {}
    headers = {
    'X-Request-Id': req_id
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)

def form_str(s):
    pos =  random.randint(0,4)
    res=""
    for i in s:
        if i in 'aeiou':
            res+=i
        else:
            res+=i
            res+='aeiou'[pos]
    print(res)
    return res
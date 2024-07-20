import json 

def get_access_token():
    import requests

    url = "https://account.olamaps.io/realms/olamaps/protocol/openid-connect/token"

    payload = 'grant_type=client_credentials&scope=openid&client_id=a4789861-0c08-4b89-b20f-2d2a22c7594e&client_secret=mKaHMLXhA56PEloGdUnVDRBK0Jda9vRy'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)
    # return access_token
# print(get_access_token()['access_token'])
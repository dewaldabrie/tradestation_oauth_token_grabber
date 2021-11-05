import os
import time
import urllib.parse
import webbrowser
import requests

# %%
# https://api.tradestation.com/docs/fundamentals/authentication/auth-code

KEY = os.environ.get('KEY', '')
SECRET = os.environ.get('SECRET', '')


# 1. Redirect user for authentication/authorization
# Make sure flask_app is running with ./run_app, which will
# capture ethe authorization code.
base_url = 'https://signin.tradestation.com/authorize?'
params = {
    'response_type': 'code',
    'client_id': KEY,
    'redirect_uri': 'http://localhost:3000',
    'audience': 'https://api.tradestation.com',
    'state': 'STATE',
    'scope': 'openid profile offline_access MarketData ReadAccount Trade Crypto'
}
safe_string = urllib.parse.urlencode(params)
url = base_url + safe_string
webbrowser.open(url)

# 2. Client receives Authorization Code#
# TODO: This should be saved to GCP secret manager
auth_code = ''
while True:
    cur_dir = os.path.dirname(__file__)
    path = os.path.join(cur_dir, 'auth_code.txt')
    print(path)
    if os.path.isfile(path):
        with open(path, mode='r') as fh:
            auth_code = fh.read().strip()
        os.remove(path)
        break
    else:
        time.sleep(1)

# %% 3. Exchange Authorization Code for Access Token, ID Token and Refresh Token
base_url = 'https://signin.tradestation.com/oauth/token'
headers = {'content-type': 'application/x-www-form-urlencoded'}
data = {
    'grant_type': 'authorization_code',
    'client_id': KEY,
    'client_secret': SECRET,
    'code': auth_code,
    'redirect_uri': 'http://localhost:3000'
}
resp = requests.post(base_url, headers=headers, data=data, allow_redirects=True)
resp_dict = resp.json()
print(resp_dict)
access_token = resp_dict['access_token']
refresh_token = resp_dict['refresh_token']

# %% 4. Get Refresh token (indefinite expiry)
# https://api.tradestation.com/docs/fundamentals/authentication/refresh-tokens/
base_url = 'https://signin.tradestation.com/oauth/token'
headers = {'content-type': 'application/x-www-form-urlencoded'}
data = {
    'grant_type': 'refresh_token',
    'client_id': KEY,
    'client_secret': SECRET,
    'refresh_token': refresh_token,
}
resp = requests.post(base_url, headers=headers, data=data, allow_redirects=True)
resp_dict = resp.json()
access_token = resp_dict['access_token']
print(f"Access token: {access_token}")

with open(os.path.join(cur_dir, 'access_token.txt'), mode='w') as fh:
    fh.write(access_token)

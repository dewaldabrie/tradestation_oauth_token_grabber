import os
import requests

KEY = os.environ.get('KEY', '')
SECRET = os.environ.get('SECRET', '')

with open('refresh_token.txt', 'r') as fh:
    refresh_token = fh.read().strip()


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
try:
    new_token = resp_dict['access_token']
except Exception as e:
    raise Exception(resp.content) from e

with open('access_token.txt', 'w') as fh:
    fh.write(new_token)

# optionally export your access token to http-client.priver.env.json
import json
private_json_env_filename = 'http-client.private.env.json'
def write_to_http_env_file(key, token):
    with open(private_json_env_filename, 'r') as fh:
        envs = json.load(fh)
    envs['dev'][key] = token
    with open(private_json_env_filename, 'w') as fh:
        json.dump(envs, fh)

write_to_http_env_file('access_token', new_token)

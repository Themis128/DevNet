#!/usr/bin/env python
import requests
from requests.auth import HTTPBasicAuth
import pprint

base_url="https://sandboxdnac2.cisco.com:443"
username="devnetuser"
password="Cisco123!"

header = {'content-type': 'application/json'}

# Authneticaiton Token
# To disable urllib3 warning: 
# export PYTHONWARNINGS="ignore:Unverified HTTPS request"
response = requests.post(base_url + '/dna/system/api/v1/auth/token', \
                        auth=HTTPBasicAuth(username, password), \
                        headers=header, verify=False)
token = response.json()['Token']
print(f"Here is my authentication token: {token}")

# Get device information 
header = {'content-type': 'application/json', 'x-auth-token': token}
response = requests.get(base_url + '/dna/intent/api/v1/network-device', \
                        headers=header, \
                        verify=False)
for device in response.json()['response']:
    try: 
        pprint.pprint(device['id'])
        pprint.pprint(device['family'])
    except: 
        print('Unable to retrieve id or family')


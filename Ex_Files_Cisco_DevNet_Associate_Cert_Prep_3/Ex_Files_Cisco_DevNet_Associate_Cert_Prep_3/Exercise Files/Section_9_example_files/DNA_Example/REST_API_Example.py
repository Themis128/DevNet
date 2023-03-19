#!/usr/bin/env python
# Task: Retrieve a list of network devices from Cisco DNA Center Controller
import requests
from requests.auth import HTTPBasicAuth
import pprint

# Step 1. Find possible Lab for practice
# https://developer.cisco.com -> Discover -> Sandbox Remote Labs 
# https://devnetsandbox.cisco.com/RM/Topology
# https://devnetsandbox.cisco.com/RM/Diagram/Index/471eb739-323e-4805-b2a6-d0ec813dc8fc?diagramType=Topology

base_url="https://sandboxdnac2.cisco.com:443"
username="devnetuser"
password="Cisco123!"

# Step 2. Find code examples
# Discover -> Sample Code on GitHub
# http://ciscodevnet.github.io/#/sample-code

# Step 3. Find documentation
# https://developer.cisco.com/docs/ -> Cisco DNA Center
# https://developer.cisco.com/docs/dna-center/

# Authentication: 
# API Quickstart -> Authentication
# https://developer.cisco.com/docs/dna-center/#!cisco-dna-center-v-1-2-6-and-later/authentication

header = {'content-type': 'application/json'}

# Authneticaiton Token
# To disable urllib3 warning: 
# export PYTHONWARNINGS="ignore:Unverified HTTPS request"
response = requests.post(base_url + '/dna/system/api/v1/auth/token', \
                        auth=HTTPBasicAuth(username, password), \
                        headers=header, verify=False)
token = response.json()['Token']
print(f"Here is my authentication token: {token}")

# Step 4. Get specific URL information
# APIs -> Intent API Reference -> Devices
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


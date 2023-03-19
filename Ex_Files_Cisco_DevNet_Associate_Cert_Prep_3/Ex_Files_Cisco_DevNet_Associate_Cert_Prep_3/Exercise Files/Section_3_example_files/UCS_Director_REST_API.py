#!/usr/bin/env python
# Reference: 
# https://developer.cisco.com/site/ucs-mim-ref-api-picker/
# https://developer.cisco.com/learning/modules/ucs-director-rest-api-introduction/ucsd-rest-api-101/step/2
import requests

# Base authentication 
base_url = 'https://10.10.20.101/app/api/rest'
username = 'admin'
passsword = 'ciscopsdt'

# Retrieve API Key
api_key_url = base_url + '?opName=getRESTKey&user=' + username + '&password=' + passsword 
response = requests.get(api_key_url, verify=False)
api_key = response.json()

# Make a request for user profile
headers = {
    'X-Cloupia-Request-Key': api_key
}
user_profile_url = base_url + '?opName=userAPIGetMyLoginProfile'
response = requests.get(user_profile_url, headers=headers, verify=False)
print(response.json())

# example output
"""
(venv) $ python UCS_Director_REST_API.py 
{'serviceResult': {'userId': 'admin', 'firstName': None, 'lastName': None, 'email': 'admin-ucsd@devnet.cisco.com', 'groupName': None, 'groupId': 0, 'role': 'Admin'}, 'serviceError': None, 'serviceName': 'InfraMgr', 'opName': 'userAPIGetMyLoginProfile'}
"""
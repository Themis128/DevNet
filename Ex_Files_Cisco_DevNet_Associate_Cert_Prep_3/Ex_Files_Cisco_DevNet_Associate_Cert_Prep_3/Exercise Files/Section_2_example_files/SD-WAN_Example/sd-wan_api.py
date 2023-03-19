#!/usr/bin/env python3
# Reference: 
# https://developer.cisco.com/learning/lab/sd-wan-rest-api-python/step/1
import requests
import pprint

base_url = "https://sandboxsdwan.cisco.com:8443"
username = "devnetuser"
password = "Cisco123!"

# start autehtnicated session 
# Version 19 and later requires XSRF Token 
session = requests.session()
response = session.post(url=base_url + "/j_security_check",
                        data={"j_username": username, "j_password": password},
                        verify=False
                        )

# GET option for device list 
device_url = base_url + '/dataservice/device'
device_list = session.get(url=device_url, verify=False)
for device in device_list: 
    pprint.pprint(device)




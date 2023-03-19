#!/usr/bin/env python3
# Reference: 
# https://github.com/PacktPublishing/Mastering-Python-Networking-Third-Edition/blob/master/Chapter03/Cisco/cisco_nxapi_2.py
import requests
import json

url='http://172.16.30.53/ins'
switchuser='cisco'
switchpassword='cisco'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show version",
      "version": 1.2
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

print(response['result']['body'])

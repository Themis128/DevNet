#!/usr/bin/env python3
import requests
import json
import pprint

base_url = "https://ios-xe-mgmt.cisco.com"
username = "developer"
password = "C1sco12345"
port = 9443

#requests.packages.urllib3.disable_warnings()
# RFC8040 /restconf/<resource-type>/<yang-module:resource>
# https://<url>/restconf<resource><container><leaf><options> 

# GET request for well known host meta, notice the header for Accepted content
headers = {'Accept': 'application/xrd+xml'}

well_known_host_meta_url = base_url + ":" + str(port) + "/.well-known/host-meta"
response = requests.get(well_known_host_meta_url, auth=(username, password), headers=headers, verify=False)
pprint.pprint(response.content)

# GET request for root URL for RESTCONF resources, can work with 'application/yang-data+xml' 
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

resource_url = base_url + ":" + str(port) + "/restconf/data"
response = requests.get(resource_url, auth=(username, password), headers=headers, verify=False)
pprint.pprint(response.json())

"""
{'ietf-restconf:restconf': {'data': {},
                            'operations': {},
                            'yang-library-version': '2016-06-21'}}

Encourage to step thru each, i.e. https://<url>:<port>/restconf/data?depth=1, https://<url>:<port>/restconf/operations
"""

#pyang -f tree ietf-interfaces.yang

# GET request for specific resources 
interface = "GigabitEthernet1"
interface_url = base_url + ":" + str(port) + "/restconf/data/ietf-interfaces:interfaces/interface=" + interface 

response = requests.get(interface_url, auth=(username, password), headers=headers, verify=False)
pprint.pprint(response.json())

"""
Example output: 
(venv) $ python restconf_example.py 
{'ietf-interfaces:interface': {'description': "MANAGEMENT INTERFACE - DON'T "
                                              'TOUCH ME',
                               'enabled': True,
                               'ietf-ip:ipv4': {'address': [{'ip': '10.10.20.48',
                                                             'netmask': '255.255.255.0'}]},
                               'ietf-ip:ipv6': {},
                               'name': 'GigabitEthernet1',
                               'type': 'iana-if-type:ethernetCsmacd'}}

"""


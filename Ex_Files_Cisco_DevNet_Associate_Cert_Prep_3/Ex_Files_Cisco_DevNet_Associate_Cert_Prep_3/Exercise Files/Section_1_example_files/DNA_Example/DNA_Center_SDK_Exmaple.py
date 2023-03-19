#!/usr/bin/env python
# Reference: 
# https://github.com/cisco-en-programmability/dnacentersdk
from dnacentersdk import api

dnac = api.DNACenterAPI(username="devnetuser",
                        password="Cisco123!",
                        base_url="https://sandboxdnac2.cisco.com:443",
                        version='1.2.10',
                        verify=False)

#devices = dnac.devices.get_device_list(family='Switches and Hubs')
devices = dnac.devices.get_device_list()


for device in devices.response:
    try: 
        print('{:20s}{}'.format(device.hostname, device.upTime))
    except: 
        print('unable to retrieve hostname or uptime')


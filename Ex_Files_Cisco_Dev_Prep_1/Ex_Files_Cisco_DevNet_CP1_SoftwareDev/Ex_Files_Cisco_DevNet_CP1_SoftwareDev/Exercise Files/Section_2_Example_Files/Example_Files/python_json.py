#!/usr/bin/env python
import json
from pprint import pprint as pp

# encoding Python objects in JSON
pp('Encoding Python objects into JSON:')
encode_switch_obj = json.dumps({
                      'name': 's1',
                      'else': ('switch', None, 1.0, 2)
                    })
pp(encode_switch_obj)

# decoding something in JSON
pp('Decoding JSON object back to Python')
decode_switch_obj = json.loads(encode_switch_obj)
pp(decode_switch_obj)

# decoding file
pp('Read JSON file and turn into Python object:')
with open('NX-API_show_version.json', 'r') as f:
    show_version_output = json.loads(f.read())

pp('Show the type of Python object and content:')
pp(type(show_version_output))
pp(show_version_output)

pp('Parse out the NX-OS version value:')
pp(show_version_output['ins_api']['outputs']['output']['body']['nxos_ver_str'])


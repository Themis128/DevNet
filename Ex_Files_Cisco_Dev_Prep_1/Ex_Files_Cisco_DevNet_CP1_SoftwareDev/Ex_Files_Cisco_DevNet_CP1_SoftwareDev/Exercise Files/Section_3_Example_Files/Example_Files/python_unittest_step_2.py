#!/usr/bin/env python
import json
#!/usr/bin/env python
import unittest

# Our software approved version is "9.3(3)"
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        switch_version = switch_os()
        self.assertEqual(switch_version, '9.3(3)')


# write a function that retrieves switch software version
def switch_os():
    # check section 2 if you are not familiar with the steps here
    with open('NX-API_show_version.json', 'r') as f:
        show_version_output = json.loads(f.read())
    switch_os = show_version_output['ins_api']['outputs']['output']['body']['nxos_ver_str']
    return switch_os


if __name__ == '__main__':
    unittest.main()

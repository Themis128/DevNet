#!/usr/bin/env python
import unittest

# Our software approved version is "9.3(3)"
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        switch_version = switch_os()
        self.assertEqual(switch_version, '9.3(3)')


# write a function that retrieves switch software version
def switch_os():
    switch_os = '0.0(0)'
    return switch_os

if __name__ == '__main__':
    unittest.main()


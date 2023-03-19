#!/usr/bin/env python
import unittest

# basics of assertions between in Unittest
# https://docs.python.org/3.8/library/unittest.html
# Have your test start with the name test
class TestStringMethods(unittest.TestCase):
    # assertEqual compares the first two items to make sure they are the same
    # try 'switch'.upper() in the interactive shell
    def test_upper(self):
        self.assertEqual('switch'.upper(), 'SWITCH')

    # assertTrue / assertFalse compare the result to be true or false
    # try 'SWITCH'.isupper() in the interactive shell
    def test_isupper(self):
        self.assertTrue('SWITCH'.isupper())
    
    # try chaning 'SWITCH' to 'sWITCH' and re-run test: python python_unittest.py

if __name__ == '__main__':
    unittest.main()


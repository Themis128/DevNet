#!/usr/bin/env python3
import os
import unittest

class Output(unittest.TestCase):
     def testFile(self):
         file_exist_true_or_false = os.path.exists('/home/echou/LinkedIn_Learning/iosv-1_output.txt')
         self.assertTrue(file_exist_true_or_false, 'iosv-1_output.txt does not exist!')

#
# Name: Carson Pepe
# Student ID: 13926584
# 9/24/2018
#
# Lab 0
# Section 13
# Purpose of Lab: To practice writing more efficient code.

import unittest
import io, sys
from planets import *

class Test_planets(unittest.TestCase):

    def test_01(self):
        sys.stdin = io.StringIO("136")
        sys.stdout = student_output = io.StringIO()
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 51.68 pounds.\nOn Jupiter you would weigh 318.24 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_02(self):
        sys.stdin = io.StringIO("173")
        sys.stdout = student_output = io.StringIO()
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 65.74 pounds.\nOn Jupiter you would weigh 404.82 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_03(self):
        sys.stdin = io.StringIO("210")
        sys.stdout = student_output = io.StringIO()
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 79.8 pounds.\nOn Jupiter you would weigh 491.4 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())

if __name__ == "__main__":
        unittest.main()

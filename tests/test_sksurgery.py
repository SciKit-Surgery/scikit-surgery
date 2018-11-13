# coding=utf-8

"""scikit-surgery tests"""

from sksurgery.ui.sksurgery_demo import run_demo

# Unittest style test case
from unittest import TestCase

class Testsksurgery(TestCase):
    def test_using_unittest_sksurgery(self):
        return_value = run_demo(True, "Hello world")
        self.assertTrue(return_value)


# Pytest style

def test_using_pytest_sksurgery():
    assert run_demo(True, "Hello World") == True


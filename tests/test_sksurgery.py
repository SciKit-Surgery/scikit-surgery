# coding=utf-8

"""scikit-surgery tests"""

from sksurgery.ui.sksurgery_demo import run_demo

def test_using_pytest_sksurgery():
    assert run_demo(True, "Hello World") == True


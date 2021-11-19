"""
example unit test for ExampleClass

list of unittest assert methods:
https://docs.python.org/3/library/unittest.html#assert-methods
"""

# std modules:
from unittest import TestCase
from datetime import datetime

# tested module(s):
from get_station_nearest_to_time import get_station_nearest_to_time


class Test_get_station_nearest_to_time(TestCase):

    def test_lk_station(self):
        """
        time at lk exactly returns lk
        """
        station_row = get_station_nearest_to_time(datetime(2019,9,24, 10, 29))
        # check station_row is what we want
        print("station row is:")
        print(station_row)
        self.assertEqual(station_row['STATION'], "LK/21")
        # ^ same as `assert station_row['STATION'] == "MR"
        
# -*- coding: utf-8 -*-
"""Tests of fordev.generators module."""

import unittest

from fordev.generators import vehicle_brand
from fordev.generators import uf


class TestGenerators(unittest.TestCase):
    def test_vehicle_brand_generator_with_data_only_argument_as_true(self):
        result = vehicle_brand(data_only=True)
        self.assertIsInstance(result, list)
    
    def test_vehicle_brand_generator_with_data_only_argument_as_false(self):
        result = vehicle_brand(data_only=False)
        self.assertIsInstance(result, dict)
        self.assertCountEqual(['msg', 'data'], result.keys())
        self.assertIsInstance(result['msg'], str)
        self.assertIsInstance(result['data'], list)

    def test_if_vehicle_brand_generator_returns_max_and_min_number_of_data(self):
        n_min = vehicle_brand(n=1)
        n_max = vehicle_brand(n=87)
        self.assertGreaterEqual(len(n_min), 1)
        self.assertLessEqual(len(n_max), 87)
    
    def test_if_vehicle_brand_generator_not_exceed_min_and_max_limit_of_return(self):
        with self.assertRaises(ValueError):
            vehicle_brand(n=0)
            vehicle_brand(n=-1)  
            vehicle_brand(n=88)


if __name__ == '__main__':
    unittest.main()

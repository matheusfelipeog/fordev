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


if __name__ == '__main__':
    unittest.main()

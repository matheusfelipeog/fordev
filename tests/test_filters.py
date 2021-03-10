# -*- coding: utf-8 -*-
"""Tests of fordev.filters module."""

import unittest

from fordev.filters import data_format


class TestFilters(unittest.TestCase):
    """Test Class of fordev.filters module."""

    def setUp(self):
        self.data_success_case = {'msg': 'success', 'data': 'data of test'}
        self.data_failed_case = {'msg': 'failed', 'data': 'exception'}

    def test_data_format_with_data_only_argument_as_true(self):
        success_case = data_format(data_only=True, data_dict=self.data_success_case)
        failed_case = data_format(data_only=True, data_dict=self.data_failed_case)

        self.assertEqual('data of test', success_case)
        self.assertDictEqual(self.data_failed_case, failed_case)
    
    def test_data_format_with_data_only_argument_as_false(self):
        success_case = data_format(data_only=False, data_dict=self.data_success_case)
        failed_case = data_format(data_only=False, data_dict=self.data_failed_case)

        self.assertDictEqual(self.data_success_case, success_case)
        self.assertDictEqual(self.data_failed_case, failed_case)

    def test_if_data_format_return_correct_keys_and_values_in_success_and_failed_case(self):
        success_case = data_format(data_only=False, data_dict=self.data_success_case)
        failed_case = data_format(data_only=False, data_dict=self.data_failed_case)

        # Test the return length
        self.assertEqual(2, len(success_case))
        self.assertEqual(2, len(failed_case))

        # Test the return keys
        self.assertIn('msg', success_case.keys())
        self.assertIn('data', success_case.keys())
        self.assertIn('msg', failed_case.keys())
        self.assertIn('data', failed_case.keys())

        # Test the return values
        self.assertEqual('success', success_case['msg'])
        self.assertEqual('data of test', success_case['data'])
        self.assertEqual('failed', failed_case['msg'])
        self.assertEqual('exception', failed_case['data'])


if __name__ == '__main__':
    unittest.main()

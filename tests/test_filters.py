# -*- coding: utf-8 -*-
"""Tests of fordev.filters module."""

import unittest

from fordev.filters import data_format
from fordev.filters import filter_bank_account_info

from tests.fixtures import HTML_OF_BANK_ACCOUNT_RESPONSE


class TestFilters(unittest.TestCase):
    """Test Class of fordev.filters module."""

    def setUp(self):
        self.data_success_case = {'msg': 'success', 'data': 'data of test'}
        self.data_failed_case = {'msg': 'failed', 'data': 'exception'}

    def test_data_format_with_data_only_argument_as_true(self):
        success_case = data_format(data_only=True, data_dict=self.data_success_case)
        failed_case = data_format(data_only=True, data_dict=self.data_failed_case)

        self.assertEqual(success_case, 'data of test')
        self.assertDictEqual(failed_case, self.data_failed_case)
    
    def test_data_format_with_data_only_argument_as_false(self):
        success_case = data_format(data_only=False, data_dict=self.data_success_case)
        failed_case = data_format(data_only=False, data_dict=self.data_failed_case)

        self.assertDictEqual(success_case, self.data_success_case)
        self.assertDictEqual(failed_case, self.data_failed_case)

    def test_if_data_format_return_correct_keys_and_values_in_success_and_failed_case(self):
        success_case = data_format(data_only=False, data_dict=self.data_success_case)
        failed_case = data_format(data_only=False, data_dict=self.data_failed_case)

        # Test the return length
        self.assertEqual(len(success_case), 2)
        self.assertEqual(len(failed_case), 2)

        # Test the return keys
        self.assertIn('msg', success_case.keys())
        self.assertIn('data', success_case.keys())
        self.assertIn('msg', failed_case.keys())
        self.assertIn('data', failed_case.keys())

        # Test the return values
        self.assertEqual(success_case['msg'], 'success')
        self.assertEqual(success_case['data'], 'data of test')
        self.assertEqual(failed_case['msg'], 'failed')
        self.assertEqual(failed_case['data'], 'exception')

    def test_bank_account_filter(self):
        result = filter_bank_account_info(html=HTML_OF_BANK_ACCOUNT_RESPONSE)

        self.assertEqual(len(result.keys()), 5)
        self.assertCountEqual(['Conta Corrente', 'Agência', 'Banco', 'Cidade', 'Estado'], result.keys())
        self.assertCountEqual(['1370571-2', '1255', 'Bradesco', 'Caieiras', 'SP'], result.values())


if __name__ == '__main__':
    unittest.main()

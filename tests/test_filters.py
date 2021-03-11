# -*- coding: utf-8 -*-
"""Tests of fordev.filters module."""

import unittest

from fordev.filters import data_format
from fordev.filters import filter_bank_account_info
from fordev.filters import filter_vehicle_info
from fordev.filters import filter_credit_card_info

from tests.fixtures import HTML_OF_BANK_ACCOUNT
from tests.fixtures import HTML_OF_VEHICLE_INFOS
from tests.fixtures import HTML_OF_CREDIT_CARD_INFOS


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
        self.assertCountEqual(['msg', 'data'], success_case.keys())
        self.assertCountEqual(['msg', 'data'], failed_case.keys())

        # Test the return values
        self.assertEqual(success_case['msg'], 'success')
        self.assertEqual(success_case['data'], 'data of test')
        self.assertEqual(failed_case['msg'], 'failed')
        self.assertEqual(failed_case['data'], 'exception')

    def test_bank_account_filter(self):
        result = filter_bank_account_info(html=HTML_OF_BANK_ACCOUNT)

        self.assertEqual(len(result.keys()), 5)
        self.assertCountEqual(['Conta Corrente', 'Agência', 'Banco', 'Cidade', 'Estado'], result.keys())
        self.assertCountEqual(['1370571-2', '1255', 'Bradesco', 'Caieiras', 'SP'], result.values())

    def test_vehicle_info_filter(self):
        result = filter_vehicle_info(html=HTML_OF_VEHICLE_INFOS)

        self.assertEqual(len(result.keys()), 6)
        self.assertCountEqual(['Marca', 'Modelo', 'Ano', 'RENAVAM', 'Placa', 'Cor'], result.keys())
        self.assertCountEqual(['Rolls-Royce', 'Wraith 6.6 V12 Aut.', '2014', '41047812580', 'HVE-9411', 'Verde'], result.values())
    
    def test_credit_card_info_filter(self):
        result = filter_credit_card_info(html=HTML_OF_CREDIT_CARD_INFOS)

        self.assertEqual(len(result.keys()), 3)
        self.assertCountEqual(['Número do Cartão', 'Data de Validade', 'Código Segurança (CVV)'], result.keys())
        self.assertCountEqual(['5016 0926 0945 3715', '11/02/2023', '812'], result.values())


if __name__ == '__main__':
    unittest.main()

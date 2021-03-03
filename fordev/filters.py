# -*- coding: utf-8 -*-
"""
fordev.filters
--------------

This module is used to filter data contained in HTML structures
and json format in Fordev module.
"""

__all__ = [
    'data_format',
    'filter_bank_account_info',
    'filter_vehicle_info',
    'filter_credit_card_info',
    'filter_company_info',
    'filter_city_name'
]

from .__about__ import __version__
from .__about__ import __author__
from .__about__ import __email__
from .__about__ import __author_github__
from .__about__ import __project_github__

from bs4 import BeautifulSoup


def data_format(data_only: bool, data_dict: dict):
    """Filter the data format return."""
    
    if data_only and data_dict['msg'] == 'success':
        return data_dict['data']
    
    return data_dict


def filter_bank_account_info(html: str) -> dict:
    """Filter the bank account info in the data of the HTML structure.

    Parameter
    ---------
    html
        Content in html structure.
    """

    soup = BeautifulSoup(html, 'html.parser')

    # Get all the labels to use as a key in the dictionary return.
    labels = [div.text for div in soup.find_all('div', 'output-subtitle')]

    # Get all the data to use as a value in the dictionary return.
    data_of_bank_account = [div.text for div in soup.find_all('div', 'output-txt')]

    data_dict = dict(
        zip(labels, data_of_bank_account)
    )

    return data_dict


def filter_vehicle_info(html: str) -> dict:
    """Filter the vehicle info in the data of the HTML structure.

    Parameter
    ---------
    html
        Content in html structure.
    """

    soup = BeautifulSoup(html, 'html.parser')

    # Get all the labels to use as a key in the dictionary return.
    labels = [div.text[:-1] for div in soup.find_all('strong')]

    # Get all the data to use as a value in the dictionary return.
    data_of_vehicle = [input_.get('value') for input_ in soup.find_all('input', 'margem_menor')]

    data_dict = dict(
        zip(labels, data_of_vehicle)
    )

    return data_dict


def filter_credit_card_info(html: str) -> dict:
    """Filter the credit card info in the data of the HTML structure.

    Parameter
    ---------
    html
        Content in html structure.
    """

    soup = BeautifulSoup(html, 'html.parser')

    # Get all the labels to use as a key in the dictionary return.
    labels = [div.text for div in soup.find_all('div', 'output-subtitle')]

    # Get all the data to use as a value in the dictionary return.
    data_of_credit_card = [div.text.strip() for div in soup.find_all('div', 'output-txt')]

    data_dict = dict(
        zip(labels, data_of_credit_card)
    )

    return data_dict


def filter_company_info(html: str) -> dict:
    """Filter the company info in the data of the HTML structure.

    Parameter
    ---------
    html
        Content in html structure.
    """

    soup = BeautifulSoup(html, 'html.parser')

    # Get all the labels to use as a key in the dictionary return.
    labels = [div.text[:-1] for div in soup.find_all('strong')]

    # Get all the data to use as a value in the dictionary return.
    data_of_company = [input_.get('value') for input_ in soup.find_all('input', 'margem_menor')]

    data_dict = dict(
        zip(labels, data_of_company)
    )

    return data_dict


def filter_city_name(html: str) -> list:
    """Filter the city name in the data of the HTML structure.

    Parameter
    ---------
    html
        Content in html structure.
    """

    soup = BeautifulSoup(html, 'html.parser')

    # Get text (city name) in option tag.
    return [
        option.text for option in soup.find_all('option')[1:]
    ]

# -*- coding: utf-8 -*-
"""This module is used to filter data contained in HTML structures."""

# --- Third-party libraries ---
from bs4 import BeautifulSoup


def filter_bank_account_info(html: str) -> dict:
    """Filter the bank account info in the data of the HTML structure.

    Keyword arguments:

    `html: str` - Content in html structure.
    """

    soup = BeautifulSoup(html, 'html.parser')

    # Get all the labels to use as a key in the dictionary return.
    labels = [div.text for div in soup.find_all('div', 'output-subtitle')]

    # Get all the data to use as a value in the dictionary return.
    data_of_bank_account = [div.text for div in soup.find_all('div', 'output-txt')]

    # Join labels with bank account data
    # and convert to a dictionary in the key-value format respectively.
    data_dict = dict(
        zip(labels, data_of_bank_account)
    )

    return data_dict


def filter_vehicle_info(html: str) -> dict:
    """Filter the vehicle info in the data of the HTML structure.

    Keyword arguments:

    `html: str` - Content in html structure.
    """

    soup = BeautifulSoup(html, 'html.parser')

    # Get all the labels to use as a key in the dictionary return.
    labels = [div.text[:-1] for div in soup.find_all('strong')]

    # Get all the data to use as a value in the dictionary return.
    data_of_vehicle = [input_.get('value') for input_ in soup.find_all('input', 'margem_menor')]

    # Join labels with vehicle data
    # and convert to a dictionary in the key-value format respectively.
    data_dict = dict(
        zip(labels, data_of_vehicle)
    )

    return data_dict


def filter_city_name(html: str) -> list:
    """Filter the city name in the data of the HTML structure.

    Keyword arguments:

    `html: str` - Content in html structure.
    """

    soup = BeautifulSoup(html, 'html.parser')

    # Get text (city name) in option tag.
    return [
        option.text for option in soup.find_all('option')[1:]
    ]

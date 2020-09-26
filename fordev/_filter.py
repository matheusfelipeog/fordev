# -*- coding: utf-8 -*-
"""This module is used to filter data contained in HTML structures."""

# --- Third-party libraries ---
from bs4 import BeautifulSoup


def filter_city_name(html: str):
    """Filter the city name in the data of the HTML structure.

    Keyword arguments:

    `html: str` - Content in html structure.
    """

    soup = BeautifulSoup(html, 'html.parser')

    # Get text (city name) in option tag.
    return [
        option.text for option in soup.find_all('option')[1:]
    ]

# -*- coding: utf-8 -*-
"""This module is a base for create requests in 4dev API."""

# --- Standard libraries ----
from random import choice

# --- Third-party libraries ---
import requests

# --- Local libraries ---
from ._const import URL_4DEV_API
from ._const import LIST_OF_USER_AGENT


def _random_user_agent() -> str:
    """A random user agent string."""

    return choice(LIST_OF_USER_AGENT)


def _create_headers(referer: str) -> dict:
    """Create headers for use in requests module.
    
    Keyword arguments:

    `referer: str` - Reference of the action to be performed.
    """

    headers = {
        "user-agent": _random_user_agent(),
        "authority": "www.4devs.com.br",
        "method": "POST",
        "path": "/ferramentas_online.php",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "pt,en-US;q=0.9,en;q=0.8",
        "content-length": "38",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "dnt": "1",
        "origin": "https://www.4devs.com.br",
        "referer": "https://www.4devs.com.br/{}".format(referer),
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest"
    }

    return headers


def fordev_request(referer: str, payload: dict) -> dict:
    """Create request for 4dev API and get your content.
    
    Keyword arguments:

    `referer: str` - Reference of the action to be performed.

    `payload: dict` - A data dictionary containing the action and other data to request.
    """

    try:
        response = requests.post(
            url=URL_4DEV_API,
            headers=_create_headers(referer),
            data=payload
        )

        # Check if the status code is between 400 to 600,
        # if yes it returns an error message and the error.
        try:
            response.raise_for_status()
        except requests.HTTPError as err:
            return {
                'msg': 'HTTP error',
                'error': err
            }

        # On success, returns a message and data.
        return {
            'msg': 'success',
            'data': response.text
        }

    # Get any other request errors and return msg and error.
    except requests.RequestException as err:
        return {
            'msg': 'failed',
            'error': err
        }

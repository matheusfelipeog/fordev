# -*- coding: utf-8 -*-
"""
fordev.core
-----------

This module is a core for create requests in 4dev API.
"""

__all__ = ['fordev_request']

from .__about__ import __version__
from .__about__ import __author__
from .__about__ import __email__
from .__about__ import __github__

from random import choice

import requests

from .consts import URL_4DEV_API
from .consts import USER_AGENTS


def _random_user_agent() -> str:
    """A random user agent string."""

    return choice(USER_AGENTS)


def _create_headers(content_length: int, referer: str) -> dict:
    """Create headers for use in requests module.
    
    Parameters
    ----------
    content_length
        Indicates the size of the entity-body, in bytes, sent to the recipient.

    referer
        Reference of the action to be performed.
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
        "content-length": str(content_length),
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


def fordev_request(content_length: int, referer: str, payload: dict) -> dict:
    """Create request for 4dev API and get your content.
    
    Parameters
    ----------
    content_length
        Indicates the size of the entity-body, in bytes, sent to the recipient.

    referer
        Reference of the action to be performed.

    payload
        A data dictionary containing the action and other data to request.
    """

    try:
        response = requests.post(
            url=URL_4DEV_API,
            headers=_create_headers(content_length, referer),
            data=payload
        )

        # Check if the status code is between 400 to 600,
        # if yes it returns an error message and the error.
        response.raise_for_status()
        
        # On success, returns a message and data.
        return {
            'msg': 'success',
            'data': response.text
        }

    except (requests.RequestException, requests.HTTPError) as err:
        return {
            'msg': 'failed',
            'error': err
        }

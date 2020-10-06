# -*- coding: utf-8 -*-
"""Module for validating data.

Options:
    CNH - Check if CNH Code is valid;
    CNPJ - Check if CNPJ Code is valid.
"""

from .__about__ import __version__

from .__about__ import __author__
from .__about__ import __email__
from .__about__ import __github__

__version__ = __version__
__author__ = f'{__author__} <{__email__}> and <{__github__}>'

# --- Local libraries ---
from ._base import fordev_request


def cnh(cnh_code: str, data_only: bool=True) -> bool:
    """Check if CNH code is valid.
    
    Keyword arguments:

    `cnh_code: str` - CNH code for check.
    
    `data_only: bool` - If True, return data only. If False, return msg and data/error.
    """

    content_length = 36
    referer = 'validador_cnh'
    payload = {
        'acao': 'validar_cnh',
        'txt_cnh': cnh_code
    }

    r = fordev_request(content_length, referer, payload)

    # Check if is valid and replace data
    is_valid = r['data'].split(' - ')[-1].lower() == 'verdadeiro'
    r['data'] = is_valid

    if data_only and r['msg'] == 'success':
        return r['data']

    return r


def cnpj(cnpj_code: str, data_only: bool=True) -> bool:
    """Check if CNPJ code is valid.
    
    Keyword arguments:

    `cnpj_code: str` - CNPJ code for check.
    
    `data_only: bool` - If True, return data only. If False, return msg and data/error.
    """

    content_length = 47
    referer = 'validador_cnpj'
    payload = {
        'acao': 'validar_cnpj',
        'txt_cnpj': cnpj_code
    }

    r = fordev_request(content_length, referer, payload)

    # Check if is valid and replace data
    is_valid = r['data'].split(' - ')[-1].lower() == 'verdadeiro'
    r['data'] = is_valid

    if data_only and r['msg'] == 'success':
        return r['data']

    return r

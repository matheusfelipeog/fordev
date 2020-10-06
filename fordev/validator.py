# -*- coding: utf-8 -*-
"""Module for validating data.

Options:
    CNH - Check if CNH Code is valid;
    CNPJ - Check if CNPJ Code is valid;
    CPF - Check if CPF Code is valid;
    PIS/PASEP - Check if PIS/PASEP Code is valid;
    RENAVAM - Check if RENAVAM Code is valid.
    RG - Check if RG Code is valid.
"""

from .__about__ import __version__

from .__about__ import __author__
from .__about__ import __email__
from .__about__ import __github__

__version__ = __version__
__author__ = f'{__author__} <{__email__}> and <{__github__}>'

# --- Local libraries ---
from ._base import fordev_request


def _data_verification_and_normalize(data: dict) -> dict:
    """"Check if data key exists and if value is valid. If true, replace data for new format.
    
    Keyword arguments:

    `data: dict` - Data dictionary for verification and format change
    """

    data = data.copy()

    if data.get('data', False):
        is_valid = data['data'].split(' - ')[-1].lower() == 'verdadeiro'
        data['data'] = is_valid
    
    return data


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

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

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

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    if data_only and r['msg'] == 'success':
        return r['data']

    return r


def cpf(cpf_code: str, data_only: bool=True) -> bool:
    """Check if CPF code is valid.
    
    Keyword arguments:

    `cpf_code: str` - CPF code for check.
    
    `data_only: bool` - If True, return data only. If False, return msg and data/error.
    """

    content_length = 39
    referer = 'validador_cpf'
    payload = {
        'acao': 'validar_cpf',
        'txt_cpf': cpf_code
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    if data_only and r['msg'] == 'success':
        return r['data']

    return r


def pis_pasep(pis_pasep_code: str, data_only: bool=True) -> bool:
    """Check if PIS/PASEP code is valid.
    
    Keyword arguments:

    `pis_pasep_code: str` - PIS/PASEP code for check.
    
    `data_only: bool` - If True, return data only. If False, return msg and data/error.
    """

    content_length = 39
    referer = 'validador_pis_pasep'
    payload = {
        'acao': 'validar_pis',
        'txt_pis': pis_pasep_code
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    if data_only and r['msg'] == 'success':
        return r['data']

    return r


def renavam(renavam_code: str, data_only: bool=True) -> bool:
    """Check if RENAVAM code is valid.
    
    Keyword arguments:

    `renavam_code: str` - RENAVAM code for check.
    
    `data_only: bool` - If True, return data only. If False, return msg and data/error.
    """

    content_length = 43
    referer = 'validador_de_renavam'
    payload = {
        'acao': 'validar_renavam',
        'txt_renavam': renavam_code
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    if data_only and r['msg'] == 'success':
        return r['data']

    return r


def rg(rg_code: str, data_only: bool=True) -> bool:
    """Check if RG code is valid.
    
    Keyword arguments:

    `rg_code: str` - RG code for check.
    
    `data_only: bool` - If True, return data only. If False, return msg and data/error.
    """

    content_length = 35
    referer = 'validador_rg'
    payload = {
        'acao': 'validar_rg',
        'txt_rg': rg_code
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    if data_only and r['msg'] == 'success':
        return r['data']

    return r
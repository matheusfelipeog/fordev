# -*- coding: utf-8 -*-
"""Module for validating data.

Options:
    Certificate - Check if Certificate Code is valid;
    CNH - Check if CNH Code is valid;
    CNPJ - Check if CNPJ Code is valid;
    CPF - Check if CPF Code is valid;
    PIS/PASEP - Check if PIS/PASEP Code is valid;
    RENAVAM - Check if RENAVAM Code is valid;
    RG - Check if RG Code is valid;
    Voter Title - Check if Voter Title Code is valid;
    State Registration - Check if State Registration Code is valid.
"""

from .__about__ import __version__

from .__about__ import __author__
from .__about__ import __email__
from .__about__ import __github__

__version__ = __version__
__author__ = f'{__author__} <{__email__}> and <{__github__}>'

# --- Local libraries ---
from ._base import fordev_request

from ._const import ALL_UF_CODE


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


def certificate(certificate_code: str, data_only: bool=True) -> bool:
    """Check if Certificate(birth, wedding, religious wedding and death) code is valid.
    
    Keyword arguments:

    `certificate_code: str` - Certificate code for check.
    
    `data_only: bool` - If True, return data only. If False, return msg and data/error.
    """

    content_length = 75
    referer = 'validador_certidoes'
    payload = {
        'acao': 'validar_certidao',
        'txt_certidao': certificate_code
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    if data_only and r['msg'] == 'success':
        return r['data']

    return r


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


def voter_title(voter_title_code: str, data_only: bool=True) -> bool:
    """Check if Voter Title code is valid.
    
    Keyword arguments:

    `voter_title_code: str` - Voter Title code for check.
    
    `data_only: bool` - If True, return data only. If False, return msg and data/error.
    """

    content_length = 59
    referer = 'validador_titulo_de_eleitor'
    payload = {
        'acao': 'validar_titulo_eleitor',
        'txt_titulo_eleitor': voter_title_code
    }

    r = fordev_request(content_length, referer, payload)

    if r.get('data', False):
        is_valid = r['data'].split(' - ')[-2].lower() == 'verdadeiro'
        r['data'] = is_valid

    if data_only and r['msg'] == 'success':
        return r['data']

    return r


def state_registration(state: str, state_registration_code: str, data_only: bool=True) -> bool:
    """Check if State Registration code is valid.
    
    Keyword arguments:

    `state: str` - State UF(Unidade Federativa) code.
        More info about UF in: https://pt.wikipedia.org/wiki/Subdivis%C3%B5es_do_Brasil 

    `state_registration_code: str` - State Registration code for check.
    
    `data_only: bool` - If True, return data only. If False, return msg and data/error.
    """

    state = state.upper()

    # Check if state is invalid. If true, raise exception.
    if state not in ALL_UF_CODE:
        msg_error = f'The UF code "{state}" is invalid. Enter a valid UF code. Ex: SP, RJ, PB...'
        msg_error += ' More info about UF in: https://pt.wikipedia.org/wiki/Subdivis%C3%B5es_do_Brasil'

        raise ValueError(msg_error)

    content_length = 48
    referer = 'validar_inscricao_estadual'
    payload = {
        'acao': 'validar_ie',
        'txt_ie': state_registration_code,
        'estado': state
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    if data_only and r['msg'] == 'success':
        return r['data']

    return r

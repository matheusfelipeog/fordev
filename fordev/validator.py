# -*- coding: utf-8 -*-
"""
fordev.validator
----------------

This module validate the data using the 4devs website.

Use help function for more information:

>>> from fordev import validator
>>> help(validator)
Help on module fordev.validator in fordev:

NAME
    fordev.validator

DESCRIPTION
(...)

Or consult the official documentation.

Note
----
Most of the functions of the ``fordev.validator`` module contain
common parameter, ``data_only`` is a case.

More details in next section.

Parameter
---------
data_only: bool
    If ``True``, return data only. If ``False``, return msg and data or error.

OBS: These are common parameters in the functions
of the ``fordev.validator`` module.
"""

__all__ = [
    'credit_card',
    'bank_account',
    'certificate',
    'cnh',
    'cnpj',
    'cpf',
    'pis_pasep',
    'renavam',
    'rg',
    'voter_title',
    'state_registration',
]

from .__about__ import __version__
from .__about__ import __author__
from .__about__ import __email__
from .__about__ import __github__

from .core import fordev_request

from .const import ALL_UF_CODE
from .const import ALL_BANK_FLAGS_2


def _data_verification_and_normalize(data: dict) -> dict:
    """"Check if data key exists and if value is valid.
    If true, replace data for new format.
    
    Parameter
    ---------
    data
        Data dictionary for verification and format change.
    """

    data = data.copy()

    if data.get('data', False):
        is_valid = data['data'].split(' - ')[-1].lower() == 'verdadeiro'
        data['data'] = is_valid
    
    return data


def credit_card(flag: int, credit_card_code: str, data_only: bool=True) -> bool:
    """Check if credit card code is valid.
    
    Parameters
    ----------
    flag
        Flag of the credit card that wants to validation the credit card information.
            Options:
                1 = MasterCard
                2 = Visa 16 Dígitos
                3 = Visa Electron
                4 = American Express
                5 = Diners Club
                6 = Discover
                7 = enRoute
                8 = JCB
                9 = Maestro
                10 = Solo
                11 = Switch
                12 = Laser

    credit_card_code
        Credit Card Code for check.
   """

    # Check if bank code is invalid. If true, raise exception.
    if not (1 <= flag <= 12):
        msg_error = f'The flag credit card code value "{flag}" is invalid. Enter a valid flag credit card code.'
        msg_error += f' The range is 1 to 12.'

        raise ValueError(msg_error)

    flag = ALL_BANK_FLAGS_2[flag]

    content_length = 68
    referer = 'validador_numero_cartao_credito'
    payload = {
        'acao': 'validar_cc',
        'txt_cc': credit_card_code,
        'bandeira': flag
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    if data_only and r['msg'] == 'success':
        return r['data']

    return r


def bank_account(bank: int, agency: str, account: str, data_only: bool=True) -> bool:
    """Check if bank account data is valid.
    
    Parameters
    ----------
    bank
        Flag of the bank that wants to validation the account information.
            Options:
                1 = Banco do Brasil
                2 = Bradesco
                3 = Citibank
                4 = Itaú
                5 = Santander
    
    agency
        Code of bank agency.

    account
        Code of bank account.
   """

    # Check if bank code is invalid. If true, raise exception.
    if not (1 <= bank <= 5):
        msg_error = f'The bank code value "{bank}" is invalid. Enter a valid bank code.'
        msg_error += f' The range is 1 to 5.'

        raise ValueError(msg_error)

    # Replace the bank number with the bank code used in 4devs.
    bank = [2, 121, 85, 120, 151][bank - 1]  # Use the index for get the bank code.

    content_length = 66
    referer = 'validador_conta_bancaria'
    payload = {
        'acao': 'validar_conta_bancaria',
        'banco': bank,
        'agencia': agency,
        'conta': account
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    if data_only and r['msg'] == 'success':
        return r['data']

    return r


def certificate(certificate_code: str, data_only: bool=True) -> bool:
    """Check if Certificate(birth, wedding, religious wedding and death) code is valid.
    
    Parameter
    ---------
    certificate_code
        Certificate code for check.
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
    
    Parameter
    ---------
    cnh_code
        CNH code for check.
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
    
    Parameter
    ---------
    cnpj_code
        CNPJ code for check.
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
    
    Parameter
    ---------
    cpf_code
        CPF code for check.
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
    
    Parameter
    ---------
    pis_pasep_code
        PIS/PASEP code for check.
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
    
    Parameter
    ---------
    renavam_code
        RENAVAM code for check.
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
    
    Parameter
    ---------
    rg_code
        RG code for check.
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
    
    Parameter
    ---------
    voter_title_code
        Voter Title code for check.
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
    
    Parameters
    ----------
    state
        State UF(Unidade Federativa) code.
        
        More info about UF in: https://pt.wikipedia.org/wiki/Subdivis%C3%B5es_do_Brasil 

    state_registration_code
        State Registration code for check.
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

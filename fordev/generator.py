# -*- coding: utf-8 -*-
"""Module for generating random data.

Options:
    CNH - Carteira Nacional de Habilitação;
    CPF - Cadastro de Pessoas Físicas;
    CNPJ - Cadastro Nacional da Pessoa Jurídica.
"""

# --- Local libraries ---
from ._base import fordev_request

from ._const import ALL_UF_CODE


def cnh(data_only: bool=True) -> str:
    """Random generate of CNH(Carteira Nacional de Habilitação).
    
    Keyword arguments:

    `data_only: bool` - If True, return data only. If False, return msg and data/error.
    """

    content_length = 14
    referer = 'gerador_de_cnh'
    payload = {'acao': 'gerar_cnh'}

    r = fordev_request(content_length, referer, payload=payload)

    if data_only and r['msg'] == 'success':
        return r['data']

    return r


def cpf(format: bool=True, state: str='', data_only: bool=True) -> str:
    """Random generate of CPF(Cadastro de Pessoas Físicas).
    
    Keyword arguments:

    `format: bool` - If True, returns formatted data how "123.456.789-10". If false, formatted data how "12345678910".

    `state: str` - State UF(Unidade Federativa) code for generating the CPF. <Optional Parameter>.
        More info about UF in: https://pt.wikipedia.org/wiki/Subdivis%C3%B5es_do_Brasil 

    `data_only: bool` - If True, return data only. If False, return msg and data/error.
    """

    state = state.upper()

    # Check if state is invalid. If true, raise exception.
    if state != '' and state not in ALL_UF_CODE:
        msg_error = f'The UF code "{state}" is invalid. Enter a valid UF code. Ex: SP, RJ, PB...'
        msg_error += ' More info about UF in: https://pt.wikipedia.org/wiki/Subdivis%C3%B5es_do_Brasil'

        raise ValueError(msg_error)

    content_length = 38 if state == '' else 40
    referer = 'gerador_de_cpf'
    payload = {
        'acao': 'gerar_cpf',
        'pontuacao': 'S' if format else 'N',
        'cpf_estado': state
    }

    r = fordev_request(content_length, referer, payload=payload)

    if data_only and r['msg'] == 'success':
        return r['data']
    
    return r


def cnpj(format: bool=True, data_only: bool=True) -> str:
    """Random generate of CNPJ(Cadastro Nacional da Pessoa Jurídica).
    
    Keyword arguments:

    `format: bool` - If True, returns formatted data how "12.345.678/0009-10". If false, formatted data how "12345678000910".

    `data_only: bool` - If True, return data only. If False, return msg and data/error.
    """

    content_length = 27
    referer = 'gerador_de_cnpj'
    payload = {
        'acao': 'gerar_cnpj',
        'pontuacao': 'S' if format else 'N',
    }

    r = fordev_request(content_length, referer, payload=payload)

    if data_only and r['msg'] == 'success':
        return r['data']
    
    return r

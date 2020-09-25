# -*- coding: utf-8 -*-
"""Module for generating random data.

Options:
    CNH - Carteira Nacional de Habilitação;
    CPF - Cadastro de Pessoas Físicas;
    CNPJ - Cadastro Nacional da Pessoa Jurídica;
    RG - Registro Geral of emitter SSP-SP;
    Voter Title - Voter Title for the selected state.
    People Data - Generate random people data.
"""

# --- Standard libraries ----
from json import loads as json_loads

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


def rg(format: bool=True, data_only: bool=True) -> str:
    """Random generate of RG(Registro Geral) of emitter SSP-SP.
    
    Keyword arguments:

    `format: bool` - If True, returns formatted data how "12.345.678-9". If false, formatted data how "123456789".

    `data_only: bool` - If True, return data only. If False, return msg and data/error.
    """

    content_length = 25
    referer = 'gerador_de_rg'
    payload = {
        'acao': 'gerar_rg',
        'pontuacao': 'S' if format else 'N',
    }

    r = fordev_request(content_length, referer, payload=payload)

    if data_only and r['msg'] == 'success':
        return r['data']
    
    return r


def voter_title(state: str, data_only: bool=True) -> str:
    """Random generation of Voter Title for the selected state.
    
    Keyword arguments:

    `state: str` - State UF(Unidade Federativa) code for generating the Voter Title.
        More info about UF in: https://pt.wikipedia.org/wiki/Subdivis%C3%B5es_do_Brasil 

    `data_only: bool` - If True, return data only. If False, return msg and data/error.
    """

    state = state.upper()

    # Check if state is invalid. If true, raise exception.
    if state not in ALL_UF_CODE:
        msg_error = f'The UF code "{state}" is invalid. Enter a valid UF code. Ex: SP, RJ, PB...'
        msg_error += ' More info about UF in: https://pt.wikipedia.org/wiki/Subdivis%C3%B5es_do_Brasil'

        raise ValueError(msg_error)

    content_length = 35
    referer = 'gerador_de_titulo_de_eleitor'
    payload = {
        'acao': 'gerar_titulo_eleitor',
        'estado': state
    }

    r = fordev_request(content_length, referer, payload=payload)

    if data_only and r['msg'] == 'success':
        return r['data']
    
    return r


def people(
        n: int=1,
        sex: str='R',
        age: int=0,
        state: str='',
        format: bool=True,
        data_only: bool=True
    ) -> str:
    """Random generation of Voter Title for the selected state.
    
    Keyword arguments:

    `n: int` - The number of people data generated. The range is 1 to 30 peoples.

    `sex: str` - "M", "F" or "R" is equal a "Male", "Feminine" and "Random" respectively. Default is "R".

    `age: int` - Age of people generated. The range is 18 to 80 age.

    `state: str` - State UF(Unidade Federativa) code for generating the people.
        More info about UF in: https://pt.wikipedia.org/wiki/Subdivis%C3%B5es_do_Brasil

    `format: bool` - If True, returns formatted data. If it is false, there is no formatted data.

    `data_only: bool` - If True, return data only. If False, return msg and data/error.
    """
    
    # Normalize
    sex = sex.upper()
    state = state.upper()

    # Check if number of people is invalid. If true, raise exception.
    if not (1 <= n <= 30):
        msg_error = f'The n value "{n}" is invalid. Enter a valid number of people.'
        msg_error += f' The range is 1 to 30 peoples.'

        raise ValueError(msg_error)

    # Check if sex is invalid. If true, raise exception.
    if sex not in ['M', 'F', 'R']:
        msg_error = f'The sex "{sex}" is invalid. Enter a valid sex.'
        msg_error += f' Ex: "M" = Male, "F" = Feminine or "R" = Random.'

        raise ValueError(msg_error)

    # Check if age is invalid. If true, raise exception.
    if not (18 <= age <= 80) and age != 0:
        msg_error = f'The age "{age}" is invalid. Enter a valid age.'
        msg_error += f' The range is 18 to 80 age'

        raise ValueError(msg_error)

    # Check if state is invalid. If true, raise exception.
    if state != '' and state not in ALL_UF_CODE:
        msg_error = f'The UF code "{state}" is invalid. Enter a valid UF code. Ex: SP, RJ, PB...'
        msg_error += ' More info about UF in: https://pt.wikipedia.org/wiki/Subdivis%C3%B5es_do_Brasil'

        raise ValueError(msg_error)

    content_length = 99  # Max of bytes for generate people in all possibilities.
    referer = 'gerador_de_pessoas'
    payload = {
        'acao': 'gerar_pessoa',
        'sexo': 'H' if sex == 'M' else 'M' if sex == 'F' else 'I',  # H, M and I flags are used in 4devs for filter.
        'pontuacao': 'S' if format else 'N',
        'idade': age,
        'cep_estado': state,
        'txt_qtde': n,

        # If the state is not selected, a default flag is used for the city ('Selecione o estado!') or
        # If the state is selected and city is not selected, a default flag is used for the city ('').
        'cep_cidade': 'Selecione o estado!' if state == '' else ''
    }

    r = fordev_request(content_length, referer, payload=payload)

    if data_only and r['msg'] == 'success':
        return json_loads(r['data'])
    
    if r['msg'] == 'success':

        # Convert data in str to dict.
        r['data'] = json_loads(r['data'])

        return r
    
    # In case of failure, return msg status and msg error.
    return r

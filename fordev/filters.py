"""
fordev.filters
--------------

Este módulo é usado para filtrar os dados contidos na estrutura HTML
retornada pela API do site 4devs e converter para uma estrutura de
dicionário Python.
"""

__all__ = [
    'data_format',
    'filter_bank_account_info',
    'filter_vehicle_info',
    'filter_credit_card_info',
    'filter_company_info',
    'filter_city_name'
]

from bs4 import BeautifulSoup


def data_format(data_only: bool, data_dict: dict) -> dict:
    """Filtra os dados conforme especificado."""

    if data_only and data_dict['msg'] == 'success':
        return data_dict['data']

    return data_dict


def filter_bank_account_info(html: str) -> dict:
    """Filtra dados de conta bancária contidos na estrutura HTML.

    Parameters
    ----------
    html
        Uma estrutra HTML contendo dados de conta bancária
        retornados pela API do site 4devs.
    """

    soup = BeautifulSoup(html, 'html.parser')

    labels = [div.text for div in soup.find_all('div', 'output-subtitle')]

    data_of_bank_account = [div.text for div in soup.find_all('div', 'output-txt')]

    data_dict = dict(
        zip(labels, data_of_bank_account)
    )

    return data_dict


def filter_vehicle_info(html: str) -> dict:
    """Filtra dados de veículo contido na estrutura HTML.

    Parameters
    ----------
    html
        Uma estrutra HTML contendo dados de veículo
        retornados pela API do site 4devs.
    """

    soup = BeautifulSoup(html, 'html.parser')

    labels = [div.text[:-1] for div in soup.find_all('strong')]

    data_of_vehicle = [input_.get('value') for input_ in soup.find_all('input', 'margem_menor')]

    data_dict = dict(
        zip(labels, data_of_vehicle)
    )

    return data_dict


def filter_credit_card_info(html: str) -> dict:
    """Filtra dados de cartão de crédito contidos na estrutura HTML.

    Parameters
    ----------
    html
        Uma estrutra HTML contendo dados de cartão de crédito
        retornados pela API do site 4devs.
    """

    soup = BeautifulSoup(html, 'html.parser')

    labels = [div.text for div in soup.find_all('div', 'output-subtitle')]

    data_of_credit_card = [div.text.strip() for div in soup.find_all('div', 'output-txt')]

    data_dict = dict(
        zip(labels, data_of_credit_card)
    )

    return data_dict


def filter_company_info(html: str) -> dict:
    """Filtra dados de companhia (empresa/organização) contidos na estrutura HTML.

    Parameters
    ----------
    html
        Uma estrutra HTML contendo dados de companhia (empresa/organização)
        retornados pela API do site 4devs.
    """

    soup = BeautifulSoup(html, 'html.parser')

    labels = [div.text[:-1] for div in soup.find_all('strong')]

    data_of_company = [input_.get('value') for input_ in soup.find_all('input', 'margem_menor')]

    data_dict = dict(
        zip(labels, data_of_company)
    )

    return data_dict


def filter_city_name(html: str) -> list:
    """Filtra dados de cidade contidos na estrutura HTML.

    Parameters
    ----------
    html
        Uma estrutra HTML contendo dados de uma cidade
        retornados pela API do site 4devs.
    """

    soup = BeautifulSoup(html, 'html.parser')

    return [
        option.text for option in soup.find_all('option')[1:]
    ]

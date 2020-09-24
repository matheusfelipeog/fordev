# -*- coding: utf-8 -*-
"""Module for generating random data.

Options:
    CNH - Carteira Nacional de Habilitação;
"""

# --- Local libraries ---
from ._base import fordev_request


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

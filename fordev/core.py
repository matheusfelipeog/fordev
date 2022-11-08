"""
fordev.core
-----------

Este módulo é o core para criar e manipular requests para a API do site 4devs.
"""

__all__ = ['fordev_request']

import requests

from fordev.consts import URL_4DEV_API


def _create_headers(content_length: int, referer: str) -> dict:
    """Gere o header para ser enviado em requests HTTP para o site 4devs.

    Parameters
    ----------
    content_length
        Indica o tamanho do entity-body, em bytes, enviados no header para o destinatário.

    referer
        Referência a ação a ser executada pela API do site 4devs.
        Pode-se interpretar como o endpoint do serviço a ser disponibilizado.

    """

    headers = {
        'user-agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
            'Chrome/106.0.0.0 Safari/537.36'
        ),
        'authority': 'www.4devs.com.br',
        'method': 'POST',
        'path': '/ferramentas_online.php',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'pt,en-US;q=0.9,en;q=0.8',
        'content-length': str(content_length),
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://www.4devs.com.br',
        'referer': f'https://www.4devs.com.br/{referer}',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'x-requested-with': 'XMLHttpRequest'
    }

    return headers


def fordev_request(content_length: int, referer: str, payload: dict) -> dict:
    """Cria uma request HTTP a API do site 4devs e
    retorna seu conteúdo em formato de dicionário.

    Parameters
    ----------
    content_length
        Indica o tamanho do entity-body, em bytes, enviados no header para o destinatário.

    referer
        Referência a ação a ser executada pela API do site 4devs.
        Pode-se interpretar como o endpoint do serviço a ser disponibilizado.

    payload
        Um dicionário de dados contendo a ação e outros dados solicitados pela API.
    """

    try:
        response = requests.post(
            url=URL_4DEV_API,
            headers=_create_headers(content_length, referer),
            data=payload,
            timeout=10
        )

        response.raise_for_status()

        return {
            'msg': 'success',
            'data': response.text
        }

    except (requests.RequestException, requests.HTTPError) as err:
        return {
            'msg': 'failed',
            'error': err
        }

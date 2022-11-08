"""
fordev.validators.voter_title
-----------------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format


def is_valid_voter_title(voter_title_code: str, data_only: bool=True) -> bool:
    """Verifique se o código do título de eleitor é válido.

    Parameters
    ----------
    voter_title_code
        O código do título de eleitor para verificação.
    """

    content_length = 59
    referer = 'validador_titulo_de_eleitor'
    payload = {
        'acao': 'validar_titulo_eleitor',
        'txt_titulo_eleitor': voter_title_code
    }

    resp = fordev_request(content_length, referer, payload)

    if resp.get('data', False):
        is_valid = resp['data'].split(' - ')[-2].lower() == 'verdadeiro'
        resp['data'] = is_valid

    return data_format(data_only=data_only, data_dict=resp)

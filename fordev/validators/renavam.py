"""
fordev.validators.renavam
-------------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format

from fordev.validators.utils import _data_verification_and_normalize


def is_valid_renavam(renavam_code: str, data_only: bool=True) -> bool:
    """Verifique se o código do RENAVAM é válido.

    Parameters
    ----------
    renavam_code
        O código do RENAVAM para verificação.
   """

    content_length = 43
    referer = 'validador_de_renavam'
    payload = {
        'acao': 'validar_renavam',
        'txt_renavam': renavam_code
    }

    resp = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=resp)

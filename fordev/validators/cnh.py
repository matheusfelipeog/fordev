"""
fordev.validators.cnh
---------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format

from fordev.validators.utils import _data_verification_and_normalize


def is_valid_cnh(cnh_code: str, data_only: bool=True) -> bool:
    """Verifique se o código da CNH é válido.

    Parameters
    ----------
    cnh_code
        O código da CNH para verificação.
    """

    content_length = 36
    referer = 'validador_cnh'
    payload = {
        'acao': 'validar_cnh',
        'txt_cnh': cnh_code
    }

    resp = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=resp)

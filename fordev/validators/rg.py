"""
fordev.validators.rg
--------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format

from fordev.validators.utils import _data_verification_and_normalize


def is_valid_rg(rg_code: str, data_only: bool=True) -> bool:
    """Verifique se o código do RG é válido.

    Parameters
    ----------
    rg_code
        O código do RG para verificação.
    """

    content_length = 35
    referer = 'validador_rg'
    payload = {
        'acao': 'validar_rg',
        'txt_rg': rg_code
    }

    resp = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=resp)

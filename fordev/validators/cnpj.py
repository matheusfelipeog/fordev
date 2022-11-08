"""
fordev.validators.cnpj
----------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format

from fordev.validators.utils import _data_verification_and_normalize


def is_valid_cnpj(cnpj_code: str, data_only: bool=True) -> bool:
    """Verifique se o código do CNPJ é válido.

    Parameters
    ----------
    cnpj_code
        O código CNPJ para verificação.
    """

    content_length = 47
    referer = 'validador_cnpj'
    payload = {
        'acao': 'validar_cnpj',
        'txt_cnpj': cnpj_code
    }

    resp = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=resp)

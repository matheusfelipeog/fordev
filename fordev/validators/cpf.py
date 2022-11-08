"""
fordev.validators.cpf
---------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format

from fordev.validators.utils import _data_verification_and_normalize


def is_valid_cpf(cpf_code: str, data_only: bool=True) -> bool:
    """Verifique se o código do CPF é válido.

    Parameters
    ----------
    cpf_code
        O código do CPF para verificação.
    """

    content_length = 39
    referer = 'validador_cpf'
    payload = {
        'acao': 'validar_cpf',
        'txt_cpf': cpf_code
    }

    resp = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=resp)

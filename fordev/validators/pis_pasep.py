"""
fordev.validators.pis_pasep
---------------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format

from fordev.validators.utils import _data_verification_and_normalize


def is_valid_pis_pasep(pis_pasep_code: str, data_only: bool=True) -> bool:
    """Verifique se o código do PIS/PASEP é válido.

    Parameters
    ----------
    pis_pasep_code
        O código PIS/PASEP para verificação.
    """

    content_length = 39
    referer = 'validador_pis_pasep'
    payload = {
        'acao': 'validar_pis',
        'txt_pis': pis_pasep_code
    }

    resp = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=resp)

"""
fordev.validators.certificate
-----------------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format

from fordev.validators.utils import _data_verification_and_normalize


def is_valid_certificate(certificate_code: str, data_only: bool=True) -> bool:
    """Verifique se o código da Certidão (birth, wedding, religious wedding and death) é válido.

    Parameters
    ----------
    certificate_code
        O código da certidão para verificação.
    """

    content_length = 75
    referer = 'validador_certidoes'
    payload = {
        'acao': 'validar_certidao',
        'txt_certidao': certificate_code
    }

    resp = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=resp)

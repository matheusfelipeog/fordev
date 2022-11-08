"""
fordev.validators.credit_card
-----------------------------
"""

from fordev.core import fordev_request

from fordev.consts import ALL_BANK_FLAGS_2

from fordev.filters import data_format

from fordev.validators.utils import _data_verification_and_normalize


def is_valid_credit_card(flag: int, credit_card_code: str, data_only: bool=True) -> bool:
    """Verifique se o código do cartão de crédito é válido.

    Parameters
    ----------
    flag
        A bandeira do cartão de crédito que deseja validar o código.

        Consulte a doc para verificar as opções suportadas:
        https://fordev.rtfd.io/pt_BR/latest/fordev/generators.html

    credit_card_code
        O código do cartão de crédito para verificação.
   """

    if not (1 <= flag <= 12):
        msg_error = (
            f'The flag credit card code value "{flag}" is invalid.'
            ' Enter a valid flag credit card code.'
            ' The range is 1 to 12.'
        )

        raise ValueError(msg_error)

    flag = ALL_BANK_FLAGS_2[flag]

    content_length = 68
    referer = 'validador_numero_cartao_credito'
    payload = {
        'acao': 'validar_cc',
        'txt_cc': credit_card_code,
        'bandeira': flag
    }

    resp = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=resp)

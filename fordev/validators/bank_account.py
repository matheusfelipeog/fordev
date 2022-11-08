"""
fordev.validators.bank_account
------------------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format

from fordev.validators.utils import _data_verification_and_normalize


def is_valid_bank_account(bank: int, agency: str, account: str, data_only: bool=True) -> bool:
    """Verifique se os dados da conta bancária são válidos.

    Parameters
    ----------
    bank
        A bandeira do banco da conta bancária que deseja validar os dados.

        Consulte a doc para verificar as opções suportadas:
        https://fordev.rtfd.io/pt_BR/latest/fordev/generators.html

    agency
        O código da agência bancária para verificação.

    account
        O código da conta bancária para verificação.
   """

    if not (1 <= bank <= 5):
        msg_error = (
            f'The bank code value "{bank}" is invalid. Enter a valid bank code.'
            ' The range is 1 to 5.'
        )

        raise ValueError(msg_error)

    bank = [2, 121, 85, 120, 151][bank - 1]

    content_length = 66
    referer = 'validador_conta_bancaria'
    payload = {
        'acao': 'validar_conta_bancaria',
        'banco': bank,
        'agencia': agency,
        'conta': account
    }

    resp = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=resp)

"""
fordev.generators.bank_account
------------------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format
from fordev.filters import filter_bank_account_info

from fordev.validators.utils import raise_for_invalid_uf


def bank_account(bank: int=0, uf_code: str='', data_only: bool=True) -> dict:
    """Gere dados de conta bancária.

    Parameters
    ----------
    bank
        Recebe um valor númerico de 0 a 5 que representa a
        bandeira do banco da conta bancária a ser gerada.

        Consulte a doc para verificar as opções suportadas:
        https://fordev.rtfd.io/pt_BR/latest/fordev/generators.html
    """

    if not (0 <= bank <= 5):
        msg_error = (
            f'The bank code value "{bank}" is invalid. Enter a valid bank code.'
            ' The range is 0 to 5.'
        )

        raise ValueError(msg_error)

    bank = ['', 2, 121, 85, 120, 151][bank]

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code, include_blank=True)

    resp = fordev_request(
        content_length=45,
        referer='gerador_conta_bancaria',
        payload={
            'acao': 'gerar_conta_bancaria',
            'estado': uf_code,
            'banco': bank
        }
    )

    resp['data'] = filter_bank_account_info(resp['data'])

    return data_format(data_only=data_only, data_dict=resp)

"""
fordev.generators.credit_card
-----------------------------
"""

from random import choice as random_choice

from fordev.core import fordev_request

from fordev.consts import ALL_BANK_FLAGS

from fordev.filters import filter_credit_card_info
from fordev.filters import data_format


def credit_card(bank: int=0, formatting: bool=True, data_only: bool=True) -> dict:
    """Gere dados de cartão de crédito aleatório.

    Parameters
    ----------
    bank
        Recebe um valor númerico de 0 a 10 representando a
        bandeira do cartão de crédito a ser gerado.

        Consulte a doc para verificar as opções suportadas:
        https://fordev.rtfd.io/pt_BR/latest/fordev/generators.html
    """

    if not (0 <= bank <= 10):
        msg_error = (
            f'The bank code value "{bank}" is invalid. Enter a valid bank code.'
            ' The range is 0 to 10.'
        )

        raise ValueError(msg_error)

    if bank != 0:
        bank = ALL_BANK_FLAGS[bank]
    else:
        bank = random_choice(
            list(ALL_BANK_FLAGS.values())
        )

    resp = fordev_request(
        content_length=43,
        referer='gerador_de_numero_cartao_credito',
        payload={
            'acao': 'gerar_cc',
            'pontuacao': 'S' if formatting else 'N',
            'bandeira': bank
        }
    )

    resp['data'] = filter_credit_card_info(resp['data'])

    return data_format(data_only=data_only, data_dict=resp)

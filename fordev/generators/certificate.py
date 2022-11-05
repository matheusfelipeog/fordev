"""
fordev.generators.certificate
-----------------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format


def certificate(type_: str='I', formatting: bool=True, data_only: bool=True) -> str:
    """Gere o código de certidões (birth, wedding, religious wedding and death) aleatórias.

    Parameters
    ----------
    type_
        O tipo da certidão para geração do código.

        Consulte a doc para verificar as opções suportadas:
        https://fordev.rtfd.io/pt_BR/latest/fordev/generators.html
    """

    type_ = type_.upper()

    certificate_types = {
        'I': 'Indiferente',
        'B': 'nascimento',
        'W': 'casamento',
        'R': 'casamento_religioso',
        'D': 'obito'
    }

    if not certificate_types.get(type_, False):
        msg_error = (
            f'The certificate type "{type_}" is invalid. Enter a valid type.'
            ' Ex: "B" = Birth, "W" = Wedding, "R" = Religious Wedding,'
            '"D" = Death and "I" = Indifferent (Default).'
        )
        raise ValueError(msg_error)

    resp = fordev_request(
        content_length=67,
        referer='gerador_numero_certidoes',
        payload={
            'acao': 'gerador_certidao',
            'pontuacao': 'S' if formatting else 'N',
            'tipo_certidao': certificate_types.get(type_)
        }
    )

    return data_format(data_only=data_only, data_dict=resp)

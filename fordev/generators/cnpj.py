"""
fordev.generators.cpnj
----------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format


def cnpj(formatting: bool=True, data_only: bool=True) -> str:
    """Gere o código do CNPJ(Cadastro Nacional da Pessoa Jurídica) aleatório."""

    resp = fordev_request(
        content_length=27,
        referer='gerador_de_cnpj',
        payload={
            'acao': 'gerar_cnpj',
            'pontuacao': 'S' if formatting else 'N',
        }
    )

    return data_format(data_only=data_only, data_dict=resp)

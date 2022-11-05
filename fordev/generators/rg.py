"""
fordev.generators.rg
--------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format


def rg(formatting: bool=True, data_only: bool=True) -> str:
    """Gere o código do RG(Registro Geral) aleatório, emitido por SSP-SP."""

    resp = fordev_request(
        content_length=25,
        referer='gerador_de_rg',
        payload={
            'acao': 'gerar_rg',
            'pontuacao': 'S' if formatting else 'N',
        }
    )

    return data_format(data_only=data_only, data_dict=resp)

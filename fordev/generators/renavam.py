"""
fordev.generators.renavam
-------------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format


def renavam(data_only: bool=True) -> str:
    """Gere o código do RENAVAM(Registro Nacional de Veículos Automotores) aleatório."""

    resp = fordev_request(
        content_length=18,
        referer='gerador_de_renavam',
        payload={'acao': 'gerar_renavam'}
    )

    return data_format(data_only=data_only, data_dict=resp)

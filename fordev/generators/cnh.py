"""
fordev.generators.cnh
---------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format


def cnh(data_only: bool=True) -> str:
    """Geração aleatória de CNH (Carteira Nacional de Habilitação)."""

    resp = fordev_request(
        content_length=14,
        referer='gerador_de_cnh',
        payload={'acao': 'gerar_cnh'}
    )

    return data_format(data_only=data_only, data_dict=resp)

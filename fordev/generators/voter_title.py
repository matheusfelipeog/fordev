"""
fordev.generators.voter_title
-----------------------------
"""

from fordev.core import fordev_request

from fordev.validators.utils import raise_for_invalid_uf

from fordev.filters import data_format


def voter_title(uf_code: str, data_only: bool=True) -> str:
    """Gere o código do título de eleitor aleatório, conforme o UF especificado."""

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code)

    resp = fordev_request(
        content_length=35,
        referer='gerador_de_titulo_de_eleitor',
        payload={
            'acao': 'gerar_titulo_eleitor',
            'estado': uf_code
        }
    )

    return data_format(data_only=data_only, data_dict=resp)

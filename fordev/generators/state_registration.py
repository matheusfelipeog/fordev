"""
fordev.generators.state_registration
------------------------------------
"""

from fordev.core import fordev_request

from fordev.validators.utils import raise_for_invalid_uf

from fordev.filters import data_format


def state_registration(uf_code: str='SP', formatting: bool=True, data_only: bool=True) -> str:
    """Gere o código de registro de estado aleatório."""

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code)

    resp = fordev_request(
        content_length=35,
        referer='gerador_de_inscricao_estadual',
        payload={
            'acao': 'gerar_ie',
            'pontuacao': 'S' if formatting else 'N',
            'estado': uf_code
        }
    )

    return data_format(data_only=data_only, data_dict=resp)

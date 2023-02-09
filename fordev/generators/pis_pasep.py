"""
fordev.generators.pis_pasep
---------------------------
"""

from typing import Union

from fordev.core import fordev_request

from fordev.filters import data_format


def pis_pasep(
    formatting: bool = True,
    data_only: bool = True
) -> Union[str, dict]:
    """Gere o código do PIS/PASEP aleatório."""

    resp = fordev_request(
        content_length=26,
        referer='gerador_de_pis_pasep',
        payload={
            'acao': 'gerar_pis',
            'pontuacao': 'S' if formatting else 'N'
        }
    )

    return data_format(data_only=data_only, data_dict=resp)

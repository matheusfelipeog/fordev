"""
fordev.generators.cpf
---------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format

from fordev.validators.utils import raise_for_invalid_uf


def cpf(uf_code: str='', formatting: bool=True, data_only: bool=True) -> str:
    """Gere o código de um CPF(Cadastro de Pessoas Físicas) aleatório."""

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code, include_blank=True)

    resp = fordev_request(
        content_length=38 if uf_code == '' else 40,
        referer='gerador_de_cpf',
        payload={
            'acao': 'gerar_cpf',
            'pontuacao': 'S' if formatting else 'N',
            'cpf_estado': uf_code
        }
    )

    return data_format(data_only=data_only, data_dict=resp)

"""
fordev.generators.city
----------------------
"""

from fordev.core import fordev_request

from fordev.validators.utils import raise_for_invalid_uf

from fordev.filters import filter_city_name
from fordev.filters import data_format


def city(uf_code: str='SP', data_only: bool=True) -> list:
    """Obtenha as cidades do UF especificado."""

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code)

    resp = fordev_request(
        content_length=35,
        referer='gerador_de_pessoas',
        payload={
            'acao': 'carregar_cidades',
            'cep_estado': uf_code
        }
    )

    resp['data'] = filter_city_name(resp['data'])

    return data_format(data_only=data_only, data_dict=resp)

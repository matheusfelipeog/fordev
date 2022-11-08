"""
fordev.generators.company
-------------------------
"""

from fordev.core import fordev_request

from fordev.validators.utils import raise_for_invalid_uf

from fordev.filters import filter_company_info
from fordev.filters import data_format


def company(uf_code: str='SP', age: int=1, formatting: bool=True, data_only: bool=True) -> dict:
    """Gere dados de companhia (empresa/organização) aleatório.

    Parameters
    ----------
    age
        Representa o tempo de existência da companhia (a idade da companhia).
    """

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code)

    if not (1 <= age <= 30):
        msg_error = (
            f'The company age value "{age}" is invalid. Enter a valid company age.'
            ' The range is 1 to 30.'
        )

        raise ValueError(msg_error)

    resp = fordev_request(
        content_length=48,
        referer='gerador_de_empresas',
        payload={
            'acao': 'gerar_empresa',
            'pontuacao': 'S' if formatting else 'N',
            'estado': uf_code,
            'idade': age
        }
    )

    resp['data'] = filter_company_info(resp['data'])

    return data_format(data_only=data_only, data_dict=resp)

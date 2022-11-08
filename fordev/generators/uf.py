"""
fordev.generators.uf
--------------------
"""

from random import sample as random_sample

from fordev.consts import ALL_UF_CODE


def uf(n: int=1, data_only: bool=True) -> list:
    """Gere o código da UF(Unidade Federativa) aleatório.

    Parameters
    ----------
    n
        O número de UF's para geração do dado. O mínimo é 1 e o máximo é 27.
    """

    if not (1 <= n <= 27):
        msg_error = (
            f'The n value "{n}" is invalid. Enter a valid number of UF.'
            ' The range is 1 to 27 UF code.'
        )

        raise ValueError(msg_error)

    full_data = {
        'msg': 'success',
        'data': random_sample(ALL_UF_CODE, n)
        }

    if data_only:
        return full_data['data']
    else:
        return full_data

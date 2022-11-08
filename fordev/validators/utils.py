"""
fordev.validators.utils
-----------------------
"""

__all__ = [
    '_data_verification_and_normalize',
    'raise_for_invalid_uf'
]

from fordev.consts import ALL_UF_CODE


def _data_verification_and_normalize(data: dict) -> dict:
    """"Verifique se a key existe e se o valor é válido.
    Se válido, substítui para um novo formato.

    Parameters
    ----------
    data
        Um dicionário de dados para verificação e mudança de formato.
    """

    data = data.copy()

    if data.get('data', False):
        is_valid = data['data'].split(' - ')[-1].lower() == 'verdadeiro'
        data['data'] = is_valid

    return data


def raise_for_invalid_uf(uf: str, include_blank=False):
    """Levanta uma exceção if o código UF for inválido.

    Parameters
    ----------
    include_blank
        Algumas funções enviam um UF em branco, para considerá-lo
        defina ``include_blank`` como ``True``.
    """

    ufs = ALL_UF_CODE.copy()

    if include_blank:
        ufs.append('')

    if uf not in ufs:
        msg_error = (
            f'The UF code "{uf}" is invalid. Enter a valid UF code. Ex: SP, RJ, PB...'
            ' More info about UF in: https://pt.wikipedia.org/wiki/Subdivis%C3%B5es_do_Brasil'
        )

        raise ValueError(msg_error)

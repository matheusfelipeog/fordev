"""
fordev.validators
-----------------

Este módulo válida os dados utilizando o site `4Devs <https://www.4devs.com.br/>`_
e disponibiliza uma API simples para uso.

Use a função ``help()`` para mais informações:

>>> from fordev import validators
>>> help(validators)
Help on module fordev.validators in fordev:

NAME
    fordev.validators

DESCRIPTION
(...)

Ou consulte a documentação oficial.

Note
----
Muitas funções do módulo ``fordev.validators`` contém parâmetros em comum,
todos estão descritos abaixo.

More details in next section.

Parameter
---------
data_only: bool
    Se receber o valor ``True``, retorna somente os dados em texto puro.
    Se receber o valor ``False``, retorna um dicionário contendo uma chave ``msg`` e ``data`` ou ``error``
    contendo valores correspondentes à nomenclatura de suas chaves.

Sendo assim, sempre que o encontrar, utilize conforme o descrito acima.
"""

__all__ = [
    'is_valid_credit_card',
    'is_valid_bank_account',
    'is_valid_certificate',
    'is_valid_cnh',
    'is_valid_cnpj',
    'is_valid_cpf',
    'is_valid_pis_pasep',
    'is_valid_renavam',
    'is_valid_rg',
    'is_valid_voter_title',
    'is_valid_state_registration',
]

from fordev.core import fordev_request

from fordev.consts import ALL_UF_CODE
from fordev.consts import ALL_BANK_FLAGS_2

from fordev.filters import data_format


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


def raise_for_invalid_uf(uf, include_blank=False):
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


def is_valid_credit_card(flag: int, credit_card_code: str, data_only: bool=True) -> bool:
    """Verifique se o código do cartão de crédito é válido.

    Parameters
    ----------
    flag
        A bandeira do cartão de crédito que deseja validar o código.

        Consulte a doc para verificar as opções suportadas:
        https://fordev.rtfd.io/pt_BR/latest/fordev/generators.html

    credit_card_code
        O código do cartão de crédito para verificação.
   """

    if not (1 <= flag <= 12):
        msg_error = (
            f'The flag credit card code value "{flag}" is invalid.'
            ' Enter a valid flag credit card code.'
            ' The range is 1 to 12.'
        )

        raise ValueError(msg_error)

    flag = ALL_BANK_FLAGS_2[flag]

    content_length = 68
    referer = 'validador_numero_cartao_credito'
    payload = {
        'acao': 'validar_cc',
        'txt_cc': credit_card_code,
        'bandeira': flag
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=r)


def is_valid_bank_account(bank: int, agency: str, account: str, data_only: bool=True) -> bool:
    """Verifique se os dados da conta bancária são válidos.

    Parameters
    ----------
    bank
        A bandeira do banco da conta bancária que deseja validar os dados.

        Consulte a doc para verificar as opções suportadas:
        https://fordev.rtfd.io/pt_BR/latest/fordev/generators.html

    agency
        O código da agência bancária para verificação.

    account
        O código da conta bancária para verificação.
   """

    if not (1 <= bank <= 5):
        msg_error = (
            f'The bank code value "{bank}" is invalid. Enter a valid bank code.'
            ' The range is 1 to 5.'
        )

        raise ValueError(msg_error)

    bank = [2, 121, 85, 120, 151][bank - 1]

    content_length = 66
    referer = 'validador_conta_bancaria'
    payload = {
        'acao': 'validar_conta_bancaria',
        'banco': bank,
        'agencia': agency,
        'conta': account
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=r)


def is_valid_certificate(certificate_code: str, data_only: bool=True) -> bool:
    """Verifique se o código da Certidão (birth, wedding, religious wedding and death) é válido.

    Parameters
    ----------
    certificate_code
        O código da certidão para verificação.
    """

    content_length = 75
    referer = 'validador_certidoes'
    payload = {
        'acao': 'validar_certidao',
        'txt_certidao': certificate_code
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=r)


def is_valid_cnh(cnh_code: str, data_only: bool=True) -> bool:
    """Verifique se o código da CNH é válido.

    Parameters
    ----------
    cnh_code
        O código da CNH para verificação.
    """

    content_length = 36
    referer = 'validador_cnh'
    payload = {
        'acao': 'validar_cnh',
        'txt_cnh': cnh_code
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=r)


def is_valid_cnpj(cnpj_code: str, data_only: bool=True) -> bool:
    """Verifique se o código do CNPJ é válido.

    Parameters
    ----------
    cnpj_code
        O código CNPJ para verificação.
    """

    content_length = 47
    referer = 'validador_cnpj'
    payload = {
        'acao': 'validar_cnpj',
        'txt_cnpj': cnpj_code
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=r)


def is_valid_cpf(cpf_code: str, data_only: bool=True) -> bool:
    """Verifique se o código do CPF é válido.

    Parameters
    ----------
    cpf_code
        O código do CPF para verificação.
    """

    content_length = 39
    referer = 'validador_cpf'
    payload = {
        'acao': 'validar_cpf',
        'txt_cpf': cpf_code
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=r)


def is_valid_pis_pasep(pis_pasep_code: str, data_only: bool=True) -> bool:
    """Verifique se o código do PIS/PASEP é válido.

    Parameters
    ----------
    pis_pasep_code
        O código PIS/PASEP para verificação.
    """

    content_length = 39
    referer = 'validador_pis_pasep'
    payload = {
        'acao': 'validar_pis',
        'txt_pis': pis_pasep_code
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=r)


def is_valid_renavam(renavam_code: str, data_only: bool=True) -> bool:
    """Verifique se o código do RENAVAM é válido.

    Parameters
    ----------
    renavam_code
        O código do RENAVAM para verificação.
   """

    content_length = 43
    referer = 'validador_de_renavam'
    payload = {
        'acao': 'validar_renavam',
        'txt_renavam': renavam_code
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=r)


def is_valid_rg(rg_code: str, data_only: bool=True) -> bool:
    """Verifique se o código do RG é válido.

    Parameters
    ----------
    rg_code
        O código do RG para verificação.
    """

    content_length = 35
    referer = 'validador_rg'
    payload = {
        'acao': 'validar_rg',
        'txt_rg': rg_code
    }

    r = _data_verification_and_normalize(
        fordev_request(content_length, referer, payload)
    )

    return data_format(data_only=data_only, data_dict=r)


def is_valid_voter_title(voter_title_code: str, data_only: bool=True) -> bool:
    """Verifique se o código do título de eleitor é válido.

    Parameters
    ----------
    voter_title_code
        O código do título de eleitor para verificação.
    """

    content_length = 59
    referer = 'validador_titulo_de_eleitor'
    payload = {
        'acao': 'validar_titulo_eleitor',
        'txt_titulo_eleitor': voter_title_code
    }

    r = fordev_request(content_length, referer, payload)

    if r.get('data', False):
        is_valid = r['data'].split(' - ')[-2].lower() == 'verdadeiro'
        r['data'] = is_valid

    return data_format(data_only=data_only, data_dict=r)


def is_valid_state_registration(uf_code: str, state_registration_code: str, data_only: bool=True) -> bool:
    """Verifique se o código do registro estadual é válido.

    Parameters
    ----------
    uf_code
        O código UF(Unidade Federativa) do estado que pertence o registro estadual.

        Mais informações: https://pt.wikipedia.org/wiki/Subdivis%C3%B5es_do_Brasil

    state_registration_code
        O código do registro estadual para verificação.
    """

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code)

    r = _data_verification_and_normalize(
        fordev_request(
            content_length=48,
            referer='validar_inscricao_estadual',
            payload={
                'acao': 'validar_ie',
                'txt_ie': state_registration_code,
                'estado': uf_code
            }
        )
    )

    return data_format(data_only=data_only, data_dict=r)

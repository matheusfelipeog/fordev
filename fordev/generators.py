"""
fordev.generators
-----------------

Este módulo coleta dados aleatórios gerados pelo site `4Devs <https://www.4devs.com.br/>`_ 
e disponíbiliza uma API simples para uso.

Use a função ``help()`` para mais informações:

>>> from fordev import generators
>>> help(generators)
Help on module fordev.generators in fordev:

NAME
    fordev.generators

DESCRIPTION
(...)

Ou consulte a documentação oficial.

Note
----
Muitas funções do módulo ``fordev.generators`` contém parâmetros em comum,
todos estão descrito abaixo.

Parameters
----------
uf_code: str
    Recebe o Código da **Unidade Federativa** para geração do dado.

    Caso não saiba o que é ou não conheça o do estado que necessita, 
    obtenha mais informações em: https://pt.wikipedia.org/wiki/Subdivis%C3%B5es_do_Brasil

formatting: bool
    Se receber o valor ``True``, retorna os dados formatados.
    Se receber o valor ``False``, retorna os dados sem formatação.

data_only: bool
    Se receber o valor ``True``, retorna somente os dados em texto puro.
    Se receber o valor ``False``, retorna um dicionário contendo uma chave ``msg`` e ``data`` ou ``error``
    contendo valores correspondentes à nomenclatura de suas chaves.

Sendo assim, sempre que os encontrar, utilize conforme o descrito acima.
"""

__all__ = [
    'certificate',
    'cnh',
    'bank_account',
    'cpf',
    'pis_pasep',
    'renavam',
    'vehicle',
    'vehicle_brand',
    'vehicle_plate',
    'cnpj',
    'rg',
    'state_registration',
    'voter_title',
    'credit_card',
    'people',
    'company',
    'uf',
    'city'
]

from json import loads as json_loads

from random import sample as random_sample
from random import choice as random_choice

from fordev.core import fordev_request

from fordev.consts import ALL_UF_CODE
from fordev.consts import ALL_VEHICLE_BRANDS
from fordev.consts import ALL_BANK_FLAGS

from fordev.validators import raise_for_invalid_uf

from fordev.filters import data_format
from fordev.filters import filter_city_name
from fordev.filters import filter_vehicle_info
from fordev.filters import filter_credit_card_info
from fordev.filters import filter_bank_account_info
from fordev.filters import filter_company_info


def certificate(type_: str='I', formatting: bool=True, data_only: bool=True) -> str:
    """Gere o código de certidões (birth, wedding, religious wedding and death) aleatórias.

    Parameters
    ----------
    type_
        O tipo da certidão para geração do código.

        Consulte a doc para verificar as opções suportadas:
        https://fordev.rtfd.io/pt_BR/latest/fordev/generators.html
    """

    type_ = type_.upper()

    certificate_types = {'I': 'Indiferente', 'B': 'nascimento', 'W': 'casamento', 'R': 'casamento_religioso', 'D': 'obito'}

    # If type_ not exists in certificate_types, raise exception.
    if not certificate_types.get(type_, False):
        msg_error = f'The certificate type "{type_}" is invalid. Enter a valid type.'
        msg_error += f' Ex: "B" = Birth, "W" = Wedding, "R" = Religious Wedding, "D" = Death and "I" = Indifferent (Default).'

        raise ValueError(msg_error)

    r = fordev_request(
        content_length=67,  # Max of bytes for generate certificate in all possibilities.
        referer='gerador_numero_certidoes', 
        payload={
            'acao': 'gerador_certidao',
            'pontuacao': 'S' if formatting else 'N',
            'tipo_certidao': certificate_types.get(type_)
        }
    )

    return data_format(data_only=data_only, data_dict=r)


def cnh(data_only: bool=True) -> str:
    """Random generate of CNH(Carteira Nacional de Habilitação)."""

    r = fordev_request(
        content_length=14,
        referer='gerador_de_cnh',
        payload={'acao': 'gerar_cnh'}
    )

    return data_format(data_only=data_only, data_dict=r)


def bank_account(bank: int=0, uf_code: str='', data_only: bool=True) -> dict:
    """Gere dados de conta bancária.

    Parameters
    ----------
    bank
        Recebe um valor númerico de 0 a 5 que representa a
        bandeira do banco da conta bancária a ser gerada.

        Consulte a doc para verificar as opções suportadas:
        https://fordev.rtfd.io/pt_BR/latest/fordev/generators.html
    """

    if not (0 <= bank <= 5):
        msg_error = f'The bank code value "{bank}" is invalid. Enter a valid bank code.'
        msg_error += f' The range is 0 to 5.'

        raise ValueError(msg_error)

    # Replace the bank number with the bank code used in 4devs.
    bank = ['', 2, 121, 85, 120, 151][bank]  # Use the index for get the bank code.

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code, include_blank=True)

    r = fordev_request(
        content_length=45,
        referer='gerador_conta_bancaria',
        payload={
            'acao': 'gerar_conta_bancaria',
            'estado': uf_code,
            'banco': bank
        }
    )

    # Replace data in html format with bank account info only.
    r['data'] = filter_bank_account_info(r['data'])

    return data_format(data_only=data_only, data_dict=r)


def cpf(uf_code: str='', formatting: bool=True, data_only: bool=True) -> str:
    """Gere o código de um CPF(Cadastro de Pessoas Físicas) aleatório."""

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code, include_blank=True)

    r = fordev_request(
        content_length=38 if uf_code == '' else 40,
        referer='gerador_de_cpf',
        payload={
            'acao': 'gerar_cpf',
            'pontuacao': 'S' if formatting else 'N',
            'cpf_estado': uf_code
        }
    )

    return data_format(data_only=data_only, data_dict=r)


def pis_pasep(formatting: bool=True, data_only: bool=True) -> str:
    """Gere o código do PIS/PASEP aleatório."""

    r = fordev_request(
        content_length=26,
        referer='gerador_de_pis_pasep',
        payload={
            'acao': 'gerar_pis',
            'pontuacao': 'S' if formatting else 'N'
        }
    )

    return data_format(data_only=data_only, data_dict=r)    


def renavam(data_only: bool=True) -> str:
    """Gere o código do RENAVAM(Registro Nacional de Veículos Automotores) aleatório."""

    r = fordev_request(
        content_length=18,
        referer='gerador_de_renavam',
        payload={'acao': 'gerar_renavam'}
    )

    return data_format(data_only=data_only, data_dict=r) 


def vehicle(brand_code: int=0, uf_code: str='', formatting: bool=True, data_only: bool=True) -> dict:
    """Gere dados de veículo aleatório.

    Parameters
    ----------
    brand
        Recebe um valor númerico de 0 a 87 que representa a marca do carro para
        geração dos dados aleatórios.

        Consulte a doc para verificar as opções suportadas:
        https://fordev.rtfd.io/pt_BR/latest/fordev/generators.html
    """

    if not (0 <= brand_code <= 87):
        msg_error = f'The vehicle brand code value "{brand_code}" is invalid. Enter a valid vehicle brand code.'
        msg_error += f' The range is 0 to 87.'

        raise ValueError(msg_error)

    # Replace the brand code with the brand code used in 4devs.
    if brand_code != 0:
        brand_code = ALL_VEHICLE_BRANDS[brand_code]['code']
    else:
        brand_code = ''

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code, include_blank=True)

    r = fordev_request(
        content_length=62,  # Max of bytes for generate vehicle data in all possibilities.
        referer='gerador_de_veiculos',
        payload={
            'acao': 'gerar_veiculo',
            'pontuacao': 'S' if formatting else 'N',
            'estado': uf_code,
            'fipe_codigo_marca': brand_code
        }
    )

    # Replace data in html format with bank account info only.
    r['data'] = filter_vehicle_info(r['data'])

    return data_format(data_only=data_only, data_dict=r)


def vehicle_brand(n: int=1, data_only: bool=True) -> list:
    """Obtenha o nome de marca(s) de veículo(s).

    Parameters
    ----------
    n
        Recebe o número de marcas de veículos a ser gerado. O valor mínimo é 1 e o máximo é 87.
    """

    if not (1 <= n <= 87):
        msg_error = f'The n value "{n}" is invalid. Enter a valid number of UF.'
        msg_error += f' The range is 1 to 27 UF code.'

        raise ValueError(msg_error)

    full_data = {
        'msg': 'success', 
        'data': random_sample(
            [v_brand['brand_name'] for v_brand in ALL_VEHICLE_BRANDS.values()],  # Create a list brand name
            n 
        )
    }

    if data_only:
        return full_data['data']
    else:
        return full_data


def vehicle_plate(uf_code: str='', formatting: bool=True, data_only: bool=True) -> str:
    """Gere o código da placa de veículo aleatório."""

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code, include_blank=True)

    r = fordev_request(
        content_length=36 if uf_code == '' else 38,
        referer='gerador_de_placa_automoveis',
        payload={
            'acao': 'gerar_placa',
            'pontuacao': 'S' if formatting else 'N',
            'estado':uf_code
        }
    )

    return data_format(data_only=data_only, data_dict=r)


def cnpj(formatting: bool=True, data_only: bool=True) -> str:
    """Gere o código do CNPJ(Cadastro Nacional da Pessoa Jurídica) aleatório."""

    r = fordev_request(
        content_length=27,
        referer='gerador_de_cnpj',
        payload={
            'acao': 'gerar_cnpj',
            'pontuacao': 'S' if formatting else 'N',
        }
    )

    return data_format(data_only=data_only, data_dict=r)


def rg(formatting: bool=True, data_only: bool=True) -> str:
    """Gere o código do RG(Registro Geral) aleatório, emitido por SSP-SP."""

    r = fordev_request(
        content_length=25,
        referer='gerador_de_rg',
        payload={
            'acao': 'gerar_rg',
            'pontuacao': 'S' if formatting else 'N',
        }
    )

    return data_format(data_only=data_only, data_dict=r)


def state_registration(uf_code: str='SP', formatting: bool=True, data_only: bool=True) -> str:
    """Gere o código de registro de estado aleatório."""

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code)

    r = fordev_request(
        content_length=35,
        referer='gerador_de_inscricao_estadual',
        payload={
            'acao': 'gerar_ie',
            'pontuacao': 'S' if formatting else 'N',
            'estado': uf_code
        }
    )
    
    return data_format(data_only=data_only, data_dict=r)


def voter_title(uf_code: str, data_only: bool=True) -> str:
    """Gere o código do título de eleitor aleatório, conforme o UF especificado."""

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code)

    r = fordev_request(
        content_length=35,
        referer='gerador_de_titulo_de_eleitor',
        payload={
            'acao': 'gerar_titulo_eleitor',
            'estado': uf_code
        }
    )

    return data_format(data_only=data_only, data_dict=r)


def credit_card(bank: int=0, formatting: bool=True, data_only: bool=True) -> dict:
    """Gere dados de cartão de crédito aleatório.

    Parameters
    ----------
    bank
        Recebe um valor númerico de 0 a 10 representando a
        bandeira do cartão de crédito a ser gerado.

        Consulte a doc para verificar as opções suportadas:
        https://fordev.rtfd.io/pt_BR/latest/fordev/generators.html
    """

    if not (0 <= bank <= 10):
        msg_error = f'The bank code value "{bank}" is invalid. Enter a valid bank code.'
        msg_error += f' The range is 0 to 10.'

        raise ValueError(msg_error)

    # Replace the bank code with the bank flag used in 4devs.
    if bank != 0:
        bank = ALL_BANK_FLAGS[bank]
    else:
        bank = random_choice(
            list(ALL_BANK_FLAGS.values())
        )

    r = fordev_request(
        content_length=43,
        referer='gerador_de_numero_cartao_credito',
        payload={
            'acao': 'gerar_cc',
            'pontuacao': 'S' if formatting else 'N',
            'bandeira': bank
        }
    )

    # Replace data in html format with credit card info only.
    r['data'] = filter_credit_card_info(r['data'])

    return data_format(data_only=data_only, data_dict=r)


def people(
        n: int=1,
        sex: str='R',
        age: int=0,
        uf_code: str='',
        formatting: bool=True,
        data_only: bool=True
    ) -> str:
    """Gere dados de pessoa(s) aleatório(s)

    Parameters
    ----------
    n
        O número de pessoas a ter dados gerados. O mínimo é 1 e o máximo é 30.

    sex
        Uma string representando o sexo da pessoa para geração dos dados.

        Consulte a doc para verificar as opções suportadas:
        https://fordev.rtfd.io/pt_BR/latest/fordev/generators.html

    age
        A idade da pessoa para geração dos dados. A idade mínima é 18 e a máxima é 80.
    """

    sex = sex.upper()

    uf_code = uf_code.upper()

    if not (1 <= n <= 30):
        msg_error = f'The n value "{n}" is invalid. Enter a valid number of people.'
        msg_error += f' The range is 1 to 30 peoples.'

        raise ValueError(msg_error)

    if sex not in ['M', 'F', 'R']:
        msg_error = f'The sex "{sex}" is invalid. Enter a valid sex.'
        msg_error += f' Ex: "M" = Male, "F" = Feminine or "R" = Random.'

        raise ValueError(msg_error)

    if not (18 <= age <= 80) and age != 0:
        msg_error = f'The age "{age}" is invalid. Enter a valid age.'
        msg_error += f' The range is 18 to 80 age'

        raise ValueError(msg_error)

    raise_for_invalid_uf(uf=uf_code, include_blank=True)

    r = fordev_request(
        content_length=99,  # Max of bytes for generate people in all possibilities.
        referer='gerador_de_pessoas',
        payload={
            'acao': 'gerar_pessoa',
            'sexo': 'H' if sex == 'M' else 'M' if sex == 'F' else 'I',  # H, M and I flags are used in 4devs for filter.
            'pontuacao': 'S' if formatting else 'N',
            'idade': age,
            'cep_estado': uf_code,
            'txt_qtde': n,

            # If the state is not selected, a default flag is used for the city ('Selecione o estado!') or
            # If the state is selected and city is not selected, a default flag is used for the city ('').
            'cep_cidade': 'Selecione o estado!' if uf_code == '' else ''
        }
    )

    if data_only and r['msg'] == 'success':
        return json_loads(r['data'])

    if r['msg'] == 'success':

        # Convert data in str to dict.
        r['data'] = json_loads(r['data'])

        return r

    # In case of failure, return msg status and msg error.
    return r


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
        msg_error = f'The company age value "{age}" is invalid. Enter a valid company age.'
        msg_error += f' The range is 1 to 30.'

        raise ValueError(msg_error)

    r = fordev_request(
        content_length=48,
        referer='gerador_de_empresas',
        payload={
            'acao': 'gerar_empresa',
            'pontuacao': 'S' if formatting else 'N',
            'estado': uf_code,
            'idade': age
        }
    )

    # Replace data in html format with company info only.
    r['data'] = filter_company_info(r['data'])

    return data_format(data_only=data_only, data_dict=r)


def uf(n: int=1, data_only: bool=True) -> list:
    """Gere o código da UF(Unidade Federativa) aleatório.

    Parameters
    ----------
    n
        O número de UF's para geração do dado. O mínimo é 1 e o máximo é 27.
    """

    if not (1 <= n <= 27):
        msg_error = f'The n value "{n}" is invalid. Enter a valid number of UF.'
        msg_error += f' The range is 1 to 27 UF code.'

        raise ValueError(msg_error)

    full_data = {
        'msg': 'success', 
        'data': random_sample(ALL_UF_CODE, n)
        }

    if data_only:
        return full_data['data']
    else:
        return full_data


def city(uf_code: str='SP', data_only: bool=True) -> list:
    """Obtenha as cidades do UF especificado."""

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code)

    r = fordev_request(
        content_length=35,
        referer='gerador_de_pessoas',
        payload={
            'acao': 'carregar_cidades',
            'cep_estado': uf_code
        }
    )

    # Replace data in html format with city names only
    r['data'] = filter_city_name(r['data'])

    return data_format(data_only=data_only, data_dict=r)

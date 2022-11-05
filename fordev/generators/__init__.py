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

from fordev.generators.certificate import certificate
from fordev.generators.cnh import cnh
from fordev.generators.bank_account import bank_account
from fordev.generators.cpf import cpf
from fordev.generators.pis_pasep import pis_pasep
from fordev.generators.renavam import renavam
from fordev.generators.vehicle import vehicle, vehicle_brand, vehicle_plate
from fordev.generators.cnpj import cnpj
from fordev.generators.rg import rg
from fordev.generators.state_registration import state_registration
from fordev.generators.voter_title import voter_title
from fordev.generators.credit_card import credit_card
from fordev.generators.people import people
from fordev.generators.company import company
from fordev.generators.uf import uf
from fordev.generators.city import city

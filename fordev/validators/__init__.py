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
    'is_valid_state_registration'
]

from fordev.validators.credit_card import is_valid_credit_card
from fordev.validators.bank_account import is_valid_bank_account
from fordev.validators.certificate import is_valid_certificate
from fordev.validators.cnh import is_valid_cnh
from fordev.validators.cnpj import is_valid_cnpj
from fordev.validators.cpf import is_valid_cpf
from fordev.validators.pis_pasep import is_valid_pis_pasep
from fordev.validators.renavam import is_valid_renavam
from fordev.validators.rg import is_valid_rg
from fordev.validators.voter_title import is_valid_voter_title
from fordev.validators.state_registration import is_valid_state_registration

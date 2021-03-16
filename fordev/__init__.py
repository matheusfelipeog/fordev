# -*- coding: utf-8 -*-
"""
fordev
------

Fordev é um pacote que mapeia o site 4devs.com.br via scraping e disponibiliza
os geradoradores e validadores de dados como uma interface Python.

Example
-------
Gere dados de 1 pessoa:

>>> from fordev.generators import people
>>> people(sex='M', age=25, state='SP')
{
    'altura': '1,90',
    'bairro': 'Jardim Maria Amélia',
    'celular': '(12) 98401-5301',
    'cep': '12318-110',
    'cidade': 'Jacareí',
    'cor': 'laranja',
    'cpf': '061.632.758-70',
    'data_nasc': '06/12/1995',
    'email': 'bentoyagolorenzogoncalves-72@alcastro.com.br',
    'endereco': 'Rua José Benedito de Oliveira',
    'estado': 'SP',
    'idade': 25,
    'mae': 'Tereza Melissa Priscila',
    'nome': 'Bento Yago Lorenzo Gonçalves',
    'numero': 760,
    'pai': 'Sérgio Guilherme Erick Gonçalves',
    'peso': 88,
    'rg': '23.920.314-8',
    'senha': 'ErOKUUyoml',
    'sexo': 'Masculino',
    'signo': 'Sagitário',
    'telefone_fixo': '(12) 2844-9806',
    'tipo_sanguineo': 'AB+'
}
"""

__all__ = [
    'generators',
    'validators',
    'filters',
    'consts'
]

from fordev.__about__ import __version__
from fordev.__about__ import __author__
from fordev.__about__ import __email__
from fordev.__about__ import __author_github__
from fordev.__about__ import __project_github__

from fordev import generators
from fordev import validators
from fordev import filters
from fordev import consts

from fordev.utils import CheckVersion


# Check if a newer version of fordev package
CheckVersion.run(
    current_version=__version__,
    package_name='fordev'
)

# -*- coding: utf-8 -*-
"""
The Fordev module is a generator, validator and manipulator of random data.

Basic use:

```
>>> from fordev.generator import people
>>> p = people(sex='M', age=25, state='SP')
>>> print(p)

# Output ---------------------------------------------------------------------------------
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
```

More info at: https://github.com/matheusfelipeog/fordev
"""

from .__about__ import __version__

from .__about__ import __author__
from .__about__ import __email__
from .__about__ import __github__

__version__ = __version__
__author__ = f'{__author__} <{__email__}> and <{__github__}>'

__all__ = [
    'generator',
    'validator'
]

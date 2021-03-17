Demo
====

Aqui você encontra uma pequena demonstração de como utilizar o pacote **fordev** no shell interativo.

Vamos socilitar a geração de dados randômicos de uma pessoa com as seguintes características:

- **É do sexo masculino**
- **Tem 25 anos de idade**
- **E mora no estado de SP**

.. code-block:: python

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
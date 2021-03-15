.. fordev documentation master file, created by
   sphinx-quickstart on Mon Mar 15 16:58:23 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Fordev - Documentação oficial
=============================

.. image:: https://img.shields.io/pypi/status/fordev?color=black
    :alt: PyPI - Status
    :target: https://pypi.org/project/fordev/

.. image:: https://img.shields.io/pypi/dm/fordev?color=black
    :alt: Downloads in month
    :target: https://pypi.org/project/fordev/

.. image:: https://img.shields.io/pypi/v/fordev?color=black
    :alt: PyPI
    :target: https://pypi.org/project/fordev/

.. image:: https://img.shields.io/github/v/release/matheusfelipeog/fordev?color=black
    :alt: GitHub release (latest by date)
    :target: https://github.com/matheusfelipeog/fordev/releases

.. image:: https://readthedocs.org/projects/fordev/badge/?version=latest&color=black
    :alt: Documentation Status
    :target: https://fordev.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/github/license/matheusfelipeog/fordev?color=black
    :alt: License MIT
    :target: https://github.com/matheusfelipeog/fordev/blob/master/LICENSE


Index
-----

- `O objetivo <#id1>`_
- `Instalação <#id2>`_
- `Demo <#id3>`_
- `Funcionalidades <#id5>`_

  - `fordev.generators <#id6>`_
  - `fordev.validators <#id7>`_

- `Contribuições <#id8>`_
- `Aviso Legal <#id9>`_
- `Licença <#id10>`_
- `Índices e tabela <#id11>`_

.. toctree::
   :caption: Docs
   :maxdepth: 1

   fordev/fordev


O objetivo
----------

O site `4Devs <https://4devs.com.br>`_ disponibiliza diversas funcionalidades muito úteis para um desenvolvedor utilizar em seus projetos que necessitam de dados randômicos válidos e outras peculiaridades, tais como: dados dos principais documentos pessoais do brasil (CPF, CNPJ, CNH etc), dados bancários, dados de cartões de crédito, dados completos de pessoas (nome, idade, documentos, endereço etc) e muitos outros geradores de dados. Porém, até o momento, não possui uma interface/API pública para utiliza-los diretamente no código da aplicação em desenvolvimento, assim, sendo necessário ir buscar tais dados diretamente no site.

**Fordev** foi construído para resolver esse problema, disponibilizando um módulo de fácil uso que mapeia todo o site 4Devs usando técnicas de scraping, de modo que seja possível obter todos os tipos de dados que são gerados no site.


Instalação
----------

Para instalar, certifique-se de que tenha `Python <https://www.python.org/>`_ e o gerenciador de pacotes ``pip`` instalados em seu ambiente.

Instale com ``pip``:

.. code-block:: bash

   $ pip install fordev


OBS: fordev precisa de acesso a internet para funcionar corretamente, certifique-se de que também a tenha.


Demo
----

Socilitando dados randômicos de uma pessoa do sexo *masculino*, de *25 anos de idade* e que *mora em SP*.

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


Confira a seção de `funcionalidades <#funcionalidades>`_ para ver todas as funções atualmente disponíveis no módulo **fordev**.


Funcionalidades
---------------

Abaixo estão todas as funções correspondentes às funcionalidades disponíveis e que foram mapeadas no site 4Devs.

Você pode conferir a `Documentação Oficial <https://github.com/matheusfelipeog/fordev/blob/master/doc/README.md>`_ para ver uma explicação detalhada e exemplos do uso de todas as funções.

`fordev.generators`
^^^^^^^^^^^^^^^^^^^

- ``certificate(...)`` - Gerador de certidões de nascimento, casamento e óbito;
- ``cnh(...)`` -  Gerador de CNH (Carteira Nacional de Habilitação);
- ``bank_account(...)`` - Gerador de contas bancárias;
- ``cpf(...)`` - Gerador de CPF (Cadastro de Pessoas Físicas);
- ``pis_pasep(...)`` - Gerador de PIS/PASEP (Programa de Integração Social e Programa de Formação do Patrimônio do Servidor Público);
- ``renavam(...)`` - Gerador de RENAVAM (Registro Nacional de Veículos Automotores);
- ``vehicle(...)`` - Gerador de veículos;
- ``vehicle_brand(...)`` - Gerador de marca de veículos;
- ``vehicle_plate(...)`` - Gerador de placa de veículos;
- ``cnpj(...)`` - Gerador de CNPJ (Cadastro Nacional da Pessoa Jurídica);
- ``rg(...)`` - Gerador de RG (Registro Geral) emitido por SSP-SP;
- ``state_registration(...)`` - Gerador de Inscrições Estaduais válidas para todos os estados;
- ``voter_title(...)`` - Gerador de título de eleitor;
- ``credit_card(...)`` - Gerador de dados de cartão de crédito;
- ``people(...)`` - Gerador de dados de pessoas (Nome, RG, CPF, CEP e Endereço);
- ``company(...)`` - Gerador de dados de empresa (Nome, Razão Social, Inscrição Estadual, CNPJ, CEP e Endereço);
- ``uf(...)`` - Gerador de código de UF (Unidade Federativa);
- ``city(...)`` - Gerador de cidades do brasil por estado selecionado.

`fordev.validators`
^^^^^^^^^^^^^^^^^^^

- ``credit_card(...)`` - Verifica se o código de cartão de crédito passado é válido;
- ``bank_account(...)`` - Verifica se os dados da conta bancária passado é válido;
- ``certificate(...)`` - Verifica se o código de certidão passado é válido;
- ``cnh(...)`` - Verifica se o código do CNH passado é válido;
- ``cnpj(...)`` - Verifica se o código do cnpj passado é válido;
- ``cpf(...)`` - Verifica se o código do cpf passado é válido;
- ``pis_pasep(...)`` - Verifica se o código do PIS/PASEP passado é válido;
- ``renavam(...)`` - Verifica se o código do RENAVAM passado é válido;
- ``rg(...)`` - Verifica se o código do RG passado é válido;
- ``voter_title(...)`` - Verifica se o código do Título de Eleitor passado é válido;
- ``state_registration(...)`` - Verifica se o código da Inscrição Estadual passado é válido.


Contribuições
-------------

Toda contribuição é super bem-vinda!

Abaixo mostro com o que você pode contribuir:

- Encontrou algum bug, quer propor uma nova funcionalidade ou conversar sobre o projeto? `Abra uma Issue <https://github.com/matheusfelipeog/fordev/issues>`_ e descreve seu caso.

- Existe uma issue aberta e você quer resolve-la, quer implementar uma nova funcionalidade ou melhorar a documentação? Faça suas adições e me envie um *Pull Request*

- Gostou do projeto, mas não quer ou ainda não consegue contribuir com ele? Considere deixar uma estrela ⭐ para o **Fordev**

Obrigado pelo interesse em colaborar de alguma forma com o projeto 😄


Aviso Legal
-----------

Todo os dados são gerados de forma randômica, respeitando as regras de criação de cada tipo de dado. 

Todo os dados gerados são para fins informativos e utilizados para auxiliar estudantes, programadores, analistas e testadores no desenvolvimento de softwares que necessitem de tais dados. Não devem ser considerados completos, atualizados, e não se destinam a ser utilizado no lugar de uma consulta jurídica, médica, financeira, ou de qualquer outro profissional. Todo e qualquer risco da utilização dos dados disponibilizados atráves do módulo **Fordev** é assumido pelo próprio usuário.

O aviso acima é uma adaptação para utilização no repositório, confira os termos de uso oficial do site 4Devs em: `Termos de Uso <https://www.4devs.com.br/termos_de_uso>`_


Licença
-------

**Fordev** utiliza a *licença MIT* em todo seu código, confira suas condições em `MIT License <https://github.com/matheusfelipeog/fordev/blob/master/LICENSE>`_.


Índices e tabela
----------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

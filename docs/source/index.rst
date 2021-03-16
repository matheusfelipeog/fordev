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


Está é a documentação oficial e completa do módulo **Fordev**, aqui você encontrará exemplos e uma explicação individual de cada função geradora e
validadora de dados disponibilizados e mapeados no site `4Devs <https://4devs.com.br>`_.

Caso queira obter mais detalhes sobre o projeto, confira o ``README.md`` na página inicial do repositório do `Fordev <https://github.com/matheusfelipeog/fordev>`_.


Index
-----

- `Demo <#id3>`_
- `Funcionalidades <#id5>`_

  - `fordev.generators <#id6>`_
  - `fordev.validators <#id7>`_

- `Contribuições <#id8>`_
- `Aviso Legal <#id9>`_
- `Licença <#id10>`_
- `Índices e tabela <#id11>`_

.. toctree::
   :caption: Fordev
   :maxdepth: 2

   install
   demo
   fordev/fordev
   terms


Funcionalidades
---------------

Abaixo estão todas as funções correspondentes às funcionalidades disponíveis e que foram mapeadas no site 4Devs.

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


Licença
-------

**Fordev** utiliza a *licença MIT* em todo seu código, confira suas condições em `MIT License <https://github.com/matheusfelipeog/fordev/blob/master/LICENSE>`_.


Índices e tabela
----------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

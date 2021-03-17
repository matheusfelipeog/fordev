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
    :target: https://fordev.readthedocs.io/pt_BR/latest/?badge=latest

.. image:: https://img.shields.io/github/license/matheusfelipeog/fordev?color=black
    :alt: License MIT
    :target: https://github.com/matheusfelipeog/fordev/blob/master/LICENSE


.. toctree::
    :hidden:
    :caption: Index
    :maxdepth: 1

    install
    demo
    fordev/fordev
    contributions
    terms
    license

Está é a documentação oficial e completa do módulo **Fordev**, aqui você encontrará exemplos e uma explicação individual de cada função geradora e
validadora de dados disponibilizados e mapeados no site `4Devs <https://4devs.com.br>`_.

Caso queira obter mais detalhes sobre o projeto, confira o ``README.md`` no `repositório <https://github.com/matheusfelipeog/fordev>`_.


Objetivo
--------

O site 4Devs disponibiliza diversas funcionalidades muito úteis para um desenvolvedor utilizar em seus projetos que necessitam
de dados randômicos válidos e outras peculiaridades, tais como: dados dos principais documentos pessoais do brasil (CPF, CNPJ, CNH etc),
dados bancários, dados de cartões de crédito, dados completos de pessoas (nome, idade, documentos, endereço etc) e muitos outros geradores
de dados. Porém, até o momento, não possui uma interface/API pública para utiliza-los diretamente no código da aplicação em desenvolvimento,
assim, sendo necessário ir buscar tais dados diretamente no site.

Fordev foi construído para resolver esse problema, disponibilizando um módulo de fácil uso que mapeia todo o site 4Devs usando técnicas de
scraping, de modo que seja possível obter todos os tipos de dados que são gerados no site.  


Índices e tabela
----------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

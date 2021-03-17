fordev.validators
=================

Este módulo válida os dados utilizando o site `4Devs <https://www.4devs.com.br/>`_ e disponibiliza uma API simples para uso.

Use a função ``help()`` para mais informações:

.. code-block:: python

    >>> from fordev import validators
    >>> help(validators)
    Help on module fordev.validators in fordev:

    NAME
        fordev.validators

    DESCRIPTION
    (...)


Parâmetros Comuns
-----------------

Muitas funções do módulo ``fordev.validators`` contém parâmetros em comum,
são eles:

``data_only: bool``
    Se receber o valor ``True``, retorna somente os dados em texto puro.
    Se receber o valor ``False``, retorna um dicionário contendo uma chave ``msg`` e ``data`` ou ``error``
    contendo valores correspondentes à nomenclatura de suas chaves.

Sendo assim, sempre que o encontrar, utilize conforme o descrito acima.


Docs de todas funções
---------------------

.. autofunction:: fordev.validators.is_valid_credit_card
.. autofunction:: fordev.validators.is_valid_bank_account
.. autofunction:: fordev.validators.is_valid_certificate
.. autofunction:: fordev.validators.is_valid_cnh
.. autofunction:: fordev.validators.is_valid_cnpj
.. autofunction:: fordev.validators.is_valid_cpf
.. autofunction:: fordev.validators.is_valid_pis_pasep
.. autofunction:: fordev.validators.is_valid_renavam
.. autofunction:: fordev.validators.is_valid_rg
.. autofunction:: fordev.validators.is_valid_voter_title
.. autofunction:: fordev.validators.is_valid_state_registration
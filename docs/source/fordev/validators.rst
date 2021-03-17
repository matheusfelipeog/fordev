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

    :Bandeiras suportadas:

        ``1`` = **MasterCard**

        ``2`` = **Visa 16 Dígitos**

        ``3`` = **Visa Electron**

        ``4`` = **American Express**

        ``5`` = **Diners Club**

        ``6`` = **Discover**

        ``7`` = **enRoute**

        ``8`` = **JCB**

        ``9`` = **Maestro**

        ``10`` = **Solo**

        ``11`` = **Switch**

        ``12`` = **Laser**

        .. note::

            O valor númerico que representa a bandeira do cartão de crédito deve ser passada para o parâmetro ``flag``.

            **Exemplo:**

            .. code-block:: python

                >>> from fordev.validators import is_valid_credit_card
                >>> is_valid_credit_card(flag=3)  # Visa Electron

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
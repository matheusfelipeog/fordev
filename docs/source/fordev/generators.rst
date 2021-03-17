fordev.generators
=================

Este módulo coleta dados aleatórios gerados pelo site `4Devs <https://www.4devs.com.br/>`_ e disponíbiliza uma API simples para uso.

Use a função ``help()`` para mais informações:

.. code-block:: python

    >>> from fordev import generators
    >>> help(generators)
    Help on module fordev.generators in fordev:

    NAME
        fordev.generators

    DESCRIPTION
    (...)


Parâmetros Comuns
-----------------

Muitas funções do módulo ``fordev.generators`` contém parâmetros em comum,
são eles:

``uf_code: str``
    Recebe o Código da **Unidade Federativa** para geração do dado.
    
    Caso não saiba o que é ou não conheça o do estado que necessita, 
    obtenha mais informações em: https://pt.wikipedia.org/wiki/Subdivis%C3%B5es_do_Brasil

``formatting: bool``
    Se receber o valor ``True``, retorna os dados formatados.
    Se receber o valor ``False``, retorna os dados sem formatação.

``data_only: bool``
    Se receber o valor ``True``, retorna somente os dados em texto puro.
    Se receber o valor ``False``, retorna um dicionário contendo uma chave ``msg`` e ``data`` ou ``error``
    contendo valores correspondentes à nomenclatura de suas chaves.

Sendo assim, sempre que os encontrar, utilize conforme o descrito acima.


Docs de todas funções
---------------------

.. autofunction:: fordev.generators.certificate
    
    :Tipos de certidões:

        ``I`` = **Indifferent** (Indiferente) `<Padrão>`

        ``B`` = **Birth** (Nascimento)

        ``W`` = **Wedding** (Casamento)

        ``R`` = **Religious** Wedding (Casamento Religioso)

        ``D`` = **Death (Morte)**

        .. note::

            Os tipos de certidões devem ser passados para o parâmetro ``type_``.

            **Exemplo:**

            .. code-block:: python

                >>> from fordev.generators import certificate
                >>> certificate(type_='B')


.. autofunction:: fordev.generators.cnh
.. autofunction:: fordev.generators.bank_account
.. autofunction:: fordev.generators.cpf
.. autofunction:: fordev.generators.pis_pasep
.. autofunction:: fordev.generators.renavam
.. autofunction:: fordev.generators.vehicle
.. autofunction:: fordev.generators.vehicle_brand
.. autofunction:: fordev.generators.vehicle_plate
.. autofunction:: fordev.generators.cnpj
.. autofunction:: fordev.generators.rg
.. autofunction:: fordev.generators.state_registration
.. autofunction:: fordev.generators.voter_title
.. autofunction:: fordev.generators.credit_card
.. autofunction:: fordev.generators.people
.. autofunction:: fordev.generators.company
.. autofunction:: fordev.generators.uf
.. autofunction:: fordev.generators.city
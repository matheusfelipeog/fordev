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
    
    :Certidões suportadas:

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

    :Bandeiras suportadas:

        ``0`` = **Aleatório** `<Padrão>`

        ``1`` = **Banco do Brasil**

        ``2`` = **Bradesco**

        ``3`` = **Citibank**

        ``4`` = **Itaú**

        ``5`` = **Santander**
        
        .. note::

            O valor númerico que representa a bandeira do banco deve ser passada para o parâmetro ``bank``.

            **Exemplo:**

            .. code-block:: python

                >>> from fordev.generators import bank_account
                >>> bank_account(bank=2)  # Banco Bradesco

.. autofunction:: fordev.generators.cpf
.. autofunction:: fordev.generators.pis_pasep
.. autofunction:: fordev.generators.renavam

.. autofunction:: fordev.generators.vehicle

    :Marcas suportadas:

        ``0`` = **Aleatório** `<Padrão>`

        ``1`` = **Acura**

        ``2`` = **Agrale**

        ``3`` = **Alfa Romeo**

        ``4`` = **AM Gen**

        ``5`` = **Asia Motors**

        ``6`` = **ASTON MARTIN**

        ``7`` = **Audi**

        ``8`` = **BMW**

        ``9`` = **BRM**

        ``10`` = **Buggy**

        ``11`` = **Bugre**

        ``12`` = **Cadillac**

        ``13`` = **CBT Jipe**

        ``14`` = **CHANA**

        ``15`` = **CHANGAN**

        ``16`` = **CHERY**

        ``17`` = **Chrysler**

        ``18`` = **Citroen**

        ``19`` = **Cross Lander**

        ``20`` = **Daewoo**

        ``21`` = **Daihatsu**

        ``22`` = **Dodge**

        ``23`` = **EFFA**

        ``24`` = **Engesa**

        ``25`` = **Envemo**

        ``26`` = **Ferrari**

        ``27`` = **Fiat**

        ``28`` = **Fibravan**

        ``29`` = **Ford**

        ``30`` = **FOTON**

        ``31`` = **Fyber**

        ``32`` = **GEELY**

        ``33`` = **GM - Chevrolet**

        ``34`` = **GREAT WALL**

        ``35`` = **Gurgel**

        ``36`` = **HAFEI**

        ``37`` = **Honda**

        ``38`` = **Hyundai**

        ``39`` = **Isuzu**

        ``40`` = **JAC**

        ``41`` = **Jaguar**

        ``42`` = **Jeep**

        ``43`` = **JINBEI**

        ``44`` = **JPX**

        ``45`` = **Kia Motors**

        ``46`` = **Lada**

        ``47`` = **LAMBORGHINI**

        ``48`` = **Land Rover**

        ``49`` = **Lexus**

        ``50`` = **LIFAN**

        ``51`` = **LOBINI**

        ``52`` = **Lotus**

        ``53`` = **Mahindra**

        ``54`` = **Maserati**

        ``55`` = **Matra**

        ``56`` = **Mazda**

        ``57`` = **Mercedes-Benz**

        ``58`` = **Mercury**

        ``59`` = **MG**

        ``60`` = **MINI**

        ``61`` = **Mitsubishi**

        ``62`` = **Miura**

        ``63`` = **Nissan**

        ``64`` = **Peugeot**

        ``65`` = **Plymouth**

        ``66`` = **Pontiac**

        ``67`` = **Porsche**

        ``68`` = **RAM**

        ``69`` = **RELY**

        ``70`` = **Renault**

        ``71`` = **Rolls-Royce**

        ``72`` = **Rover**

        ``73`` = **Saab**

        ``74`` = **Saturn**

        ``75`` = **Seat**

        ``76`` = **SHINERAY**

        ``77`` = **smart**

        ``78`` = **SSANGYONG**

        ``79`` = **Subaru**

        ``80`` = **Suzuki**

        ``81`` = **TAC**

        ``82`` = **Toyota**

        ``83`` = **Troller**

        ``84`` = **Volvo**

        ``85`` = **VW - VolksWagen**

        ``86`` = **Wake**

        ``87`` = **Walk**
            
        .. note::

            O valor númerico que representa a marca do veículo deve ser passada para o parâmetro ``brand_code``.

            **Exemplo:**

            .. code-block:: python

                >>> from fordev.generators import vehicle
                >>> vehicle(brand_code=26)  # Ferrari

.. autofunction:: fordev.generators.vehicle_brand
.. autofunction:: fordev.generators.vehicle_plate
.. autofunction:: fordev.generators.cnpj
.. autofunction:: fordev.generators.rg
.. autofunction:: fordev.generators.state_registration
.. autofunction:: fordev.generators.voter_title

.. autofunction:: fordev.generators.credit_card

    :Bandeiras suportadas:

        ``0`` = **Aleatório** `<Padrão>`

        ``1`` = **MasterCard**

        ``2`` = **Visa 16 Dígitos**

        ``3`` = **American Express**

        ``4`` = **Diners Club**

        ``5`` = **Discover**

        ``6`` = **enRoute**

        ``7`` = **JCB**

        ``8`` = **Voyager**

        ``9`` = **HiperCard**

        ``10`` = **Aura**

        .. note::

            O valor númerico que representa a bandeira do cartão de crédito deve ser passada para o parâmetro ``bank``.

            **Exemplo:**

            .. code-block:: python

                >>> from fordev.generators import credit_card
                >>> credit_card(bank=3)  # American Express

.. autofunction:: fordev.generators.people
.. autofunction:: fordev.generators.company
.. autofunction:: fordev.generators.uf
.. autofunction:: fordev.generators.city
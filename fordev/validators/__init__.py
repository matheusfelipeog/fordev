"""
fordev.validators
-----------------

Este módulo válida os dados utilizando o site `4Devs <https://www.4devs.com.br/>`_
e disponibiliza uma API simples para uso.

Use a função ``help()`` para mais informações:

>>> from fordev import validators
>>> help(validators)
Help on module fordev.validators in fordev:

NAME
    fordev.validators

DESCRIPTION
(...)

Ou consulte a documentação oficial.

Note
----
Muitas funções do módulo ``fordev.validators`` contém parâmetros em comum,
todos estão descritos abaixo.

More details in next section.

Parameter
---------
data_only: bool
    Se receber o valor ``True``, retorna somente os dados em texto puro.
    Se receber o valor ``False``, retorna um dicionário contendo uma chave ``msg`` e ``data`` ou ``error``
    contendo valores correspondentes à nomenclatura de suas chaves.

Sendo assim, sempre que o encontrar, utilize conforme o descrito acima.
"""

Instalação
==========

Use ``pip`` e ``virtualenv`` para instalar **fordev** em seu ambiente. Isso irá separar as dependências do módulo fordev dos módulos instalados globalmente em seu sistema.

Instalação com pip
------------------

Crie e entre no diretório do seu projeto:

.. code-block:: bash

    $ mkdir my_project && cd my_project

Crie e ative o ambiente virtual:

.. code-block:: bash
    
    $ virtualenv venv && source venv/Scripts/activate

.. note::

    Em ambiente linux, use ``source venv/bin/activate`` para ativar o ambiente virtual.

Instale com ``pip``:

.. code-block:: bash

   $ pip install fordev

Pronto, pode começar o trabalho ;)

Instalação
==========

.. note::

    Para instalar, certifique-se de que tenha `Python <https://www.python.org/>`_ e um dos gerenciadores de pacote utilizados instalado em seu ambiente.

.. note::

    **OBS:** fordev precisa de acesso a internet para funcionar corretamente, certifique-se de que também a tenha.


Use ``pipenv`` para instalar **fordev** em seu ambiente. Ele criará um ambiente virtual e separar todas as dependências e subdependências do seu ambiente global.

Instalação com pipenv
---------------------

Crie e entre no diretório do seu projeto:

.. code-block:: bash

    $ mkdir my_project && cd my_project

Instale usando pipenv:

.. code-block:: bash

    $ pipenv install fordev

Agora ative o ambiente virtual:

.. code-block:: bash

    $ pipenv shell


Instalação com pip
------------------

Como alternativa, caso não queira usar ``pipenv``, utilize ``pip`` + ``virtualenv`` para fazer a mesma coisa.

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

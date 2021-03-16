Referência
==========

Aqui você encontra a referência completa do pacote **fordev**, podendo ser usado como referência de uso ou referência de desenvolvimento.

.. automodule:: fordev
    :no-members:

Funcionalidades
---------------

Os módulos e funções internos que contém a API para uso são:

- ``fordev.generators`` - **O módulo que contém a API para geração de dados.**

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

- ``fordev.validators`` - **O módulo que contém a API para validação de dados.**

    - ``is_valid_credit_card(...)`` - Verifica se o código de cartão de crédito passado é válido;
    - ``is_valid_bank_account(...)`` - Verifica se os dados da conta bancária passado é válido;
    - ``is_valid_certificate(...)`` - Verifica se o código de certidão passado é válido;
    - ``is_valid_cnh(...)`` - Verifica se o código do CNH passado é válido;
    - ``is_valid_cnpj(...)`` - Verifica se o código do cnpj passado é válido;
    - ``is_valid_cpf(...)`` - Verifica se o código do cpf passado é válido;
    - ``is_valid_pis_pasep(...)`` - Verifica se o código do PIS/PASEP passado é válido;
    - ``is_valid_renavam(...)`` - Verifica se o código do RENAVAM passado é válido;
    - ``is_valid_rg(...)`` - Verifica se o código do RG passado é válido;
    - ``is_valid_voter_title(...)`` - Verifica se o código do Título de Eleitor passado é válido;
    - ``is_valid_state_registration(...)`` - Verifica se o código da Inscrição Estadual passado é válido.

Todos os demais módulos internos são os responsáveis por manter o pacote **fordev** funcional.
Apenas os consulte/use se deseja compreender seu funcionamento e/ou contribuir com o projeto. 

Obtenha mais detalhes dos módulos internos na seção abaixo:

.. toctree::
   :caption: Módulos Internos
   :maxdepth: 1

   generators
   validators
   core
   filters
<h1 align="center">
    <img src="../.github/assets/images/fordev.png" alt="Logo Fordev" width="500px" />
</h1>

<p align="center">
    <img src="https://img.shields.io/github/license/matheusfelipeog/fordev?color=black&style=for-the-badge" alt="License MIT" />
</p>

<h2 align="center">Documentação Oficial</h2>

Está é a documentação oficial e completa do módulo **Fordev**, aqui você encontrará exemplos e uma explicação individual de cada função geradora, validadora e manipuladora de dados disponibilizados no site [4Devs](https://4devs.com.br).


## Funcionalidades

Abaixo estão todas as funções correspondentes às funcionalidades disponíveis e que foram mapeadas no site 4Devs. 

Caso queira pular para a documentação de uma função em específico, basta clicar no nome da função desejada abaixo.

### `fordev.generator`

- [`certificate(...)`](#certificate) - Gerador de certidões de nascimento, casamento e óbito;
- [`cnh(...)`](#cnh) - Gerador de CNH (Carteira Nacional de Habilitação);
- [`bank_account(...)`](#bank_account) - Gerador de contas bancárias;
- [`cpf(...)`](#cpf) - Gerador de CPF (Cadastro de Pessoas Físicas);
- `pis_pasep(...)` - Gerador de PIS/PASEP (Programa de Integração Social and Programa de Formação do Patrimônio do Servidor Público);
- `renavam(...)` - Gerador de RENAVAM (Registro Nacional de Veículos Automotores);
- `vehicle(...)` - Gerador de veículos;
- `vehicle_brand(...)` - Gerador de marca de veículos;
- `vehicle_plate(...)` - Gerador de placa de veículos;
- `cnpj(...)` - Gerador de CNPJ (Cadastro Nacional da Pessoa Jurídica);
- `rg(...)` - Gerador de RG (Registro Geral) emitido por SSP-SP;
- `state_registration(...)` - Gerador de Inscrições Estaduais válidas para todos os estados;
- `voter_title(...)` - Gerador de título de eleitor;
- `credit_card(...)` - Gerador de dados de cartão de crédito;
- `people(...)` - Gerador de dados de pessoas (Nome, RG, CPF, CEP e Endereço);
- `company(...)` - Gerador de dados de empresa (Nome, Razão Social, Inscrição Estadual, CNPJ, CEP e Endereço);
- `uf(...)` - Gerador de código de UF (Unidade Federativa);
- `city(...)` - Gerador de cidades do brasil por estado selecionado.


## Doc

Documentação e exemplos de uso de cada função disponível no módulo **Fordev**.

### Argumentos Genêricos

O módulo `fordev.generator` possui diversas funções que tem argumentos semelhantes ou iguais, então, para simplificar, sempre que encontrar um dos argumentos genêricos disponível em uma das funções, considere-os como o descrito abaixo.

- `state: str` - Corresponde ao código UF (Unidade Federativa) de dois caracteres, maisculos ou minúsculos, que representa o estado a ser utilizado como filtro.
Você pode conferir todos os UFs em [Constantes](https://github.com/matheusfelipeog/fordev/blob/master/fordev/_const.py) ou, para mais detalhes, na [Wikipédia](https://pt.wikipedia.org/wiki/Subdivis%C3%B5es_do_Brasil ).

```python
# Exemplo de uso do argumento 'state'
>>> from fordev.generator import cpf
>>> cpf(state='SP')
```

- `format: bool` - Este argumento representa a formatação contida no retorno de determinado dado gerado, por exemplo um CPF: 123.456.789-10. Você pode especificar `False` para caso não queira que a formatação seja utilizada, assim, com o mesmo exemplo anterior, o CPF ficaria: 12345678910. Ou, pode explicitar `True` para que a formatação seja utilizada (essa opção já é padrão).

```python
# Exemplo de uso do argumento 'format'
>>> from fordev.generator import cpf
>>> cpf(format=False)
```

- `data_only` - Este argumento é um pouco semelhante ao `format`, mas não modificando o dado gerado e sim a estrutura de retorno desse dado. Quando passado o valor `False` para esse argumento, é retornado um `dict` contendo uma mensagem que representa o status da solicitação da geração do dado e o dado em si. De modo oposto, passando o valor `True` é retornado somente o dado (essa opção já é padrão).

```python
# Exemplo de uso do argumento 'data_only'
>>> from fordev.generator import cpf
>>> cpf(data_only=False)

# Output in case of success ------------------------
{'msg': 'success', 'data': '123.456.789-10'}

# Output in case of failed -------------------------
{'msg': 'failed', 'error': 'MENSAGEM DE ERRO AQUI'}
# Ou
{'msg': 'HTTP error', 'error': 'MENSAGEM DE ERRO AQUI'}
```


### `fordev.generator`

Este módulo contém todas as funções geradoras de dados e é responsável por realizar todas as solicitações que corresponde a geração de dados ao site 4Devs.

#### Exemplo:

```python
>>> import fordev.generator
```


### `certificate(...)`

```python
certificate(type_: str='I', format: bool=True, data_only: bool=True) -> str:
```

Gerador de certidões de nascimento, casamento, casamento relogioso e óbito.

#### Argumentos

- `type_: str` - Este argumento rebece um único caracter que especifica qual tipo de certidão que deve ser gerada, são 5 opções disponíveis.
    - Opções
        - 'B' = Birth;
        - 'W' = Wedding;
        - 'R' = Religious Wedding;
        - 'D' = Death;
        - 'I' = Indifferent (Default).

#### Exemplo de uso

```python
>>> from fordev.generator import certificate
>>> certificate(type_='D')
```


### `cnh(...)`

```python
cnh(data_only: bool=True) -> str:
```

Gerador de código CNH (Carteira Nacional de Habilitação) válido.

#### Exemplo de uso

```python
>>> from fordev.generator import cnh
>>> cnh()
```


### `bank_account(...)`

```python
bank_account(bank: int=0, state: str='', data_only: bool=True) -> dict:
```

Gerador de dados de conta bancária (Conta Corrente, Agência, Banco, Cidade e Estado) válido.

#### Argumentos

- `bank: int` - Este argumento recebe um número inteiro, entre 0 a 5, que corresponde a uma bandeira de um dos bancos disponíveis para geração dos dados bancários.
    - Opções
       - 0 = Random (Padrão);
       - 1 = Banco do Brasil;
       - 2 = Bradesco;
       - 3 = Citibank;
       - 4 = Itaú;
       - 5 = Santander.

#### Exemplo de uso

```python
>>> from fordev.generator import bank_account
>>> bank_account(bank=2, state='PB')
```


### `cpf(...)`

```python
cpf(state: str='', format: bool=True, data_only: bool=True) -> str:
```

Gerador de código de CPF (Cadastro de Pessoas Físicas) válidos para todos os estados.

#### Exemplo de uso

```python
>>> from fordev.generator import cpf
>>> cpf(state='AC')
```
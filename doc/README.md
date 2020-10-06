<h1 align="center">
    <img src="../.github/assets/images/fordev.png" alt="Logo Fordev" width="500px" />
</h1>

<p align="center">
    <img src="https://img.shields.io/github/license/matheusfelipeog/fordev?color=black&style=for-the-badge" alt="License MIT" />
</p>

<h2 align="center">Documentação Oficial</h2>

Está é a documentação oficial e completa do módulo **Fordev**, aqui você encontrará exemplos e uma explicação individual de cada função geradora, validadora e manipuladora de dados disponibilizados e mapeados no site [4Devs](https://4devs.com.br).

Caso queira obter mais detalhes sobre o projeto, confira o `README.md` na página inicial do repositório do [**Fordev**](https://github.com/matheusfelipeog/fordev).

Agora, para obter mais detalhes sobre como utilizar o projeto **Fordev**, indico iniciar o estudo pela seção [Doc](#doc).


## Index

Abaixo estão todas as funções correspondentes às funcionalidades disponíveis e que foram mapeadas no site 4Devs.

Caso queira pular para a documentação de uma função/módulo em específico, basta clicar no nome da função desejada abaixo.

- [Doc](#doc) - Inicio da documentação.
    - [Argumentos Genêricos](#argumentos-genêricos) - Explicação dos argumentos genêricos;
    - [Retornos](#retornos) - Explicação e exemplos de todos os possíveis retornos de cada função.
    
- [`fordev.generator`](#fordevgenerator)
    - [`certificate(...)`](#certificate) - Gerador de certidões de nascimento, casamento e óbito;
    - [`cnh(...)`](#cnh) - Gerador de CNH (Carteira Nacional de Habilitação);
    - [`bank_account(...)`](#bank_account) - Gerador de contas bancárias;
    - [`cpf(...)`](#cpf) - Gerador de CPF (Cadastro de Pessoas Físicas);
    - [`pis_pasep(...)`](#pis_pasep) - Gerador de PIS/PASEP (Programa de Integração Social e Programa de Formação do Patrimônio do Servidor Público);
    - [`renavam(...)`](#renavam) - Gerador de RENAVAM (Registro Nacional de Veículos Automotores);
    - [`vehicle(...)`](#vehicle) - Gerador de veículos;
    - [`vehicle_brand(...)`](#vehicle_brand) - Gerador de marca de veículos;
    - [`vehicle_plate(...)`](#vehicle_plate) - Gerador de placa de veículos;
    - [`cnpj(...)`](#cnpj) - Gerador de CNPJ (Cadastro Nacional da Pessoa Jurídica);
    - [`rg(...)`](#rg) - Gerador de RG (Registro Geral) emitido por SSP-SP;
    - [`state_registration(...)`](#state_registration) - Gerador de Inscrições Estaduais válidas para todos os estados;
    - [`voter_title(...)`](#voter_title) - Gerador de título de eleitor;
    - [`credit_card(...)`](#credit_card) - Gerador de dados de cartão de crédito;
    - [`people(...)`](#people) - Gerador de dados de pessoas (Nome, RG, CPF, CEP e Endereço);
    - [`company(...)`](#company) - Gerador de dados de empresa (Nome, Razão Social, Inscrição Estadual, CNPJ, CEP e Endereço);
    - [`uf(...)`](#uf) - Gerador de código de UF (Unidade Federativa);
    - [`city(...)`](#city) - Gerador de cidades do brasil por estado selecionado.

- [`fordev.validator`](#fordevvalidator)
    - [`credit_card(...)`](#credit_card-1) - Verifica se o código de cartão de crédito passado é válido;
    - [`bank_account(...)`](#bank_account-1) - Verifica se os dados da conta bancária passado é válido;
    - [`certificate(...)`](#certificate-1) - Verifica se o código de certidão passado é válido;
    - [`cnh(...)`](#cnh-1) - Verifica se o código do CNH passado é válido;
    - [`cnpj(...)`](#cnpj-1) - Verifica se o código do cnpj passado é válido;
    - [`cpf(...)`](#cpf-1) - Verifica se o código do cpf passado é válido;
    - [`pis_pasep(...)`](#pis_pasep-1) - Verifica se o código do PIS/PASEP passado é válido;
    - [`renavam(...)`](#renavam-1) - Verifica se o código do RENAVAM passado é válido;
    - [`rg(...)`](#rg-1) - Verifica se o código do RG passado é válido;
    - [`voter_title(...)`](#voter_title-1) - Verifica se o código do Título de Eleitor passado é válido;
    - [`state_registration(...)`](#state_registration-1) - Verifica se o código da Inscrição Estadual passado é válido.


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

- `formatting: bool` - Este argumento representa a formatação contida no retorno de determinado dado gerado, por exemplo um CPF: 123.456.789-10. Você pode especificar `False` para caso não queira que a formatação seja utilizada, assim, com o mesmo exemplo anterior, o CPF ficaria: 12345678910. Ou, pode explicitar `True` para que a formatação seja utilizada (essa opção já é padrão).

```python
# Exemplo de uso do argumento 'format'
>>> from fordev.generator import cpf
>>> cpf(formatting=False)
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


### Retornos

Muitas das funções disponíveis pelo módulo **Fordev** tem retornos parecidos, variando as msg de sucesso e erro ou os dados, podendo variar de tipo, conforme os argumentos passados, entre: uma string, uma lista ou um dicionário.

Possíveis retornos:

O retorno padrão em quase todas as funções é uma string:
```python
>>> from fordev.generator import cpf
>>> cpf(data_only=False)

# Retorna uma string
'123.456.789-10'
```

Algumas funções tem uma lista de strings como retorno:
```python
>>> from fordev.generator import uf
>>> uf(n=10)

# Retorna uma lista de string
['PE', 'PI', 'RS', 'SP', 'CE', 'AL', 'TO', 'MT', 'MS', 'RR']
```

Também tem funções que tem um dicionário de dados como retorno:
```python
>>> from fordev.generator import people
>>> people(sex='M', age=25, state='SP')

# Retorna um dicionário
{
    'altura': '1,90',
    'bairro': 'Jardim Maria Amélia',
    'celular': '(12) 98401-5301',
    'cep': '12318-110',
    'cidade': 'Jacareí',
    'cor': 'laranja',
    'cpf': '061.632.758-70',
    'data_nasc': '06/12/1995',
    'email': 'bentoyagolorenzogoncalves-72@alcastro.com.br',
    'endereco': 'Rua José Benedito de Oliveira',
    'estado': 'SP',
    'idade': 25,
    'mae': 'Tereza Melissa Priscila',
    'nome': 'Bento Yago Lorenzo Gonçalves',
    'numero': 760,
    'pai': 'Sérgio Guilherme Erick Gonçalves',
    'peso': 88,
    'rg': '23.920.314-8',
    'senha': 'ErOKUUyoml',
    'sexo': 'Masculino',
    'signo': 'Sagitário',
    'telefone_fixo': '(12) 2844-9806',
    'tipo_sanguineo': 'AB+'
}
```

Em caso de erros ou a função que tiverem o argumento `data_only` receber o valor `False`, também retornam um dicionário de dados:
```python
>>> from fordev.generator import cpf
>>> cpf(data_only=False)

# Retorno em caso de falha no processo de scraping
{'msg': 'failed', 'error': 'MENSAGEM DE ERRO AQUI'}

# Retorno em caso de falha com o protocolo HTTP
{'msg': 'HTTP error', 'error': 'MENSAGEM DE ERRO AQUI'}

# Retorno caso o argumento 'data_only' receber o valor 'False'
{'msg': 'success', 'data': '123.456.789-10'}

```


### `fordev.generator`

Este módulo contém todas as funções geradoras de dados e é responsável por realizar todas as solicitações que corresponde a geração de dados ao site 4Devs.

#### Exemplo:

```python
>>> import fordev.generator
```


### `certificate(...)`

```python
certificate(type_: str='I', formatting: bool=True, data_only: bool=True) -> str
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
cnh(data_only: bool=True) -> str
```

Gerador de código CNH (Carteira Nacional de Habilitação) válido.

#### Exemplo de uso

```python
>>> from fordev.generator import cnh
>>> cnh()
```


### `bank_account(...)`

```python
bank_account(bank: int=0, state: str='', data_only: bool=True) -> dict
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
cpf(state: str='', formatting: bool=True, data_only: bool=True) -> str
```

Gerador de código de CPF (Cadastro de Pessoas Físicas) válidos para todos os estados.

#### Exemplo de uso

```python
>>> from fordev.generator import cpf
>>> cpf(state='AC')
```


### `pis_pasep(...)`

```python
pis_pasep(formatting: bool=True, data_only: bool=True) -> str
```

Gerador de código de PIS/PASEP (Programa de Integração Social e Programa de Formação do Patrimônio do Servidor Público) válido.

#### Exemplo de uso

```python
>>> from fordev.generator import pis_pasep
>>> pis_pasep()
```


### `renavam(...)`

```python
renavam(data_only: bool=True) -> str
```

Gerador de código de RENAVAM (Registro Nacional de Veículos Automotores) válido.

#### Exemplo de uso

```python
>>> from fordev.generator import renavam
>>> renavam()
```


### `vehicle(...)`

```python
vehicle(brand_code: int=0, state: str='', formatting: bool=True, data_only: bool=True) -> dict
```

Gerador de dados de veículo (Marca, Modelo, Ano, Renavam, Placa e Cor) válido.

#### Argumentos

- `brand_code: int` - Este argumento recebe um número inteiro, entre 0 a 87, que corresponde a uma marca de veículo disponível para geração dos dados.
    - Opções
        - 0 = Random (Padrão);
        - 1 = Acura;
        - 2 = Agrale;
        - 3 = Alfa Romeo;
        - 4 = AM Gen;
        - 5 = Asia Motors;
        - 6 = ASTON MARTIN;
        - 7 = Audi;
        - 8 = BMW;
        - 9 = BRM;
        - 10 = Buggy;
        - 11 = Bugre;
        - 12 = Cadillac;
        - 13 = CBT Jipe;
        - 14 = CHANA;
        - 15 = CHANGAN;
        - 16 = CHERY;
        - 17 = Chrysler;
        - 18 = Citroen;
        - 19 = Cross Lander;
        - 20 = Daewoo;
        - 21 = Daihatsu;
        - 22 = Dodge;
        - 23 = EFFA;
        - 24 = Engesa;
        - 25 = Envemo;
        - 26 = Ferrari;
        - 27 = Fiat;
        - 28 = Fibravan;
        - 29 = Ford;
        - 30 = FOTON;
        - 31 = Fyber;
        - 32 = GEELY;
        - 33 = GM - Chevrolet;
        - 34 = GREAT WALL;
        - 35 = Gurgel;
        - 36 = HAFEI;
        - 37 = Honda;
        - 38 = Hyundai;
        - 39 = Isuzu;
        - 40 = JAC;
        - 41 = Jaguar;
        - 42 = Jeep;
        - 43 = JINBEI;
        - 44 = JPX;
        - 45 = Kia Motors;
        - 46 = Lada;
        - 47 = LAMBORGHINI;
        - 48 = Land Rover;
        - 49 = Lexus;
        - 50 = LIFAN;
        - 51 = LOBINI;
        - 52 = Lotus;
        - 53 = Mahindra;
        - 54 = Maserati;
        - 55 = Matra;
        - 56 = Mazda;
        - 57 = Mercedes-Benz;
        - 58 = Mercury;
        - 59 = MG;
        - 60 = MINI;
        - 61 = Mitsubishi;
        - 62 = Miura;
        - 63 = Nissan;
        - 64 = Peugeot;
        - 65 = Plymouth;
        - 66 = Pontiac;
        - 67 = Porsche;
        - 68 = RAM;
        - 69 = RELY;
        - 70 = Renault;
        - 71 = Rolls-Royce;
        - 72 = Rover;
        - 73 = Saab;
        - 74 = Saturn;
        - 75 = Seat;
        - 76 = SHINERAY;
        - 77 = smart;
        - 78 = SSANGYONG;
        - 79 = Subaru;
        - 80 = Suzuki;
        - 81 = TAC;
        - 82 = Toyota;
        - 83 = Troller;
        - 84 = Volvo;
        - 85 = VW - VolksWagen;
        - 86 = Wake;
        - 87 = Walk.

#### Exemplo de uso

```python
>>> from fordev.generator import vehicle
>>> vehicle(brand_code=26 state='SP')
```


### `vehicle_brand(...)`

```python
vehicle_brand(n: int=1, data_only: bool=True) -> list
```

Gerador de nome de marca de veículos válidos.

#### Argumentos

- `n: int` - Este argumento recebe um número inteiro, entre 1 a 87, que corresponde a quantidade de nomes de marcas de veículos a ser gerado.

#### Exemplo de uso

```python
>>> from fordev.generator import vehicle_brand
>>> vehicle_brand(n=35)
```


### `vehicle_plate(...)`

```python
vehicle_plate(state: str='', formatting: bool=True, data_only: bool=True) -> str
```

Gerador de código de placa de veículo válido.

#### Exemplo de uso

```python
>>> from fordev.generator import vehicle_plate
>>> vehicle_plate(state='RJ')
```


### `cnpj(...)`

```python
cnpj(formattingt: bool=True, data_only: bool=True) -> str
```

Gerador de código de CNPJ (Cadastro Nacional da Pessoa Jurídica) válido.

#### Exemplo de uso

```python
>>> from fordev.generator import cnpj
>>> cnpj()
```


### `rg(...)`

```python
rg(formatting: bool=True, data_only: bool=True) -> str
```

Gerador de código de RG (Registro Geral) emitido por SSP-SP.

#### Exemplo de uso

```python
>>> from fordev.generator import rg
>>> rg()
```


### `state_registration(...)`

```python
state_registration(state: str='SP', formatting: bool=True, data_only: bool=True) -> str
```

Gerador de código de Inscrições Estaduais válidas para todos os estados.

#### Exemplo de uso

```python
>>> from fordev.generator import state_registration
>>> state_registration(state='BA')
```


### `voter_title(...)`

```python
voter_title(state: str, data_only: bool=True) -> str
```

Gerador de código de Título de Eleitor válido para todos os estados.

#### Exemplo de uso

```python
>>> from fordev.generator import voter_title
>>> voter_title(state='AC')
```


### `credit_card(...)`

```python
credit_card(bank: int=0, formatting: bool=True, data_only: bool=True) -> dict
```

Gerador de dados de cartão de crédito (Número, Data de Validade e CVV) válidos.

#### Argumentos

- `bank: int` - Este argumento recebe um número inteiro, entre 0 a 10, que corresponde a uma bandeira de um dos bancos disponíveis para geração dos dados bancários.
    - Opções
        - 0 = Random;
        - 1 = MasterCard;
        - 2 = Visa 16 Dígitos;
        - 3 = American Express;
        - 4 = Diners Club;
        - 5 = Discover;
        - 6 = enRoute;
        - 7 = JCB;
        - 8 = Voyager;
        - 9 = HiperCard;
        - 10 = Aura.

#### Exemplo de uso

```python
>>> from fordev.generator import credit_card
>>> credit_card(bank=2)
```


### `people(...)`

```python
people(n: int=1, sex: str='R', age: int=0, state: str='', formatting: bool=True, data_only: bool=True) -> str:
```

Gerador de dados de pessoas (nome, idade, documentos, contatos, endereço etc) válidos.

#### Argumentos

- `n: int` - Este argumento recebe um número inteiro, entre 1 a 30, que corresponde a quantidade de dados de pessoas a ser gerados.

- `sex: str` - Este argumento recebe um único caracter string que corresponde ao sexo da pessoa a ser gerada.
    - Opções
        - 'R' = Random;
        - 'M' = Masculino;
        - 'F' = Feminino.

- `age: int` - Este argumento recebe um número inteiro, entre 18 a 80, que representa a idade da pessoa a ser gerada.

#### Exemplo de uso

```python
>>> from fordev.generator import people
>>> people(n=5, sex='M', age=75)
```


### `company(...)`

```python
company(state: str='SP', age: int=1, formatting: bool=True, data_only: bool=True) -> dict
```

Gerador de dados de empresa (nome, cnpj, endereço, contatos, data de abertura etc) válidos.

#### Argumentos

- `age: int` - Este argumento recebe um número inteiro, entre 1 a 30, que representa o tempo de existência da empresa em anos.

#### Exemplo de uso

```python
>>> from fordev.generator import company
>>> company(state='PB', age=10)
```


### `uf(...)`

```python
uf(n: int=1, data_only: bool=True) -> list
```

Gerador de código UF (Unidade Federativa) de todos os estados.

#### Argumentos

- `n: int` - Este argumento recebe um número inteiro, entre 1 a 27, que corresponde a quantidade de ufs dos estados a serem gerados.

#### Exemplo de uso

```python
>>> from fordev.generator import uf
>>> uf(n=15)
```


### `city(...)`

```python
city(state: str='SP', data_only: bool=True) -> list
```

Gerador de todas as cidade com base no estado selecionado.

#### Exemplo de uso

```python
>>> from fordev.generator import city
>>> city(state='PB')
```


### `fordev.validator`

Todas as funções disponíveis neste módulo são responsáveis por verificar se o dado passado é válido ou não.

#### Exemplo:

```python
>>> import fordev.validator
```


### `credit_card(...)`

```python
credit_card(flag: int, credit_card_code: str, data_only: bool=True) -> bool
```

Verifica se o código da Cartão de Crédito passado é válido.

#### Argumentos

- `flag: int` - Este argumento recebe um número inteiro, entre 1 a 12, que corresponde a bandeira do cartão. Veja a docstring para visualizar o número.

- `credit_card_code: str` - Este argumento corresponde ao código do cartão de crédito.

#### Exemplo de uso

```python
>>> from fordev.validator import credit_card
>>> credit_card(1, '5567 3314 3773 8787')
```


### `bank_account(...)`

```python
bank_account(bank: int, agency: str, account: str, data_only: bool=True) -> bool
```

Verifica se dados da Conta Bancária passado é válido.

#### Argumentos

- `bank: int` - Este argumento recebe um número inteiro, entre 1 a 5, que corresponde ao banco da conta. Veja a docstring para visualizar o número.

- `agency: str` - Este argumento corresponde ao código da agência da conta bancária.

- `account: str` - Este argumento corresponde ao código da conta bancária.

#### Exemplo de uso

```python
>>> from fordev.validator import bank_account
>>> bank_account(1, '0902', '0190451-5')
```


### `certificate(...)`

```python
certificate(certificate_code: str, data_only: bool=True) -> bool
```

Verifica se o código da Certidão passado é válido.

#### Argumentos

- `certificate_code: str` - Este argumento corresponde ao código da certidão.

#### Exemplo de uso

```python
>>> from fordev.validator import certificate
>>> certificate('126239 01 55 2014 1 39856 604 7586258-53')
```


### `cnh(...)`

```python
cnh(cnh_code: str, data_only: bool=True) -> bool
```

Verifica se o código do CNH passado é válido.

#### Argumentos

- `cnh_code: str` - Este argumento corresponde ao código da CNH.

#### Exemplo de uso

```python
>>> from fordev.validator import cnh
>>> cnh('61999385394')
```


### `cnpj(...)`

```python
cnpj(cnpj_code: str, data_only: bool=True) -> bool
```

Verifica se o código do CNPJ passado é válido.

#### Argumentos

- `cnpj_code: str` - Este argumento corresponde ao código do CNPJ.

#### Exemplo de uso

```python
>>> from fordev.validator import cnpj
>>> cnpj('02.104.761/0001-19')
```


### `cpf(...)`

```python
cpf(cpf_code: str, data_only: bool=True) -> bool
```

Verifica se o código do CPF passado é válido.

#### Argumentos

- `cpf_code: str` - Este argumento corresponde ao código do CPF.

#### Exemplo de uso

```python
>>> from fordev.validator import cpf
>>> cpf('140.834.930-20')
```


### `pis_pasep(...)`

```python
pis_pasep(pis_pasep_code: str, data_only: bool=True) -> bool
```

Verifica se o código do PIS/PASEP passado é válido.

#### Argumentos

- `pis_pasep_code: str` - Este argumento corresponde ao código do PIS/PASEP.

#### Exemplo de uso

```python
>>> from fordev.validator import pis_pasep
>>> pis_pasep('891.29467.46-6')
```


### `renavam(...)`

```python
renavam(renavam_code: str, data_only: bool=True) -> bool
```

Verifica se o código do RENAVAM passado é válido.

#### Argumentos

- `renavam_code: str` - Este argumento corresponde ao código da RENAVAM.

#### Exemplo de uso

```python
>>> from fordev.validator import renavam
>>> renavam('36017811164')
```


### `rg(...)`

```python
rg(rg_code: str, data_only: bool=True) -> bool
```

Verifica se o código do RG passado é válido.

#### Argumentos

- `rg_code: str` - Este argumento corresponde ao código do RG.

#### Exemplo de uso

```python
>>> from fordev.validator import rg
>>> rg('14.278.923-9')
```


### `voter_title(...)`

```python
voter_title(voter_title_code: str, data_only: bool=True) -> bool
```

Verifica se o código do Título de Eleitor passado é válido.

#### Argumentos

- `voter_title_code: str` - Este argumento corresponde ao código do título de eleitor.

#### Exemplo de uso

```python
>>> from fordev.validator import voter_title
>>> voter_title('172335860183')
```


### `state_registration(...)`

```python
state_registration(state: str, state_registration_code: str, data_only: bool=True) -> bool
```

Verifica se o código da Inscrição Estadual passado é válido.

#### Argumentos

- `state_registration_code: str` - Este argumento corresponde ao código da inscrição estadual.

#### Exemplo de uso

```python
>>> from fordev.validator import state_registration
>>> state_registration('SP', '174.749.664.188')
```

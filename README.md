<p align="center">
    <img src="https://raw.githubusercontent.com/matheusfelipeog/fordev/master/.github/assets/images/fordev.png" alt="Fordev - Gere e Valide Dados Randômicos" width="400px" />
</p>

<p align="center">
    <sup>Metadata</sup>
    <br />
    <a href="https://pypi.org/project/fordev/">
        <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/fordev" />
    </a>
    <a href="https://github.com/matheusfelipeog/fordev/blob/master/LICENSE">
        <img alt="License MIT" src="https://img.shields.io/github/license/matheusfelipeog/fordev" />
    </a>
    <a href="https://pepy.tech/project/fordev">
        <img alt="Total Downloads" src="https://pepy.tech/badge/fordev" />
    </a>
</p>

<p align="center">
    <sup>Status</sup>
    <br />
    <a href="https://pypi.org/project/fordev/">
        <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/fordev" />
    </a>
    <a href="https://fordev.readthedocs.io/pt_BR/latest/?badge=latest">
        <img alt="Documentation Status" src="https://readthedocs.org/projects/fordev/badge/?version=latest" />
    </a>
    <a href="https://github.com/matheusfelipeog/fordev/actions/workflows/tests.yml">
        <img alt="Test Status" src="https://github.com/matheusfelipeog/fordev/workflows/Tests/badge.svg" />
    </a>
</p>


## Index

- [O objetivo](#o-objetivo)
- [Instalação](#instalação)
- [Demo](#demo)
- [Documentação Oficial](https://fordev.readthedocs.io/)
- [Funcionalidades](#funcionalidades)
   - [fordev.generators](#fordevgenerators)
   - [fordev.validators](#fordevvalidators)
- [Contribuições](#contribuições)
- [Aviso Legal](#aviso-legal)
- [Licença](#licença)


## O objetivo

O site [4Devs](https://4devs.com.br) disponibiliza diversas funcionalidades muito úteis para um desenvolvedor utilizar em seus projetos que necessitam de dados randômicos válidos e outras peculiaridades, tais como: dados dos principais documentos pessoais do brasil (CPF, CNPJ, CNH etc), dados bancários, dados de cartões de crédito, dados completos de pessoas (nome, idade, documentos, endereço etc) e muitos outros geradores de dados. Porém, até o momento, não possui uma interface/API pública para utiliza-los diretamente no código da aplicação em desenvolvimento, assim, sendo necessário ir buscar tais dados diretamente no site.

**Fordev** foi construído para resolver esse problema, disponibilizando um módulo de fácil uso que mapeia todo o site 4Devs usando técnicas de scraping, de modo que seja possível obter todos recursos disponíveis no site em um módulo Python.


## Instalação

Para instalar, certifique-se de que tenha [Python](https://www.python.org/) e o gerenciador de pacotes `pip` instalados em seu ambiente.

Instale com `pip`:

```bash
$ pip install fordev
```

> OBS: fordev precisa de acesso a internet para funcionar corretamente, certifique-se de que também a tenha


## Demo

Socilitando dados randômicos de uma pessoa do sexo *masculino*, de *25 anos de idade* e que *mora em SP*.

```python
>>> from fordev.generators import people
>>> people(sex='M', age=25, state='SP')
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

Confira a seção de [funcionalidades](#funcionalidades) para ver todas as funções atualmente disponíveis no módulo **fordev**.


## Funcionalidades

Todas as funcionalidades disponíveis e que foram mapeadas no site 4Devs estão listados na tabela abaixo.

| Função | Tem gerador? | Tem validador? |
| :----: | :----------: | :------------: |
| **certificate**        | ✔ | ✔ |
| **cnh**                | ✔ | ✔ |
| **bank_account**       | ✔ | ✔ |
| **pis_pasep**          | ✔ | ✔ |
| **renavam**            | ✔ | ✔ |
| **vehicle**            | ✔ | ❌ |
| **vehicle_brand**      | ✔ | ❌ |
| **vehicle_plate**      | ✔ | ❌ |
| **cnpj**               | ✔ | ✔ |
| **rg**                 | ✔ | ❌ |
| **state_registration** | ✔ | ✔ |
| **voter_title**        | ✔ | ✔ |
| **credit_card**        | ✔ | ✔ |
| **people**             | ✔ | ❌ |
| **company**            | ✔ | ❌ |
| **uf**                 | ✔ | ❌ |
| **city**               | ✔ | ❌ |

Confira a [Documentação Oficial](https://fordev.readthedocs.io/) para mais detalhes.


## Contribuições

Toda contribuição é super bem-vinda!

Abaixo mostro com o que você pode contribuir:

- Encontrou algum bug, quer propor uma nova funcionalidade ou conversar sobre o projeto? [Abra uma Issue](https://github.com/matheusfelipeog/fordev/issues) e descreve seu caso.

- Existe uma issue aberta e você quer resolve-la, quer implementar uma nova funcionalidade ou melhorar a documentação? Faça suas adições e me envie um *Pull Request*

- Gostou do projeto, mas não quer ou ainda não consegue contribuir com ele? Considere deixar uma estrela ⭐ para o **Fordev**

Obrigado pelo interesse em colaborar de alguma forma com o projeto 😄


## Aviso Legal

Todo os dados são gerados de forma randômica, respeitando as regras de criação de cada tipo de dado. 

Todo os dados gerados são para fins informativos e utilizados para auxiliar estudantes, programadores, analistas e testadores no desenvolvimento de softwares que necessitem de tais dados. Não devem ser considerados completos, atualizados, e não se destinam a ser utilizado no lugar de uma consulta jurídica, médica, financeira, ou de qualquer outro profissional. Todo e qualquer risco da utilização dos dados disponibilizados atráves do módulo **Fordev** é assumido pelo próprio usuário.

O aviso acima é uma adaptação para utilização no repositório, confira os termos de uso oficial do site 4Devs em: [Termos de Uso](https://www.4devs.com.br/termos_de_uso)


## Licença

**Fordev** utiliza a *licença MIT* em todo seu código, confira suas condições em [MIT License](https://github.com/matheusfelipeog/fordev/blob/master/LICENSE).

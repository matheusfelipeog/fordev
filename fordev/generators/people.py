"""
fordev.generators.people
------------------------
"""

from json import loads as json_loads

from fordev.core import fordev_request

from fordev.validators.utils import raise_for_invalid_uf


def people(
        n: int=1,
        sex: str='R',
        age: int=0,
        uf_code: str='',
        formatting: bool=True,
        data_only: bool=True
    ) -> str:
    """Gere dados de pessoa(s) aleatório(s)

    Parameters
    ----------
    n
        O número de pessoas a ter dados gerados. O mínimo é 1 e o máximo é 30.

    sex
        Uma string representando o sexo da pessoa para geração dos dados.

        Consulte a doc para verificar as opções suportadas:
        https://fordev.rtfd.io/pt_BR/latest/fordev/generators.html

    age
        A idade da pessoa para geração dos dados. A idade mínima é 18 e a máxima é 80.
    """

    sex = sex.upper()

    uf_code = uf_code.upper()

    if not (1 <= n <= 30):
        msg_error = (
            f'The n value "{n}" is invalid. Enter a valid number of people.'
            ' The range is 1 to 30 peoples.'
        )

        raise ValueError(msg_error)

    if sex not in ['M', 'F', 'R']:
        msg_error = (
            f'The sex "{sex}" is invalid. Enter a valid sex.'
            ' Ex: "M" = Male, "F" = Feminine or "R" = Random.'
        )

        raise ValueError(msg_error)

    if not (18 <= age <= 80) and age != 0:
        msg_error = (
            f'The age "{age}" is invalid. Enter a valid age.'
            ' The range is 18 to 80 age.'
        )

        raise ValueError(msg_error)

    raise_for_invalid_uf(uf=uf_code, include_blank=True)

    resp = fordev_request(
        content_length=99,
        referer='gerador_de_pessoas',
        payload={
            'acao': 'gerar_pessoa',
            'sexo': 'H' if sex == 'M' else 'M' if sex == 'F' else 'I',
            'pontuacao': 'S' if formatting else 'N',
            'idade': age,
            'cep_estado': uf_code,
            'txt_qtde': n,
            'cep_cidade': 'Selecione o estado!' if uf_code == '' else ''
        }
    )

    if data_only and resp['msg'] == 'success':
        return json_loads(resp['data'])

    if resp['msg'] == 'success':

        resp['data'] = json_loads(resp['data'])

        return resp

    return resp

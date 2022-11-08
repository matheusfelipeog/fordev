"""
fordev.generators.vehicle
-------------------------
"""

from random import sample as random_sample

from fordev.core import fordev_request

from fordev.consts import ALL_VEHICLE_BRANDS

from fordev.validators.utils import raise_for_invalid_uf

from fordev.filters import filter_vehicle_info
from fordev.filters import data_format


def vehicle(
        brand_code: int=0,
        uf_code: str='',
        formatting: bool=True,
        data_only: bool=True
    ) -> dict:
    """Gere dados de veículo aleatório.

    Parameters
    ----------
    brand
        Recebe um valor númerico de 0 a 87 que representa a marca do carro para
        geração dos dados aleatórios.

        Consulte a doc para verificar as opções suportadas:
        https://fordev.rtfd.io/pt_BR/latest/fordev/generators.html
    """

    if not (0 <= brand_code <= 87):
        msg_error = (
            f'The vehicle brand code value "{brand_code}" is invalid.'
            ' Enter a valid vehicle brand code.'
            ' The range is 0 to 87.'
        )

        raise ValueError(msg_error)

    if brand_code != 0:
        brand_code = ALL_VEHICLE_BRANDS[brand_code]['code']
    else:
        brand_code = ''

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code, include_blank=True)

    resp = fordev_request(
        content_length=62,
        referer='gerador_de_veiculos',
        payload={
            'acao': 'gerar_veiculo',
            'pontuacao': 'S' if formatting else 'N',
            'estado': uf_code,
            'fipe_codigo_marca': brand_code
        }
    )

    resp['data'] = filter_vehicle_info(resp['data'])

    return data_format(data_only=data_only, data_dict=resp)


def vehicle_brand(n: int=1, data_only: bool=True) -> list:
    """Obtenha o nome de marca(s) de veículo(s).

    Parameters
    ----------
    n
        Recebe o número de marcas de veículos a ser gerado. O valor mínimo é 1 e o máximo é 87.
    """

    if not (1 <= n <= 87):
        msg_error = (
            f'The n value "{n}" is invalid. Enter a valid number of UF.'
            ' The range is 1 to 27 UF code.'
        )

        raise ValueError(msg_error)

    full_data = {
        'msg': 'success',
        'data': random_sample(
            [v_brand['brand_name'] for v_brand in ALL_VEHICLE_BRANDS.values()],
            n
        )
    }

    if data_only:
        return full_data['data']
    else:
        return full_data


def vehicle_plate(uf_code: str='', formatting: bool=True, data_only: bool=True) -> str:
    """Gere o código da placa de veículo aleatório."""

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code, include_blank=True)

    resp = fordev_request(
        content_length=36 if uf_code == '' else 38,
        referer='gerador_de_placa_automoveis',
        payload={
            'acao': 'gerar_placa',
            'pontuacao': 'S' if formatting else 'N',
            'estado':uf_code
        }
    )

    return data_format(data_only=data_only, data_dict=resp)

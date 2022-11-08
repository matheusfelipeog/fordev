"""
fordev.validators.state_registration
------------------------------------
"""

from fordev.core import fordev_request

from fordev.filters import data_format

from fordev.validators.utils import _data_verification_and_normalize
from fordev.validators.utils import raise_for_invalid_uf


def is_valid_state_registration(
        uf_code: str,
        state_registration_code: str,
        data_only: bool=True
    ) -> bool:
    """Verifique se o código do registro estadual é válido.

    Parameters
    ----------
    uf_code
        O código UF(Unidade Federativa) do estado que pertence o registro estadual.

        Mais informações: https://pt.wikipedia.org/wiki/Subdivis%C3%B5es_do_Brasil

    state_registration_code
        O código do registro estadual para verificação.
    """

    uf_code = uf_code.upper()

    raise_for_invalid_uf(uf=uf_code)

    resp = _data_verification_and_normalize(
        fordev_request(
            content_length=48,
            referer='validar_inscricao_estadual',
            payload={
                'acao': 'validar_ie',
                'txt_ie': state_registration_code,
                'estado': uf_code
            }
        )
    )

    return data_format(data_only=data_only, data_dict=resp)

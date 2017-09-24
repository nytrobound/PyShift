import requests

import constants
from helpers import requests_error, response_to_dict


@requests_error
def signatures_get(shift_id):
    payload = {'id': shift_id}
    response = requests.get(constants.SIGNATURES_GET,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def signatures_add_second(secret, secondSecret, publicKey):
    payload = {
        'secret': secret,
        'secondSecret': secondSecret,
        'publicKey': publicKey
    }
    response = requests.put(constants.SIGNATURES_ADD_SECOND,
                            data=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)

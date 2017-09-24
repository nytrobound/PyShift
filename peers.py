import requests

import constants
from helpers import requests_error, response_to_dict


@requests_error
def peers_list(**kwargs):
    PARAMS = [
        'state',
        'os',
        'version',
        'limit',
        'offset',
        'orderBy'
    ]
    payload = {}
    for name in kwargs:
        if name not in PARAMS:
            raise ValueError("%s is not a valid parameter." % name)
        payload[name] = kwargs[name]

    response = requests.get(constants.PEERS_LIST,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def peers_get(ip, port):
    payload = {
        'ip': ip,
        'port': port
    }
    response = requests.get(constants.PEERS_GET,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def peers_get_version():
    response = requests.get(constants.PEERS_GET_VERSION,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)

import requests

import constants
from helpers import requests_error, response_to_dict


@requests_error
def accounts_open(secret):
    payload = {'secret': secret}
    response = requests.post(constants.ACCOUNTS_OPEN,
                             data=payload,
                             timeout=constants.TIMEOUT
                             )
    return response_to_dict(response)


@requests_error
def accounts_get_balance(address):
    payload = {'address': address}
    response = requests.get(constants.ACCOUNTS_GET_BALANCE,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def accounts_get_publickey(address):
    payload = {'address': address}
    response = requests.get(constants.ACCOUNTS_GET_PUBLICKEY,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def accounts_gen_publickey(secret):
    payload = {'secret': secret}
    response = requests.post(constants.ACCOUNTS_GEN_PUBLICKEY,
                             data=payload,
                             timeout=constants.TIMEOUT
                             )
    return response_to_dict(response)


@requests_error
def accounts_get(address):
    payload = {'address': address}
    response = requests.get(constants.ACCOUNTS_GET,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def accounts_get_delegates(address):
    payload = {'address': address}
    response = requests.get(constants.ACCOUNTS_GET_DELEGATES,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def accounts_put_delegates(secret, delegates, **kwargs):
    PARAMS = [
        'secret',
        'publicKey',
        'secondSecret',
        'delegates'
    ]
    if len(delegates) > 33:
        raise ValueError("You are only allowed to vote for 33 delegates at once. You have voted for:", len(delegates))

    payload = {
        'secret': secret,
        'delegates': delegates
    }

    for name in kwargs:
        if name not in PARAMS:
            raise ValueError("%s is not a valid parameter." % name)
        payload[name] = kwargs[name]

    response = requests.put(constants.ACCOUNTS_PUT_DELEGATES,
                            data=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)

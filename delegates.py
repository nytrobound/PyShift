import requests

import constants
from helpers import requests_error, response_to_dict


@requests_error
def delegates_create(secret, secondSecret, username):
    if len(username) > 20:
        print(username, "is too long. Please us a string from 1 to 20 characters")
    payload = {
        'secret': secret,
        'secondSecret': secondSecret,
        'username': username
    }
    response = requests.put(constants.DELEGATES_CREATE,
                            data=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def delegates_list(**kwargs):
    PARAMS = [
        'limit',
        'offset',
        'orderBy'
    ]

    payload = {}

    for name in kwargs:
        if name not in PARAMS:
            raise ValueError("%s is not a valid parameter." % name)
        payload[name] = kwargs[name]

    response = requests.get(constants.DELEGATES_LIST,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def delegates_get(**kwargs):
    if 'publicKey' in kwargs:
        payload = {'publicKey': kwargs['publicKey']}
    elif 'username' in kwargs:
        payload = {'username': kwargs['username']}
    else:
        raise ValueError("Invalid parameter.")

    response = requests.get(constants.DELEGATES_GET,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def delegates_count():
    response = requests.get(constants.DELEGATES_COUNT,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def delegates_get_votes(address):
    payload = {'address': address}
    response = requests.get(constants.DELEGATES_GET_VOTES,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def delegates_get_votes(publicKey):
    payload = {'publicKey': publicKey}
    response = requests.get(constants.DELEGATES_GET_VOTERS,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def delegates_enable_forging(secret):
    payload = {'secret': secret}
    response = requests.post(constants.DELEGATES_ENABLE_FORGING,
                             data=payload,
                             timeout=constants.TIMEOUT
                             )
    return response_to_dict(response)


@requests_error
def delegates_disable_forging(secret):
    payload = {'secret': secret}
    response = requests.post(constants.DELEGATES_DISABLE_FORGING,
                             data=payload,
                             timeout=constants.TIMEOUT
                             )
    return response_to_dict(response)


@requests_error
def delegates_get_forged(generatorPublicKey, **kwargs):
    PARAMS = [
        'start',
        'end'
    ]
    payload = {'generatorPublicKey': generatorPublicKey}

    for name in kwargs:
        if name not in PARAMS:
            raise ValueError("%s is not a valid parameter." % name)
        payload[name] = kwargs[name]

    response = requests.get(constants.DELEGATES_GET_FORGED,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)

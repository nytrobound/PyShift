import requests

import constants
from helpers import requests_error, response_to_dict


@requests_error
def transactions_list(**kwargs):
    PARAMS = [
        'blockId',
        'senderId',
        'recipientId',
        'limit',
        'offset',
        'orderBy'
    ]
    payload = {}
    for name in kwargs:
        if name not in PARAMS:
            raise ValueError("%s is not a valid parameter." % name)
        payload[name] = kwargs[name]

    response = requests.get(constants.TRANSACTIONS_LIST,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def transactions_send(secret, amount, recipientId, publicKey, **kwargs):
    PARAMS = [
        'secondSecret'
    ]
    payload = {
        'secret': secret,
        'amount': amount,
        'recipientId': recipientId,
        'publicKey': publicKey
    }

    for name in kwargs:
        if name not in PARAMS:
            raise ValueError("%s is not a valid parameter." % name)
        payload[name] = kwargs[name]

    response = requests.put(constants.TRANSACTIONS_SEND,
                            data=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def transactions_get(shift_id):
    payload = {'id': shift_id}
    response = requests.get(constants.TRANSACTIONS_GET,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def transactions_unconf_get(shift_id):
    payload = {'id': shift_id}
    response = requests.get(constants.TRANSACTIONS_UNCONFIRMED_GET,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def transactions_unconf_list():
    response = requests.get(constants.TRANSACTIONS_UNCONFIRMED_LIST,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)

import requests

import constants
from helpers import requests_error, response_to_dict


@requests_error
def msignatures_pending(publicKey):
    payload = {'id': publicKey}
    response = requests.get(constants.MULTI_SIGNATURE_PENDING,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def msignatures_create(secret, lifetime, min_sig, keysgroup):
    payload = {
        'secret': secret,
        'lifetime': lifetime,
        'min': min_sig,
        'keysgroup': keysgroup
    }
    response = requests.put(constants.MULTI_SIGNATURE_CREATE_ACCOUNT,
                            data=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def msignatures_sign(secret, transactionId, **kwargs):
    PARAMS = ['publicKey']
    payload = {
        'secret': secret,
        'transactionId': transactionId
    }

    for name in kwargs:
        if name not in PARAMS:
            raise ValueError("%s is not a valid parameter." % name)
        payload[name] = kwargs[name]

    response = requests.post(constants.MULTI_SIGNATURE_SIGN,
                             data=payload,
                             timeout=constants.TIMEOUT
                             )
    return response_to_dict(response)


@requests_error
def msignatures_get(publicKey):
    payload = {'publicKey': publicKey}
    response = requests.get(constants.MULTI_SIGNATURE_ACCOUNTS,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)

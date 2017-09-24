import requests

import constants
from helpers import requests_error, response_to_dict


@requests_error
def blocks_get_one(shift_id):
    payload = {'id': shift_id}
    response = requests.get(constants.BLOCKS_GET_ONE,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def blocks_get_filter(**kwargs):
    PARAMS = [
        'totalFee',
        'totalAmount',
        'previousBlock',
        'height',
        'generatorPublickey',
        'offset',
        'limit',
        'orderBy'
    ]

    payload = {}

    for name in kwargs:
        if name not in PARAMS:
            raise ValueError("%s is not a valid parameter." % name)
        payload[name] = kwargs[name]

    response = requests.get(constants.BLOCKS_GET_FILTER,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def blocks_get_fee():
    response = requests.get(constants.BLOCKS_GET_FEE,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def blocks_get_fees():
    response = requests.get(constants.BLOCKS_GET_FEES,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def blocks_get_supply():
    response = requests.get(constants.BLOCKS_GET_SUPPLY,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def blocks_get_height():
    response = requests.get(constants.BLOCKS_GET_HEIGHT,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def blocks_get_status():
    response = requests.get(constants.BLOCKS_GET_STATUS,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def blocks_get_nethash():
    response = requests.get(constants.BLOCKS_GET_NETHASH,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def blocks_get_milestone():
    response = requests.get(constants.BLOCKS_GET_MILESTONE,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)

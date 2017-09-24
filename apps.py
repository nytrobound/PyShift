import requests

import constants
from helpers import requests_error, response_to_dict


@requests_error
def apps_register(secret, category, app_name, app_type, link, **kwargs):
    PARAMS = [
        'secret',
        'secondSecret',
        'publicKey',
        'category',
        'name',
        'description',
        'tags',
        'type',
        'link',
        'icon'
    ]
    payload = {
        'secret': secret,
        'category': category,
        'name': app_name,
        'type': app_type,
        'link': link
    }

    for name in kwargs:
        if name not in PARAMS:
            raise ValueError("%s is not a valid parameter." % name)
        payload[name] = kwargs[name]

    response = requests.put(constants.APPS_REGISTER,
                            data=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def apps_get_registered(**kwargs):
    PARAMS = [
        'category',
        'name',
        'type',
        'link',
        'limit',
        'offset',
        'orderBy'
    ]
    payload = {}

    for name in kwargs:
        if name not in PARAMS:
            raise ValueError("%s is not a valid parameter." % name)
        payload[name] = kwargs[name]

    response = requests.get(constants.APPS_GET_REGISTERED,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def apps_get(app_id):
    payload = {'id': app_id}
    response = requests.get(constants.APPS_GET,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def apps_search(**kwargs):
    PARAMS = [
        'q',
        'category',
        'installed'
    ]
    payload = {}

    for name in kwargs:
        if name not in PARAMS:
            raise ValueError("%s is not a valid parameter." % name)
        payload[name] = kwargs[name]

    response = requests.get(constants.APPS_SEARCH,
                            params=payload,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def apps_install(app_id):
    payload = {'id': app_id}
    response = requests.post(constants.APPS_INSTALL,
                             data=payload,
                             timeout=constants.TIMEOUT
                             )
    return response_to_dict(response)


@requests_error
def apps_installed():
    response = requests.get(constants.APPS_INSTALLED,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def apps_installed_ids():
    response = requests.get(constants.APPS_INSTALLED_IDS,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def apps_uninstall(app_id):
    payload = {'id': app_id}
    response = requests.post(constants.APPS_UNINSTALL,
                             data=payload,
                             timeout=constants.TIMEOUT
                             )
    return response_to_dict(response)


@requests_error
def apps_launch(app_id, **kwargs):
    PARAMS = ['params']
    payload = {'id': app_id}

    for name in kwargs:
        if name not in PARAMS:
            raise ValueError("%s is not a valid parameter." % name)
        payload[name] = kwargs[name]

    response = requests.post(constants.APPS_LAUNCH,
                             data=payload,
                             timeout=constants.TIMEOUT
                             )
    return response_to_dict(response)


@requests_error
def apps_installing():
    response = requests.get(constants.APPS_INSTALLING,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def apps_uninstalling():
    response = requests.get(constants.APPS_UNINSTALLING,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def apps_launched():
    response = requests.get(constants.APPS_LAUNCHED,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def apps_categories():
    response = requests.get(constants.APPS_CATEGOREIS,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def apps_installing():
    response = requests.get(constants.APPS_INSTALLING,
                            timeout=constants.TIMEOUT
                            )
    return response_to_dict(response)


@requests_error
def apps_stop(app_id):
    payload = {'id': app_id}
    response = requests.post(constants.APPS_STOP,
                             data=payload,
                             timeout=constants.TIMEOUT
                             )
    return response_to_dict(response)

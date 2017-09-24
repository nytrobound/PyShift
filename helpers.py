import json
import requests


def requests_error(f):
    def requests_problems(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except requests.exceptions.Timeout:
            print("Timeout")
        except requests.exceptions.TooManyRedirects:
            print("Bad URL")
        except requests.exceptions.RequestException as e:
            print(e)
    return requests_problems


def response_to_dict(response):
    return json.loads(response.text)
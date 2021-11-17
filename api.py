import requests
from requests.exceptions import HTTPError

BASE_URL = "http://127.0.0.1:7000"


def user_login_api(*args):
    try:
        login_url = BASE_URL + '/auth/token/login/'
        headers = {
            "Content-Type": "application/json"
        }
        json = {
            "username":args["username"],
            "password":args["password"]
        }
        response = requests.post(login_url, headers=headers, json=json)
        print(f"user_login_api(): response {response.json()} - {response.status_code()}")
        raise response.raise_for_status()

    except HTTPError as http_err:
        print(f'user_login_api(): HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'user_login_api(): Other error occurred: {err}')
    else:
        print(f'user_login_api(): Success!')

import requests
from requests.exceptions import HTTPError
BASE_URL = "http://127.0.0.1:7000"


def user_login_api(**args):
    """
    login api call
    """
    try:
        login_url = BASE_URL + "/auth/token/login"

        response = requests.post(
            login_url,
            headers={"Content-Type": "application/json"},
            json={
                "username": args['username'],
                "password": args['password']
            }
        )

        print(f"user_login_api(): response {response.json()}")

        # If the response was successful, no Exception will be raised
        response.status_code()
    except HTTPError as http_err:
        print(f'user_login_api(): HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'user_login_api(): Other error occurred: {err}')
    else:
        print('user_login_api(): Success!')

    return response


def user_movie_list_api(**args):
    """
    login api call
    """
    try:
        login_url = BASE_URL + "/movie/"

        response = requests.get(
            login_url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"token {args['token']}"
                }
        )

        print(f"user_movie_list_api(): response {response.json()}")

        # If the response was successful, no Exception will be raised
        response.status_code()
    except HTTPError as http_err:
        print(f'user_movie_list_api(): HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'user_movie_list_api(): Other error occurred: {err}')
    else:
        print('user_movie_list_api(): Success!')

    return response

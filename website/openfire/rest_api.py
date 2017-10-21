import requests
from . import settings


def create_new_user(username, password, name="", email=""):
    credentials = {'username': username, 'password': password, 'name': name, 'email': email}

    headers = {
        'Authorization': settings.api_auth_key,
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }

    response = requests.post(settings.create_user_endpoint, json=credentials, headers=headers)
    if response.status_code == 201:
        return True
    else:
        return False


def delete_user(username):
    headers = {
        'Authorization': settings.api_auth_key,
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }

    response = requests.delete(settings.delete_user_endpoint.format(username), headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False

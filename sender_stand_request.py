import configuration
import requests
import data

def post_new_user(body):
    return requests.post (configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                          json = body,
                          headers = data.headers)

def get_new_user_token():
    response = post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    return auth_token

def post_new_client_kit(kit_body, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                        json = kit_body,
                        headers = {"Authorization": "Bearer " + auth_token})

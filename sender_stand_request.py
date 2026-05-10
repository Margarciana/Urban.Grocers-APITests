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

def get_kits_search_by_name(name, auth_token):
    return requests.get(configuration.URL_SERVICE + configuration.KITS_PATH + "/search",
                       params={"name": name},
                       headers={"Authorization": "Bearer " + auth_token})

def get_kits_search_by_products(product_ids, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH + "/search",
                        json={"ids": product_ids},
                        headers={"Authorization": "Bearer " + auth_token})

def get_client_personal_kits(auth_token):
    return requests.get(configuration.URL_SERVICE + configuration.KITS_PATH,
                        headers = {"Authorization": "Bearer " + auth_token})

def put_kit_name(kit_id, body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.put(configuration.URL_SERVICE + configuration.KITS_PATH + "/" + str(kit_id),
                        json=body,
                        headers=headers)

def delete_kit(kit_id, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.delete(configuration.URL_SERVICE + configuration.KITS_PATH + "/" + str(kit_id),
                        headers=headers)

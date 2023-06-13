import random

import pytest
import requests
from Utilities.read_csv_data import read_test_data_from_csv

endpoint = "https://gorest.co.in/public/v2/users/"


# testing web_app used = https://gorest.co.in/

@pytest.mark.parametrize("name, email, gender, status", read_test_data_from_csv())
def test_post_rqst(name, email, gender, status):
    # create user
    print("post rqst")
    print(name)
    payload = {"name": name, "email": email, "gender": gender, "status": status}
    headers = {"content-type": "application/json",
               "Authorization": "Bearer 9c000fb269972e5e6f5874289b44aee494f0b0aab72b3e643f0370aab328ed76"}
    response = requests.post(endpoint, json=payload, headers=headers)
    print(response.status_code)
    print(response.json())
    data = response.json()
    global id_user
    id_user = data['id']
    print(id_user)


def test_get_rqst():
    # get user
    print("get rqst")
    headers = {"content-type": "application/json",
               "Authorization": "Bearer 9c000fb269972e5e6f5874289b44aee494f0b0aab72b3e643f0370aab328ed76"}
    response = requests.get(endpoint + f"{id_user}", headers=headers)
    print(response.status_code)
    print(response.json())


def test_put_rqst():
    # update user
    print("put rqst")
    headers = {"content-type": "application/json",
               "Authorization": "Bearer 9c000fb269972e5e6f5874289b44aee494f0b0aab72b3e643f0370aab328ed76"}
    payload = {
        "gender": "female", "status": "inactive"
    }
    response = requests.put(endpoint + f"{id_user}", json=payload, headers=headers)
    print(response.status_code)
    print(response.json())

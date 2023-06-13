import requests
from Utilities import config_reader

ENDPOINT = config_reader.readConfig("update_task", "url")


def test_update_task_rqst_validation_error():
    payload = {
        "content": "",
        "user_id": "",
        "task_id": "",
        "is_done": ""
    }
    response = requests.put(ENDPOINT, json=payload)
    print(response)
    print(response.json())
    data = response.json()

    # validate status code is 422
    assert response.status_code == 422
    # validate msg should be: value could not be parsed to a boolean
    assert data['detail'][0]['msg'] == "value could not be parsed to a boolean"



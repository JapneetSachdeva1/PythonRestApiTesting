import requests
from Utilities import config_reader

ENDPOINT = config_reader.readConfig("list_tasks", "url")


def test_get_tasks_rqst():
    user_id = "test_user"
    response = requests.get(ENDPOINT + f"{user_id}")
    print(response)
    print(response.json())
    data = response.json()
   # print(str(data['tasks'][0]['user_id']))

    # validate if response code is 200
    assert response.status_code == 200
    # validate if user_id is same in response received
    assert data['tasks'][0]['user_id'] == user_id

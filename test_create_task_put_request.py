import requests
from Utilities import config_reader

ENDPOINT = config_reader.readConfig("create_task", "url")


def test_create_task_rqst():
    #put rqst
    payload = {
        "content": "my test content",
        "user_id": "test_user",
        "is_done": False
    }

    response = requests.put(ENDPOINT, json=payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    print(data['task']['user_id'])
    # task_id = data['task']['task_id']
    # # Check whether a task exits with above task id
    # endpoint = config_reader.readConfig("get_task", "url")
    # get_task_response = requests.get(endpoint+f"{task_id}")
    # print(get_task_response.content)

    # check whether user got updated
    assert data['task']['user_id'] == payload["user_id"]
    # check whether content got updated
    assert data['task']['content'] == payload['content']
    # check whether is_done set to false
    assert data['task']['is_done'] == payload['is_done']
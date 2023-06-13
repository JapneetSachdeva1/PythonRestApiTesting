import requests
from Utilities import config_reader


def create_task():
    endpoint = config_reader.readConfig("create_task", "url")
    global task_id
    payload = {
        "content": "test content 2",
        "user_id": "test_user 2",
        "is_done": False
    }
    response = requests.put(endpoint, json=payload)
    # print(response.json())
    data = response.json()
    print(data)
    task_id = data['task']['task_id']


def get_task():
    endpoint = config_reader.readConfig("get_task", "url")

    response = requests.get(endpoint + f"{task_id}")
    print(response)
    print(response.json())


def delete_task():
    endpoint = config_reader.readConfig("delete_task", "url")
    response = requests.delete(endpoint + f"{task_id}")
    print(response)
    print(response.json())


def test_api_flow():
    print("create task")
    create_task()
    print("get task")
    get_task()
    print("delete task")
    delete_task()

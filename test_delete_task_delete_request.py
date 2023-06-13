import requests
from Utilities import config_reader

ENDPOINT = config_reader.readConfig("update_task", "url")


def test_delete_task_rqst_validation_error():
    task_id = 'sd'
    response = requests.delete(ENDPOINT + f"{task_id}")
    data = response.json()
    # validate status code should be 404
    assert response.status_code == 404
    # validate detail key should have Not Found
    assert data['detail'] == 'Not Found'

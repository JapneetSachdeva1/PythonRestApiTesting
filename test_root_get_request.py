import requests
from Utilities import config_reader

ENDPOINT = config_reader.readConfig("endpoint", "url")


def test_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200  # test status code
    all_headers = response.headers
    content_type = all_headers["Content-Type"]
    assert content_type == "application/json"  # test content_type of response received
    data = response.json()
    response_msg = data["message"]
    assert response_msg == config_reader.readConfig("root", "root_rqst_response")  # test response msg received

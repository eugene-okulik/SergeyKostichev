import requests

url = 'http://167.172.172.115:52353/'


def test_get_object(response):
    template = f'{url}/object/{response.json()["id"]}'
    response = requests.get(template)
    assert response.status_code == 200, "Page didn't answer"
    assert len(response.json()) == 3, "Page structure is correct"

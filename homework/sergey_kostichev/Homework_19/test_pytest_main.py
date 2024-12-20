import pytest
import requests
from faker import Faker

url = 'http://167.172.172.115:52353/'


@pytest.fixture(scope='session', autouse=True)
def start_and_finish_testing():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(autouse=True)
def pre_and_post_condition():
    print('before test')
    yield
    print('after test')


@pytest.fixture(scope="session")
def header():
    return {"Content-Type": "application/json"}


@pytest.fixture
def response(header):
    fake = Faker()
    template = f'{url}/object'
    body = {"name": 'Thing', "data": {"color": fake.color_name(), "size": "small"}}
    response = requests.post(template, json=body, headers=header)
    # Возвращаю весь response, потому что мне нужно иметь доступ не только к айди
    yield response
    template = f"{url}/object/{response.json()['id']}"
    requests.delete(template)


def test_get_object(response):
    template = f'{url}/object/{response.json()["id"]}'
    response = requests.get(template)
    assert response.status_code == 200, "Page didn't answer"
    assert len(response.json()) == 3, "Page structure is correct"


@pytest.mark.critical
@pytest.mark.parametrize('object_data', [
    {'name': 'Thing1', 'data': {'color': 'black', 'size': 'XXL'}},
    {'name': 'Thing2', 'data': {'color': 'blue', 'size': 'A2'}},
    {'name': 'Thing3', 'data': {'color': 'white', 'size': 'small'}}])
def test_post_object(object_data, header):
    template = f'{url}/object'
    old_length = len(requests.get(template).json()["data"])
    body = object_data
    response = requests.post(template, json=body, headers=header)
    assert response.status_code == 200, "Object was not created"

    new_length = len(requests.get(template).json()["data"])
    assert old_length + 1 == new_length, "Object was not added"


@pytest.mark.medium
def test_put_object(response, header):
    template = f'{url}/object/{response.json()["id"]}'
    body = {"name": "T-shirt", "data": {"color": "green", "size": "M"}}
    response = requests.put(template, json=body, headers=header)
    assert response.status_code == 200, "Datas were not updated"
    assert len(response.json()) == 3, "Not all datas were saved"


def test_patch_object(response, header):
    fake = Faker()
    color_name = fake.color_name()
    template = f'{url}/object/{response.json()["id"]}'
    body = {"data": {"color": color_name}}
    response = requests.patch(template, json=body, headers=header)
    assert response.status_code == 200, "Not all datas were saved"
    assert response.json()["data"]["color"] == color_name, "There is wrong data"


def test_delete_object(response):
    old_length = len(requests.get(url + '/object').json()["data"])
    template = f'{url}/object/{response.json()["id"]}'
    response = requests.delete(template)
    # Почему не было ошибки на повторное удаление, я же после этого теста в фикстуре тоже удаляю
    assert response.status_code == 200, "Post was not deleted"

    new_length = len(requests.get(url + '/object').json()["data"])
    assert old_length - 1 == new_length, "Object was not deleted"

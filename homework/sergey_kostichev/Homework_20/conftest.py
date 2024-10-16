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

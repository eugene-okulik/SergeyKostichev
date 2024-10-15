import pytest
import requests

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



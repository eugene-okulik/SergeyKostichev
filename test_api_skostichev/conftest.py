import pytest
from test_api_skostichev.endpoints.delete_object import DeleteObject
from test_api_skostichev.endpoints.get_object import GetObject
from test_api_skostichev.endpoints.create_object import CreateObject
from test_api_skostichev.endpoints.update_object import UpdateObject


@pytest.fixture()
def create_post_endpoint():
    return CreateObject()


@pytest.fixture()
def create_test_response():
    test_object = CreateObject()
    test_response = test_object.create_new_object()
    yield test_response
    test_object.delete_object(test_response.json()["id"])


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def create_delete_endpoint():
    return DeleteObject()


@pytest.fixture()
def create_get_endpoint():
    return GetObject()

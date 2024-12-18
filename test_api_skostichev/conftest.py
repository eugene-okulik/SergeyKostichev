import pytest
from test_api_skostichev.endpoints.delete_object import DeleteObject
from test_api_skostichev.endpoints.get_object import GetObject
from test_api_skostichev.endpoints.create_object import CreateObject
from test_api_skostichev.endpoints.full_update_object import FullUpdateObject
from test_api_skostichev.endpoints.part_update_object import PartUpdateObject


@pytest.fixture(scope="session")
def create_post_endpoint():
    return CreateObject()


@pytest.fixture()
def create_test_response(create_post_endpoint, delete_endpoint):
    test_response = create_post_endpoint.create_new_object()
    yield test_response
    delete_endpoint.delete_object(test_response)


@pytest.fixture(scope="session")
def full_update_object_endpoint():
    return FullUpdateObject()


@pytest.fixture(scope="session")
def part_update_object_endpoint():
    return PartUpdateObject()


@pytest.fixture(scope="session")
def delete_endpoint():
    return DeleteObject()


@pytest.fixture(scope="session")
def create_get_endpoint():
    return GetObject()

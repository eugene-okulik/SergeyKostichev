import pytest
from test_api_skostichev.endpoints.delete_method import DELETEMethod
from test_api_skostichev.endpoints.get_method import GETMethod
from test_api_skostichev.endpoints.patch_method import PATCHMethod
from test_api_skostichev.endpoints.post_method import POSTMethod
from test_api_skostichev.endpoints.put_method import PUTMethod


@pytest.fixture()
def create_post_endpoint():
    return POSTMethod()


@pytest.fixture()
def create_test_response():
    test_object = POSTMethod()
    test_response = test_object.create_new_object()
    yield test_response
    test_object.delete_object(test_response.json()["id"])


@pytest.fixture()
def create_put_endpoint():
    return PUTMethod()


@pytest.fixture()
def create_patch_endpoint():
    return PATCHMethod()


@pytest.fixture()
def create_delete_endpoint():
    return DELETEMethod()


@pytest.fixture()
def create_get_endpoint():
    return GETMethod()

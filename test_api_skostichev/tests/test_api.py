import pytest
import allure


TEST_DATA = [
    {"name": "Pencil", "data": {"color": "transparent", "size": "XXL"}},
    {"name": "Notebook", "data": {"color": "blue", "size": "A4"}},
    {"name": "Eraser", "data": {"color": "white", "size": "small"}}
]

NEGATIVE_DATA = [
    {"name": None, "data": {"color": "transparent", "size": "XXL"}},
    {"data": {"color": None, "size": "XXL"}},
    {"name": "Pencil"}
]

EXPECTED_KEYS = ['id', 'name', 'data']


@allure.feature('Create Object')
@pytest.mark.parametrize('data', TEST_DATA)
@allure.story('Valid Object Creation')
@allure.title('Test POST object creation with valid data')
def test_post_object(create_post_endpoint, data):
    create_post_endpoint.create_new_object(data=data)
    create_post_endpoint.check_success()
    create_post_endpoint.check_response_name_is_correct(data)
    create_post_endpoint.check_response_structure(EXPECTED_KEYS)
    create_post_endpoint.check_specific_parameter('name', data['name'])
    create_post_endpoint.check_response_time(max_time=2)
    create_post_endpoint.delete_object(create_post_endpoint.response)


@allure.feature('Create Object')
@pytest.mark.parametrize('data', NEGATIVE_DATA)
@allure.story('Invalid Object Creation')
@allure.title('Test POST object creation with negative data')
def test_post_with_negative_data(create_post_endpoint, data):
    create_post_endpoint.check_status_request_400(data=data)
    create_post_endpoint.delete_object(create_post_endpoint.response)


@allure.feature('Update Object')
@pytest.mark.parametrize('data', TEST_DATA)
@allure.story('Valid Object Update')
@allure.title('Test PUT object update with valid data')
def test_put_object(create_test_response, create_put_endpoint, data):
    create_put_endpoint.change_object(create_test_response, data=data)
    create_put_endpoint.check_success()
    create_put_endpoint.check_response_name_is_correct(data)
    create_put_endpoint.check_response_structure(EXPECTED_KEYS)
    create_put_endpoint.check_specific_parameter('name', data['name'])
    create_put_endpoint.check_response_time(max_time=2)


@allure.feature('Update Object')
@pytest.mark.parametrize('data', NEGATIVE_DATA)
@allure.story('Invalid Object Update')
@allure.title('Test PUT object update with negative data')
def test_put_object_with_negative_data(create_test_response, create_put_endpoint, data):
    create_put_endpoint.check_negative_data(data)


@allure.feature('Update Object')
@pytest.mark.parametrize('data', TEST_DATA)
@allure.story('Valid Object Partial Update')
@allure.title('Test PATCH object update with valid data')
def test_patch_object(create_test_response, create_patch_endpoint, data):
    create_patch_endpoint.change_object(create_test_response, data=data)
    create_patch_endpoint.check_success()
    create_patch_endpoint.check_response_name_is_correct(data)
    create_patch_endpoint.check_response_structure(EXPECTED_KEYS)
    create_patch_endpoint.check_specific_parameter('name', data['name'])
    create_patch_endpoint.check_response_time(max_time=2)


@allure.feature('Update Object')
@pytest.mark.parametrize('data', NEGATIVE_DATA)
@allure.story('Invalid Object Partial Update')
@allure.title('Test PATCH object update with negative data')
def test_patch_with_negative_data(create_test_response, create_patch_endpoint, data):
    create_patch_endpoint.change_object(create_test_response, data=data)
    create_patch_endpoint.check_negative_data(data)


@allure.feature('Delete Object')
@allure.title('Test DELETE object')
def test_delete_object(create_test_response, create_delete_endpoint):
    create_delete_endpoint.delete_object(create_test_response)
    create_delete_endpoint.check_success()
    create_delete_endpoint.verify_object_deleted(create_test_response)


@allure.feature('Delete Object')
@allure.title('Test DELETE non-existent object')
def test_delete_non_existent_object(create_delete_endpoint):
    fake_id = 999999
    create_delete_endpoint.check_delete_non_existent_object(fake_id)


@allure.feature('Retrieve Object')
@pytest.mark.parametrize("test_object", ["valid", "non_existent"])
@allure.story('Valid and Invalid Object Retrieval')
@allure.title('Test GET object with valid and non-existent IDs')
def test_get_valid_object(create_test_response, create_get_endpoint, test_object):
    if test_object == "valid":
        create_get_endpoint.get_object(create_test_response)
        create_get_endpoint.check_success()
        expected_data = create_test_response.json()
        create_get_endpoint.check_response_values(expected_data)
        create_get_endpoint.check_response_structure(EXPECTED_KEYS)
        create_get_endpoint.check_response_time(max_time=2)
    else:
        none_id = 999999
        create_get_endpoint.check_not_found(none_id)


@allure.feature('Retrieve Object')
@allure.title('Test GET non-existent object')
def test_get_nonexistent_object(create_get_endpoint):
    none_id = 999999
    create_get_endpoint.check_not_found(none_id)

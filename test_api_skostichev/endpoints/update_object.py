import allure
import requests
from test_api_skostichev.endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):

    @allure.step('Change test object with PUT method')
    def put_object(self, test_object, data, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/object/{test_object.json()["id"]}', json=data, headers=headers)
        self.response_json = self.response.json()
        return self.response

    @allure.step('Create a new object with PATCH method')
    def patch_object(self, test_object, data, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(f'{self.url}/object/{test_object.json()["id"]}', json=data, headers=headers)
        self.response_json = self.response.json()
        return self.response

    @allure.step('Check success status code for PUT/PATCH')
    def check_success(self):
        assert self.response.status_code in [200, 204], f"Unexpected status code: {self.response.status_code}"

    @allure.step('Check parameter values in the new object')
    def check_response_name_is_correct(self, data):
        for key, value in data.items():
            assert self.response.json()[key] == value, f"Parameter value is wrong: {value}"

    @allure.step('Check response structure')
    def check_response_structure(self, expected_keys):
        response_json = self.response.json()
        for key in expected_keys:
            assert key in response_json, f"Parameter '{key}' not found in response"

    @allure.step('Check specific parameter value')
    def check_specific_parameter(self, key, expected_value):
        assert self.response.json()[key] == expected_value, \
            f"Parameter '{key}' is not '{self.response_json[key]}'"

    @allure.step('Check response time')
    def check_response_time(self, max_time):
        assert self.response.elapsed.total_seconds() < max_time, \
            f"Response took too long: {self.response.elapsed.total_seconds()} seconds"

    @allure.step('Check 405 status code for invalid PUT/PATCH')
    def check_negative_data(self, data=None, headers=None, method='PUT'):
        headers = headers if headers else self.headers
        data = data if data else self.default_data
        url = f"{self.url}/object"

        if method == 'PUT':
            self.response = requests.put(url, json=data, headers=headers)
        else:
            self.response = requests.patch(url, json=data, headers=headers)

        assert self.response.status_code == 405, f"Unexpected status code: {self.response.status_code}"

    @allure.step("Deleting object")
    def delete_object(self, object_id):
        requests.delete(f"{self.url}/object/{object_id}")

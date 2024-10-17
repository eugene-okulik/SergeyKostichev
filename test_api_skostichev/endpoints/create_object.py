import requests
import allure
from test_api_skostichev.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    @allure.step('Create a new object with POST method')
    def create_new_object(self, data=None, headers=None):
        headers = headers if headers else self.headers
        data = data if data else self.default_data
        self.response = requests.post(f"{self.url}/object", json=data, headers=headers)
        self.response_json = self.response.json()
        return self.response

    @allure.step('Check parameter values in the new object')
    def check_response_name_is_correct(self, data):
        for parameter_key, parameter_value in data.items():
            assert self.response.json()[parameter_key] == parameter_value, "Value of the created object is wrong"

    @allure.step('Check success status code')
    def check_success(self):
        assert self.response.status_code in [200, 201], f"Unexpected status code: {self.response.status_code}"

    @allure.step('Check response content type')
    def check_content_type(self):
        assert self.response.headers['Content-Type'] == 'application/json', "Incorrect Content-Type"

    @allure.step('Check response structure')
    def check_response_structure(self, expected_keys):
        response_json = self.response.json()
        for key in expected_keys:
            assert key in response_json, f"Parameter '{key}' not found in response"

    @allure.step('Check for status code 400')
    def check_status_request_400(self, data=None, headers=None):
        headers = headers if headers else self.headers
        data = data if data else self.default_data
        self.response = requests.post(f"{self.url}/object", json=data, headers=headers)
        assert self.response.status_code == 400, f"Unexpected status code: {self.response.status_code}"

    @allure.step('Check specific parameter value')
    def check_specific_parameter(self, key, expected_value):
        assert self.response.json()[key] == expected_value, \
            f"Value for '{key}' is wrong: '{self.response.json()[key]}'"

    @allure.step('Check response time')
    def check_response_time(self, max_time):
        assert self.response.elapsed.total_seconds() < max_time, \
            f"Response took too much time: {self.response.elapsed.total_seconds()} seconds"

    @allure.step("Deleting object")
    def delete_object(self, object_id):
        requests.delete(f"{self.url}/object/{object_id}")

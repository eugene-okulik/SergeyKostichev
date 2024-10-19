import requests
import allure
from test_api_skostichev.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    @allure.step('Create a new object with POST method')
    def create_new_object(self, data=None, headers=None):
        headers = headers if headers else self.headers
        data = data if data else self.default_data
        self.response = requests.post(f"{self.url}/object", json=data, headers=headers)
        try:
            self.response_json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.response_json = ""
        return self.response

    @allure.step('Check parameter values in the new object')
    def check_response_name_is_correct(self, data):
        for parameter_key, parameter_value in data.items():
            assert self.response.json()[parameter_key] == parameter_value, "Value of the created object is wrong"

    @allure.step('Check response content type')
    def check_content_type(self):
        assert self.response.headers['Content-Type'] == 'application/json', "Incorrect Content-Type"

    @allure.step('Check response structure')
    def check_response_structure(self, expected_keys):
        response_json = self.response.json()
        for key in expected_keys:
            assert key in response_json, f"Parameter '{key}' not found in response"

    @allure.step('Check specific parameter value')
    def check_specific_parameter(self, key, expected_value):
        assert self.response.json()[key] == expected_value, \
            f"Value for '{key}' is wrong: '{self.response.json()[key]}'"

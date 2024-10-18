import allure
import requests
from test_api_skostichev.endpoints.endpoint import Endpoint


class PartUpdateObject(Endpoint):

    @allure.step('Change test object with PATCH method')
    def patch_object(self, test_object, data, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(f'{self.url}/object/{test_object.json()["id"]}', json=data, headers=headers)
        try:
            self.response_json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.response_json = ""
        return self.response

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

import allure
import requests
from test_api_skostichev.endpoints.endpoint import Endpoint


class GetObject(Endpoint):
    @allure.step('Retrieve an object using GET method')
    def get_object(self, test_object=None, test_id=None):
        if test_object:
            test_id = test_object.json()["id"]
        else:
            test_id = test_id
        self.response = requests.get(f'{self.url}/object/{test_id}')
        return self.response

    @allure.step('Check for 404 status code when object does not exist')
    def check_not_found(self, object_id):
        self.response = requests.get(f'{self.url}/object/{object_id}')
        assert self.response.status_code == 404, f"Expected 404 but got {self.response.status_code}"

    @allure.step('Check parameter values in the retrieved object')
    def check_response_values(self, expected_data):
        response_json = self.response.json()
        for key, expected_value in expected_data.items():
            assert response_json[key] == expected_value, f"Value of '{key}' is wrong: '{response_json[key]}'"

    @allure.step('Check response structure')
    def check_response_structure(self, expected_keys):
        response_json = self.response.json()
        for key in expected_keys:
            assert key in response_json, f"Key '{key}' not found in response"

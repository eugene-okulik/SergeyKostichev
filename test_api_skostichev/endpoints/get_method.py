import allure
import requests
from test_api_skostichev.endpoints.http_method import HTTPMethod


class GETMethod(HTTPMethod):
    @allure.step('Retrieve an object using GET method')
    def get_object(self, test_object):
        self.response = requests.get(f'{self.url}/object/{test_object.json()["id"]}')
        return self.response

    @allure.step('Check success status code')
    def check_success(self):
        assert self.response.status_code == 200, f"Unexpected status code: {self.response.status_code}"

    @allure.step('Check for 404 status code when object does not exist')
    def check_not_found(self, object_id):
        self.response = requests.get(f'{self.url}/object/{object_id}')
        assert self.response.status_code == 404, f"Expected 404 but got {self.response.status_code}"

    @allure.step('Check parameter values in the retrieved object')
    def check_response_values(self, expected_data):
        response_json = self.response.json()
        for key, expected_value in expected_data.items():
            assert response_json[
                       key] == expected_value, f"Expected value for '{key}' is '{expected_value}', got '{response_json[key]}'"

    @allure.step('Check response structure')
    def check_response_structure(self, expected_keys):
        response_json = self.response.json()
        for key in expected_keys:
            assert key in response_json, f"Key '{key}' not found in response"

    @allure.step('Check response time')
    def check_response_time(self, max_time):
        assert self.response.elapsed.total_seconds() < max_time, f"Response took too long: {self.response.elapsed.total_seconds()} seconds"

import allure
import requests
from test_api_skostichev.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    template = "{0}/object/{1}"
    @allure.step('Delete an object using DELETE method')
    def delete_object(self, test_object):
        test_object_id = test_object.json()["id"]
        self.response = requests.delete(self.template.format(self.url, test_object_id))
        return self.response

    @allure.step('Check success status code on delete')
    def check_success(self):
        assert self.response.status_code == 200, f"Unexpected status code: {self.response.status_code}"

    @allure.step('Check if object is truly deleted')
    def verify_object_deleted(self, test_object):
        test_object_id = test_object.json()["id"]
        response = requests.get(self.template.format(self.url, test_object_id))
        assert response.status_code == 404, \
            f"Object with ID {test_object_id} was not deleted"

    @allure.step('Check delete on non-existent object')
    def check_delete_non_existent_object(self, object_id):
        self.response = requests.delete(self.template.format(self.url, object_id))
        assert self.response.status_code == 404, f"Unexpected status code: {self.response.status_code}"

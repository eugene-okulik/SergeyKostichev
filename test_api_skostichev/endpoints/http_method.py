import allure
import requests


class HTTPMethod:
    url = 'http://167.172.172.115:52353'
    response = None
    response_json = None
    headers = {"Content-Type": "application/json"}
    default_data = {"name": "Pencil", "data": {"color": "transparent", "size": "XXL"}}

    @allure.step("Deleting object")
    def delete_object(self, object_id):
        requests.delete(f"{self.url}/object/{object_id}")

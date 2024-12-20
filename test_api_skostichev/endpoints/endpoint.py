import allure


class Endpoint:
    url = 'http://167.172.172.115:52353'
    response = None
    response_json = None
    headers = {"Content-Type": "application/json"}
    default_data = {"name": "Pencil", "data": {"color": "transparent", "size": "XXL"}}

    @allure.step('Check response time')
    def check_response_time(self, max_time):
        assert self.response.elapsed.total_seconds() < max_time, \
            f"Response took too long: {self.response.elapsed.total_seconds()} seconds"

    @allure.step('Check 400 status code for invalid data')
    def check_response_400(self):
        assert self.response.status_code == 400, f"Unexpected status code: {self.response.status_code}"

    @allure.step('Check 404 status code for invalid data')
    def check_response_404(self):
        assert self.response.status_code == 404, f"Unexpected status code: {self.response.status_code}"

    @allure.step('Check success status code')
    def check_success(self):
        assert self.response.status_code == 200, f"Unexpected status code: {self.response.status_code}"

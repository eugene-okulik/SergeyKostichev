import random
from locust import task, HttpUser

TEST_DATA = [
    {"name": "Pencil", "data": {"color": "transparent", "size": "XXL"}},
    {"name": "Notebook", "data": {"color": "blue", "size": "A4"}},
    {"name": "Eraser", "data": {"color": "white", "size": "small"}}
]

NEGATIVE_DATA = [
    {"name": None, "data": {"color": "transparent", "size": "XXL"}},
    {"data": {"color": None, "size": "XXL"}, "id": 99999},
    {"name": "Pencil", "": None}
]


class ObjectUser(HttpUser):
    token = None
    object_ids = None
    headers = {"Content-Type": "application/json"}

    def on_start(self):
        response = self.client.get('/object', headers=self.headers)
        response_data = response.json()
        self.object_ids = [item['id'] for item in response_data.get('data', [])]

    @task(1)
    def get_all_objects(self):
        self.client.get(
            '/object',
            headers=self.headers
        )

    @task(4)
    def get_one_object(self):
        if self.object_ids:
            self.client.get(
                f'/object/{random.choice(self.object_ids)}',
                headers=self.headers
            )

    @task(3)
    def post_object(self):
        data = random.choice(TEST_DATA)
        self.client.post(
            '/object',
            json=data,
            headers=self.headers
        )

    @task(3)
    def post_object_with_negative_data(self):
        data = random.choice(NEGATIVE_DATA)
        self.client.post(
            '/object',
            json=data,
            headers=self.headers
        )

    @task(2)
    def put_object(self):
        data = random.choice(TEST_DATA)
        object_id = random.choice(self.object_ids)
        self.client.put(
            f'/object/{object_id}',
            json=data,
            headers=self.headers
        )

    @task(2)
    def put_object_with_negative_data(self):
        data = random.choice(NEGATIVE_DATA)
        object_id = random.choice(self.object_ids)
        self.client.put(
            f'/object/{object_id}',
            json=data,
            headers=self.headers
        )

    @task(2)
    def patch_object(self):
        if self.object_ids:
            data = random.choice(TEST_DATA)
            object_id = random.choice(self.object_ids)
            self.client.patch(
                f'/object/{object_id}',
                json=data,
                headers=self.headers
            )

    @task(2)
    def patch_object_with_negative_data(self):
        if self.object_ids:
            data = random.choice(NEGATIVE_DATA)
            object_id = random.choice(self.object_ids)
            self.client.patch(
                f'/object/{object_id}',
                json=data,
                headers=self.headers
            )

    @task(1)
    def delete_object(self):
        if self.object_ids:
            object_id = random.choice(self.object_ids)
            self.client.delete(
                f'/object/{object_id}',
                headers=self.headers
            )

    @task(1)
    def delete_non_existent_object(self):
        fake_id = 999999
        self.client.delete(
            f'/object/{fake_id}',
            headers=self.headers
        )

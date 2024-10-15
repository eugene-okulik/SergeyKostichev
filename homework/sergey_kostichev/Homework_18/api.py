import requests

url = 'http://167.172.172.115:52353/'
response = requests.get(url)


def get_object(obj_id):
    template = f'{url}/object/{obj_id}'
    response = requests.get(template)
    assert response.status_code == 200, "Page didn't answer"
    return response


def post_object():
    length = len(requests.get(url + '/object').json()["data"])
    template = f'{url}/object'

    body = {
        "name": "Pencil",
        "data": {
            "color": "black",
            "size": "XXL"
        }
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(template, json=body, headers=headers)
    new_length = len(requests.get(url + '/object').json()["data"])

    assert length + 1 == new_length, "Object was not added"

    assert response.status_code == 200, f"Process was finished with {response.status_code}"

    return response


def put_post(post_id):
    template = f'{url}/object/{post_id}'
    body = {
        "name": "T-shirt",
        "data": {
            "color": "green",
            "size": "M"
        }
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.put(template, json=body, headers=headers)
    assert len(response.json()) == 3, "Not all datas were saved"

    return response


def patch_post(post_id):
    template = f'{url}/object/{post_id}'
    body = {
        "data": {
            "color": "yellow"
        }
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.patch(template, json=body, headers=headers)
    assert response.status_code == 200, "Not all datas were saved"
    return response


def delete_post(post_id):
    template = f'{url}/object/{post_id}'
    response = requests.delete(template)
    assert response.status_code == 200, "Post wasn't deleted"


def decode_response(new_response):
    print(new_response.json())


post = post_object()
post_id = post.json()['id']
decode_response(post)

post = put_post(post_id)
decode_response(post)

post = patch_post(post_id)
decode_response(post)

post = get_object(post_id)
decode_response(post)

delete_post(post_id)

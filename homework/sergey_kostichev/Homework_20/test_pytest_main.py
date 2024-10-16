import allure
import pytest
import requests
from faker import Faker

url = 'http://167.172.172.115:52353/'


@allure.feature('Objects')
@allure.story('Objects interaction')
@allure.title('Создание 3 объектов через параметр')
@pytest.mark.critical
@pytest.mark.parametrize('object_data', [
    {'name': 'Thing1', 'data': {'color': 'black', 'size': 'XXL'}},
    {'name': 'Thing2', 'data': {'color': 'blue', 'size': 'A2'}},
    {'name': 'Thing3', 'data': {'color': 'white', 'size': 'small'}}])
def test_post_object(object_data, header):
    with allure.step('Подготовка тестовых данных'):
        template = f'{url}/object'
        old_length = len(requests.get(template).json()["data"])
        body = object_data
    with allure.step('Post запрос на создание объекта'):
        response = requests.post(template, json=body, headers=header)
    with allure.step('Проверка статус кода'):
        assert response.status_code == 200, "Object was not created"
    with allure.step('Сбор обновленных данных после добавления объекта'):
        new_length = len(requests.get(template).json()["data"])
    with allure.step('Сравнение предыдущего и текущего количества объектов'):
        assert old_length + 1 == new_length, "Object was not added"


@allure.feature('Objects')
@allure.story('Objects interaction')
@allure.title('Изменение объекта по айди через put-запрос')
@pytest.mark.medium
def test_put_object(response, header):
    with allure.step('Подготовка тестовых данных'):
        template = f'{url}/object/{response.json()["id"]}'
        body = {"name": "T-shirt", "data": {"color": "green", "size": "M"}}
    with allure.step('Put запрос для внесения изменений в объект по айди'):
        response = requests.put(template, json=body, headers=header)
    with allure.step('Проверка статус кода'):
        assert response.status_code == 200, "Datas were not updated"
    with allure.step('Проверка длины измененного объекта'):
        assert len(response.json()) == 3, "Not all datas were saved"


@allure.feature('Objects')
@allure.story('Objects interaction')
@allure.title('Изменение объекта по айди через patch-запрос')
def test_patch_object(response, header):
    with allure.step('Настройка фейковых данных'):
        fake = Faker()
        color_name = fake.color_name()
    with allure.step('Подготовка тестовых данных'):
        template = f'{url}/object/{response.json()["id"]}'
        body = {"data": {"color": color_name}}
    with allure.step('Patch запрос для внесения изменений в объект по айди'):
        response = requests.patch(template, json=body, headers=header)
    with allure.step('Проверка статус кода'):
        assert response.status_code == 200, "Not all datas were saved"
    with allure.step('Проверка обновленного параметра color'):
        assert response.json()["data"]["color"] == color_name, "There is wrong data"


@allure.feature('Objects')
@allure.story('Objects interaction')
@allure.title('Удаление объекта по айди')
def test_delete_object(response):
    with allure.step('Подготовка тестовых данных'):
        old_length = len(requests.get(url + '/object').json()["data"])
        template = f'{url}/object/{response.json()["id"]}'
    with allure.step('Delete запрос для удаления объекта по айди'):
        response = requests.delete(template)
    with allure.step('Проверка статус кода'):
        assert response.status_code == 200, "Post was not deleted"
    with allure.step('Сбор обновленных данных после добавления объекта'):
        new_length = len(requests.get(url + '/object').json()["data"])
    with allure.step('Сравнение предыдущего и текущего количества объектов'):
        assert old_length - 1 == new_length, "Object was not deleted"


@allure.feature('Objects')
@allure.story('Get objects')
@allure.title('Получение объекта по айди')
def test_get_object(response):
    with allure.step('Подготовка тестовых данных'):
        template = f'{url}/object/{response.json()["id"]}'
    with allure.step('Get запрос на получение объекта по айди'):
        response = requests.get(template)
    with allure.step('Проверка статус кода'):
        assert response.status_code == 200, "Page didn't answer"
    with allure.step('Проверка длины измененного объекта'):
        assert len(response.json()) == 3, "Page structure is incorrect"

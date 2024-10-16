import allure
import pytest


@allure.feature('Experiments')
@allure.story('Equals')
@allure.title('Сравнение переменной с 1')
@pytest.mark.experiment
def test_experiment_1():
    var = 2
    assert 1 == var, f"1 is not equal {var}"


@allure.feature('Experiments')
@allure.story('Equals')
@allure.title('Сравнение переменной с 100')
@pytest.mark.experiment
def test_experiment_2():
    var = 100
    assert 100 == var, f"100 is not equal {var}"


@allure.feature('Experiments')
@allure.story('Equals')
@allure.title('Сравнение переменной с 1000')
@pytest.mark.experiment
def test_experiment_3():
    var = 1000
    assert 1000 == var, f"1000 is not equal {var}"


@allure.feature('Experiments')
@allure.story('Print')
@allure.title('Вывод переменной')
@pytest.mark.experiment
def test_print():
    var = 1
    print(var)


@allure.feature('Experiments')
@allure.story('Print')
@allure.title('Сравнение переменной после вычисления')
@pytest.mark.experiment
def test_print_2():
    var = 100
    var = 100 / 2 * 3 + 5
    print(var)

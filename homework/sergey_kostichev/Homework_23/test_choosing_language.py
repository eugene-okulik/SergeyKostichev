import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

language = 'Python'


@pytest.fixture(scope='session')
def browser():
    options = Options()
    options.add_argument('--force-device-scale-factor=0.5')
    options.add_experimental_option('detach', True)
    browser = webdriver.Chrome(options=options)
    browser.get('https://www.qa-practice.com/elements/select/single_select')
    return browser


def test_choose_language(browser):
    driver = browser
    try:
        select_element = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.ID, 'id_choose_language'))
        )
        select = Select(select_element)
        select.select_by_visible_text(language)
        # select.select_by_index(1)


    except Exception as e:
        print(f"An error occurred: {e}")

    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()

    result = driver.find_element(By.ID, 'result').text
    assert language in result, f"Wrong result: {result}"

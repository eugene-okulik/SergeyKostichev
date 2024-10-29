from turtledemo.penrose import start

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

text = 'Hello World'


@pytest.fixture(scope='session')
def browser():
    options = Options()
    options.add_argument('--force-device-scale-factor=0.5')
    #  options.add_experimental_option('detach', True)
    browser = webdriver.Chrome(options=options)
    browser.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    return browser


def test_hello_world(browser):
    driver = browser
    start_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "//button[text()='Start']"))
    )
    start_button.click()

    finish_label = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'finish'))
    )
    assert text in finish_label.text, f"Wrong result: {finish_label}"

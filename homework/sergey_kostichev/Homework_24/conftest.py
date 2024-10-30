import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def browser():
    options = Options()
    options.add_argument('--force-device-scale-factor=0.5')
    options.add_experimental_option('detach', True)
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(4)
    return browser

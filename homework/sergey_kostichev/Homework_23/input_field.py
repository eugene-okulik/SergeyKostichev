from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def open_browser(link):
    options = Options()
    options.add_argument('start-maximized')
    #  options.add_experimental_option('detach', True)
    browser = webdriver.Chrome(options=options)
    browser.get(link)
    return browser

driver = open_browser('https://www.qa-practice.com/elements/input/simple')
input_field = driver.find_element(By.NAME, 'text_string')
input_field.send_keys('typingsometext23_0')
input_field.submit()
result_text = driver.find_element(By.ID, 'result-text')
print(result_text.text)

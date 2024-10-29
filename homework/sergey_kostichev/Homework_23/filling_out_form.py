from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def open_browser(link):
    options = Options()
    options.add_argument('--force-device-scale-factor=0.5')
    #  options.add_experimental_option('detach', True)
    browser = webdriver.Chrome(options=options)
    browser.get(link)
    return browser


driver = open_browser('https://demoqa.com/automation-practice-form')

first_name_field = driver.find_element(By.ID, 'firstName')
first_name_field.send_keys('Sergey')
last_name_field = driver.find_element(By.ID, 'lastName')
last_name_field.send_keys('Kutrapali')
user_email_field = driver.find_element(By.ID, 'userEmail')
user_email_field.send_keys('sergey.kutrapali@mail.ru')
label_element = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
label_element.click()
user_number_field = driver.find_element(By.ID, 'userNumber')
user_number_field.send_keys('9655485654')
date_of_birth_input = driver.find_element(By.ID, 'dateOfBirthInput')
date_of_birth_input.send_keys('20 Feb 2000')
date_of_birth_input.send_keys(Keys.ENTER)
subjects_input = driver.find_element(By.ID, 'subjectsInput')
subjects_input.send_keys('H')
subjects_input.send_keys(Keys.ENTER)

label_element = driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
label_element.click()
label_element = driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
label_element.click()
#  music_checkbox = driver.find_element('hobbies-checkbox-3')

state_dropdown = driver.find_element(By.CSS_SELECTOR, "div#state .css-yk16xz-control")
state_dropdown.click()
state_input = driver.find_element(By.ID, "react-select-3-input")
state_input.send_keys("Uttar")
state_input.send_keys(Keys.ENTER)

city_dropdown = driver.find_element(By.ID, "city")
city_dropdown.click()
city_input = driver.find_element(By.ID, "react-select-4-input")
city_input.send_keys("A")
city_input.send_keys(Keys.ENTER)

current_address_textarea = driver.find_element(By.ID, 'currentAddress')
current_address_textarea.send_keys('There is my Address: I want in Central Asia, Afghanistan')

submit_button = driver.find_element(By.ID, 'submit')
submit_button.click()

try:
    modal = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "div.modal.show"))
    )

    table = modal.find_element(By.CSS_SELECTOR, "table.table")

    rows = table.find_elements(By.TAG_NAME, "tr")

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if cells:
            label = cells[0].text
            value = cells[1].text
            print(f"{label}: {value}")

except Exception as e:
    print(f"An error occurred: {e}")

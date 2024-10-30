import time
import random
import pytest
from selenium.common import NoAlertPresentException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.skip("checked")
def test_add_to_cart(browser):
    browser.get('https://www.demoblaze.com/index.html')
    time.sleep(3)
    #  Никакие ожидания не помогают, ни явные, ни неявные.
    #  Тег для таблицы есть сразу, но таблица заполняется позже. Не получилось заставить ожидать заполнения таблицы.
    WebDriverWait(browser, 10).until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, ".col-lg-4.col-md-6.mb-4"))
    )
    products = browser.find_elements(By.CSS_SELECTOR, ".col-lg-4.col-md-6.mb-4")

    random_product = random.choice(products)
    product_name = random_product.find_element(By.TAG_NAME, "h4").text
    product_price = random_product.find_element(By.TAG_NAME, "h5").text.replace('$', '').strip()
    random_product_link = random_product.find_element(By.TAG_NAME, "a")

    actions = ActionChains(browser)
    actions.key_down(Keys.CONTROL).click(random_product_link).key_up(Keys.CONTROL).perform()

    browser.switch_to.window(browser.window_handles[-1])

    add_to_cart_button = WebDriverWait(browser, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-success.btn-lg"))
    )
    add_to_cart_button.click()

    try:
        WebDriverWait(browser, 5).until(ec.alert_is_present())
        alert = browser.switch_to.alert
        alert.accept()
    except NoAlertPresentException:
        print("There is no alert")
    finally:
        browser.close()

    browser.switch_to.window(browser.window_handles[0])

    browser.find_element(By.ID, 'cartur').click()

    WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.ID, "tbodyid"))
    )

    rows = browser.find_elements(By.CSS_SELECTOR, "#tbodyid tr")
    found_product = False

    for row in rows:
        title = row.find_element(By.XPATH, ".//td[2]").text
        price = row.find_element(By.XPATH, ".//td[3]").text

        if title == product_name and price == product_price:
            found_product = True
            break

    assert found_product, "Item was not found."

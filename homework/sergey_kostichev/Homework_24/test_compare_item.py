import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


def test_add_to_cart(browser):
    browser.get('https://magento.softwaretestingboard.com/gear/bags.html')

    products_list = browser.find_elements(By.CSS_SELECTOR, ".item.product.product-item")

    random_product = random.choice(products_list)
    random_product_name = random_product.find_element(By.CSS_SELECTOR, ".product-item-link").text
    actions = ActionChains(browser)
    to_compare_button = random_product.find_element(By.CSS_SELECTOR, ".action.tocompare")
    actions.move_to_element(random_product).click(to_compare_button).perform()

    WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.ID, 'compare-items')))
    compare_table = browser.find_element(By.ID, 'compare-items').find_elements(By.TAG_NAME, 'li')

    for item in compare_table:
        compared_product_name = item.find_element(By.CSS_SELECTOR, '.product-item-link').text
        assert compared_product_name == random_product_name, \
            f'Names are not matching {compared_product_name} is not {random_product_name}'

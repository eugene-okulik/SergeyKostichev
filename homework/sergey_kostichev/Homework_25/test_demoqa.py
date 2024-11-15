from playwright.sync_api import Page, expect
import time


def test_fill_out_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Sergey')
    page.get_by_placeholder('Last Name').fill('Kostichev')
    page.get_by_placeholder('name@example.com').fill('sergey.kostichev@gmail.com')
    page.get_by_placeholder('Mobile Number').fill('6666688998')
    page.locator('#dateOfBirthInput').fill('28 Feb 1989')
    subject = page.locator('#subjectsInput')
    subject.click()
    subject.fill('Maths')
    subject.press('Enter')
    page.get_by_placeholder('Current Address').fill('Home sweet home')
    state_field = page.locator('#state')
    state_field.click()
    state_field.press_sequentially('ncr')
    state_field.press('Enter')
    city_field = page.locator('#city')
    city_field.click()
    city_field.press_sequentially("Delhi")
    city_field.press('Enter')

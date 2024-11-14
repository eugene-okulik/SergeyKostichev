import re
import time

from playwright.sync_api import Page, expect


def test_get_by_role(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    time.sleep(2)
    page.get_by_role('link', name='Form Authentication').click()
    time.sleep(2)
    field = page.get_by_role('textbox', name='username')
    field.fill('tomsmith')
    field = page.get_by_role('textbox', name='password')
    field.fill('SuperSecretPassword!')
    page.get_by_role('button', name='Login').click()
    expect(page).to_have_url(re.compile('https://the-internet.herokuapp.com/secure'))
    time.sleep(2)

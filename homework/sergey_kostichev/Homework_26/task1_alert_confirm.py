from time import sleep
from playwright.sync_api import Page, Dialog, expect


def test_alert(page: Page):
    def ok_alert(alert: Dialog):
        alert.accept()
    page.on('dialog', ok_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    expect(page.locator('#result-text'), "Dialog was not accepted").to_have_text('Ok')




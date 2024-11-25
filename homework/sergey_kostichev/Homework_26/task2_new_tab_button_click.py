from playwright.sync_api import Page, BrowserContext, expect


def test_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    link = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        link.click()

    page2 = new_page_event.value
    result_on_new_page = page2.locator('#result-text')
    expect(result_on_new_page, "There is no new tab").to_have_text('I am a new page in a new tab')
    page2.close()

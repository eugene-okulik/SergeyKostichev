from playwright.sync_api import Page, expect


def test_color_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    btn_color = page.get_by_role('button', name='Color Change')
    expect(btn_color).to_have_css('color', 'rgb(220, 53, 69)')
    btn_color.click()

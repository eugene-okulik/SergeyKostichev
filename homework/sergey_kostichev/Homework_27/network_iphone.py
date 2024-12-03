import re
import json
from playwright.sync_api import Route, expect, Page


def test_change_iphone(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body = json.dumps(body)
        body = body.replace('iPhone 16 Pro', 'Яблокофон 16 про')
        body = body.replace(r'iPhone\u00a016\u00a0Pro', 'Яблокофон 16 про')
        route.fulfill(
            status=response.status,
            headers=response.headers,
            content_type="application/json",
            body=body
        )

    page.route(re.compile('/step0_iphone/'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    locator = page.locator('.rf-cards-scroller-itemview').first
    expect(locator).to_be_visible()
    locator.click()

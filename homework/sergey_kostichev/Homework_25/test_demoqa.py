from playwright.sync_api import Page, expect


def test_fill_out_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Sergey')

    page.get_by_placeholder('Last Name').fill('Kostichev')

    email = page.get_by_placeholder('name@example.com')
    email.fill('sergey.kostichev@gmail.com')

    gender = page.locator('#genterWrapper')
    gender.press('Tab', delay=500)
    gender.press('Space')

    page.get_by_placeholder('Mobile Number').fill('6666688998')

    page.locator('#dateOfBirthInput').fill('28 Feb 1989')

    subject = page.locator('#subjectsInput')
    subject.click()
    subject.fill('Maths')
    subject.press('Enter')

    hobbies = page.locator('#hobbiesWrapper')
    hobbies.press('Tab', delay=500)
    hobbies.press('Space')
    hobbies.press('Tab', delay=500)
    hobbies.press('Tab', delay=500)
    hobbies.press('Space')

    page.get_by_placeholder('Current Address').fill('Home sweet home')

    state_field = page.locator('#state')
    state_field.click()
    state_field.press_sequentially('ncr', delay=500)
    state_field.press('Enter')

    city_field = page.locator('#city')
    city_field.click()
    city_field.press_sequentially("Delhi", delay=500)
    city_field.press('Enter')
    page.locator('#submit').click()
    modal_title = page.locator('#example-modal-sizes-title-lg')
    expect(modal_title).to_be_visible()
    response = modal_title.text_content()

    assert response == 'Thanks for submitting the form', "The form was not filled out"

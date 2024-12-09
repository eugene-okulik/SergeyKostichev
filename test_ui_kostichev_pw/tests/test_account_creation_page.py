import utils.test_data as td
from utils.messages import Messages

def test_creation_account(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_in_account_form_properly()


def test_creation_account_with_wrong_confirmation_password(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_in_account_form_properly(password_confirmation=False)


def test_creation_account_with_existed_email(create_account_page):
    create_account_page.open_page()
    create_account_page.check_mismatching_password(Messages.EXISTED_EMAIL_ERROR.value)

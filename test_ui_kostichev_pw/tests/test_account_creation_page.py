import utils.test_data as td
from utils.messages import Messages


def test_creation_account(create_account_page):
    create_account_page.open_page()
    field_flags = td.validate_field_flags()
    create_account_page.check_filling_required_fields(field_flags=field_flags,
                                                      account_data=td.generate_account_data(field_flags))


def test_creation_account_with_wrong_confirmation_password(create_account_page):
    create_account_page.open_page()
    field_flags = td.validate_field_flags(password_confirmation=False)
    create_account_page.check_filling_required_fields(field_flags=field_flags,
                                                      account_data=td.generate_account_data(field_flags))


def test_creation_account_with_existed_email(create_account_page):
    create_account_page.open_page()
    create_account_page.check_mismatching_password(Messages.EXISTED_EMAIL_ERROR.value)

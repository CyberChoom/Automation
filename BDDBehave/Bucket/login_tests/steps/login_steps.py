from behave import given, when, then
from pages.login_page import LoginPage


@given("user launched the login page")
def launch_login_page(context):
    login_page = LoginPage(context.browser)
    context.login_page = login_page


@given("user is not logged in")
def verify_user_not_logged_in(context):
    login_page = LoginPage(context.browser)
    assert login_page.get_new_customer_title() == "New Customer"
    assert login_page.get_returning_customer_title() == "Returning Customer"
    context.login_page = login_page


@when('user types "{value}" in "{field}"')
def enter_email_and_password(context, value, field):
    context.execute_steps(
        """
        When user enters email "{value}" in "{field}"
        When user enters password "{value}" in "{field}"
        """
    )


@when('user enters email "{value}" in "{field}"')
def enter_email(context, value, field):
    login_page = context.login_page
    if value == "None":
        return
    if field == "email":
        login_page.input_email(value)


@when('user enters password "{value}" in "{field}"')
def enter_password(context, value, field):
    login_page = context.login_page
    if value == "None":
        return
    if field == "password":
        login_page.input_password(value)


@when('user clicks Login button')
def click_login_button(context):
    login_page = context.login_page
    login_page.press_login()


@then('warning is shown "Warning: No match for E-Mail Address and/or Password."')
def verify_warning(context):
    login_page = context.login_page
    assert login_page.get_warning() == "Warning: No match for E-Mail Address and/or Password."

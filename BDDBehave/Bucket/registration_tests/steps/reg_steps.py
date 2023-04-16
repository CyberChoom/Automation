from behave import given, when, then
from BDDBehave.utils.config_reader import ConfigReader
from pages.registration_page import RegistrationPage

configs = ConfigReader("C:/Users/user/Desktop/Automation/BDDBehave/Bucket/registration_tests/steps/config.ini")


@given('user launched the registration page')
def launch_registration_page(context):
    registration_page = RegistrationPage(context.browser)
    context.registration_page = registration_page

#
@when('user enters his "{first_name}" in the First Name field')
def enter_first_name(context, first_name):
    registration_page = context.registration_page
    if first_name == "None":
        pass
    else:
        registration_page.enter_first_name(first_name)


@when('"{last_name}" in the Last Name field')
def enter_last_name(context, last_name):
    registration_page = context.registration_page
    if last_name == "None":
        pass
    else:
        registration_page.enter_last_name(last_name)


@when('"{email}" in the E-Mail field')
def enter_email(context, email):
    registration_page = context.registration_page
    if email == "None":
        pass
    else:
        registration_page.enter_email(email)


@when('"{phone}" in the Telephone field')
def enter_phone(context, phone):
    registration_page = context.registration_page
    if phone == "None":
        pass
    else:
        registration_page.enter_telephone(phone)


@when('"{address}" in the Address 1 field')
def enter_address(context, address):
    registration_page = context.registration_page
    if address == "None":
        pass
    else:
        registration_page.enter_first_line_address(address)


@when('"{city}" in the City field')
def enter_city(context, city):
    registration_page = context.registration_page
    if city == "None":
        pass
    else:
        registration_page.enter_city(city)


@when('"{country}" in the Country field')
def enter_country(context, country):
    registration_page = context.registration_page
    if country == "None":
        pass
    else:
        registration_page.select_country(country)


@when('"{state}" in the Region / State field')
def enter_state(context, state):
    registration_page = context.registration_page
    if state == "None":
        pass
    else:
        registration_page.select_state(state)


@when('"{password}" in the Password field')
def enter_password(context, password):
    registration_page = context.registration_page
    if password == "None":
        pass
    else:
        registration_page.enter_password(password)


@when('"{password}" in the Password Confirm field')
def confirm_password(context, password):
    registration_page = context.registration_page
    if password == "None":
        pass
    else:
        registration_page.confirm_password(password)


@when('user clicks on the "Privacy Policy" checkbox')
def tick_privacy_policy(context):
    registration_page = context.registration_page
    registration_page.agree_to_privacy_policy()


@when('user clicks on the "Register" button')
def register(context):
    registration_page = context.registration_page
    registration_page.submit_form()


@then('user account is created, message stating "Your Account Has Been Created!" is shown')
def successful_registration_alert(context):
    registration_page = context.registration_page
    registration_page.verify_successful_registration()


@then('user account is not created, message stating "Warning: You must agree to the Privacy Policy!" is shown')
def privacy_policy_warning(context):
    registration_page = context.registration_page
    registration_page.verify_privacy_policy_warning()

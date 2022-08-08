from selenium.webdriver.common.by import By
import time

from webelements.browser import Browser
from webelements.UIElement import UIElement as Element
from webelements.dropdown import Dropdown

from components.header import Header
from components.right_menu import RightMenu

# 8-7-2022    V
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage

URL = "https://cleveronly.com/brainbucket"


def test_registration_through_dropdown():
    browser = Browser(URL, "firefox")
    driver = browser.get_driver()

    header = Header(browser)
    header.change_currency("gbp")

    # 8-7-2022    V
    login_page = LoginPage(browser)
    login_page.open_registration_from_account_dropdown()

    registration_form = RegistrationPage(browser)
    assert registration_form.get_form_title() == 'Register Account'

    registration_form.enter_first_name("Bob")
    registration_form.enter_last_name("Marcus")
    registration_form.enter_email("bob.marcus@cleverqqqqqqqqqonly.com")
    registration_form.enter_telephone("1234567890")
    registration_form.enter_first_line_address("42 Simpson Avenue")
    registration_form.enter_city("Chicago")
    registration_form.select_state("Illinois")
    registration_form.enter_password("testPassword")
    registration_form.confirm_password("testPassword")
    registration_form.subscribe_to_newsletters()
    registration_form.agree_to_privacy_policy()

    registration_form.submit_form()
    time.sleep(1)

    successful_registration_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
    assert successful_registration_title.get_text() == 'Your Account Has Been Created!'

    successful_registration_subtitle = Element(browser, By.XPATH, "//*[@id='content']/p")
    assert successful_registration_subtitle.get_text() == \
           'Congratulations! Your new account has been successfully created!'

    time.sleep(5)
    browser.shutdown()


def test_registration_from_right_menu():
    browser = Browser(URL, "firefox")
    driver = browser.get_driver()

    # 8-7-2022    V
    login_page = LoginPage(browser)
    login_page.open_registration_from_menu()

    registration_form = RegistrationPage(browser)
    registration_form.enter_first_name("Bob")
    registration_form.enter_last_name("Marcus")
    registration_form.enter_email("bob.marcus@cleverwwwwwwwonly.com")
    registration_form.enter_telephone("1234567890")
    registration_form.enter_first_line_address("42 Simpson Avenue")
    registration_form.enter_city("Chicago")
    registration_form.select_state("Illinois")
    registration_form.enter_password("testPassword")
    registration_form.confirm_password("testPassword")
    registration_form.subscribe_to_newsletters()
    registration_form.agree_to_privacy_policy()

    registration_form.submit_form()
    time.sleep(1)

    successful_registration_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
    assert successful_registration_title.get_text() == 'Your Account Has Been Created!'

    successful_registration_subtitle = Element(browser, By.XPATH, "//*[@id='content']/p")
    assert successful_registration_subtitle.get_text() == \
           'Congratulations! Your new account has been successfully created!'

    time.sleep(5)
    browser.shutdown()


if __name__ == "__main__":
    test_registration_through_dropdown()
    test_registration_from_right_menu()

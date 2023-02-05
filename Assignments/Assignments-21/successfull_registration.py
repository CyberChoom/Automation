from selenium.webdriver.common.by import By
import time
from webelements.browser import Browser
from webelements.UIElement import UIElement as Element
from webelements.dropdown import Dropdown
from components.header import Header
from components.right_menu import RightMenu
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utils.config_reader import ConfigReader

URL = "https://cleveronly.com/brainbucket"
configs = ConfigReader("config.json")


def test_registration_through_dropdown():
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    header = Header(browser)
    header.change_currency("gbp")

    login_page = LoginPage(browser)
    login_page.open_registration_from_account_dropdown()

    registration_form = RegistrationPage(browser)
    assert registration_form.get_form_title() == 'Register Account'

    registration_form.enter_first_name("Bob")
    registration_form.enter_last_name("Marcus")
#   2/4/2023 - V
#   Using config_reader
    registration_form.enter_email(configs.get_user1_email())
    registration_form.enter_telephone("1234567890")
    registration_form.enter_first_line_address("42 Simpson Avenue")
    registration_form.enter_city("Chicago")
    registration_form.select_state("Illinois")
#   2/4/2023 - V
#   Using config_reader
    registration_form.enter_password(configs.get_user1_password())
    registration_form.confirm_password(configs.get_user1_password())

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
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    login_page = LoginPage(browser)
    login_page.open_registration_from_menu()

    registration_form = RegistrationPage(browser)
    registration_form.enter_first_name("Bob")
    registration_form.enter_last_name("Marcus")
#   2/4/2023 - V
#   Using config_reader
    registration_form.enter_email(configs.get_user1_email())
    registration_form.enter_telephone("1234567890")
    registration_form.enter_first_line_address("42 Simpson Avenue")
    registration_form.enter_city("Chicago")
    registration_form.select_state("Illinois")
#   2/4/2023 - V
#   Using config_reader
    registration_form.enter_password(configs.get_user1_password())
    registration_form.confirm_password(configs.get_user1_password())
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

from selenium.webdriver.common.by import By
import time

from webelements.browser import Browser
from webelements.UIElement import UIElement as Element
from webelements.dropdown import Dropdown

from components.header import Header
from components.right_menu import RightMenu

URL = "https://cleveronly.com/brainbucket"


def test_registration_through_dropdown():
    browser = Browser(URL, "firefox")
    driver = browser.get_driver()

    header = Header(browser)
    header.open_registration_form()

    header.change_currency("gbp")

    registration_form_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
    assert registration_form_title.get_text() == 'Register Account'

    inputs = {
        'firstname': "Bob",
        'lastname': "Marcus",
        'email': "bob.marcus@cleveronly.com",
        'telephone': "1234567890",
        'fax': "1234567890",
        'company': "CleverOnly",
        'address_1': "42 Simpson Avenue",
        'city': "Chicago",
        'password': "testPassword",
        'confirm': "testPassword"
    }

    for field, text in inputs.items():
        input_field = Element(browser, By.NAME, field)
        input_field.enter_text(text)

    # find dropdown element for Country
    Dropdown(browser, By.ID, 'input-country').select_by_text("United States")

    # find dropdown element for Region
    Dropdown(browser, By.NAME, 'zone_id').select_by_text("Illinois")

    # clicking on subscribe YES radio button
    subscribe_btn = driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']")
    if not subscribe_btn.is_selected():
        subscribe_btn.click()

    agree_to_policy = driver.find_element(By.NAME, "agree")
    if not agree_to_policy.is_selected():
        agree_to_policy.click()

    Element(browser, By.XPATH, "//input[@value='Continue']").submit()
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

    # in Account dropdown select Login option
    header = Header(browser)
    header.open_login_page()

    # click on Register btn in the right menu
    right_menu = RightMenu(browser)
    right_menu.click_registration()

    registration_form_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
    assert registration_form_title.get_text() == 'Register Account'

    inputs = {
        'firstname': "Bob",
        'lastname': "Marcus",
        'email': "bob.marcus@cleveronly.com",
        'telephone': "1234567890",
        'fax': "1234567890",
        'company': "CleverOnly",
        'address_1': "42 Simpson Avenue",
        'city': "Chicago",
        'password': "testPassword",
        'confirm': "testPassword"
    }

    for field, text in inputs.items():
        input_field = driver.find_element(By.NAME, field)
        input_field.clear()
        input_field.send_keys(text)

    # find dropdown element for Country
    Dropdown(browser, By.ID, 'input-country').select_by_text("United States")

    # find dropdown element for Region
    Dropdown(browser, By.NAME, 'zone_id').select_by_text("Illinois")

    # clicking on subscribe YES radio button
    subscribe_btn = driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']")
    if not subscribe_btn.is_selected():
        subscribe_btn.click()

    driver.find_element(By.NAME, "agree").click()

    Element(browser, By.XPATH, "//input[@value='Continue']").submit()
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

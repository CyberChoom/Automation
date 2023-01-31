from webelements.browser import Browser
from webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
import time
from webelements.alert import Alert
from webelements.iframe import IFrame

URL = "https://cleveronly.com/practice/"


def test_simple_alert():
    browser = Browser(URL)
    alert_btn = Element(browser, By.XPATH, "//button[@onclick='openAlert()']")
    alert_btn.click()

    alert = Alert(browser)
    alert.accept_alert()

    browser.shutdown()


def test_confirmation_alert():
    browser = Browser(URL, "firefox")
    confirm_btn = Element(browser, By.XPATH, "//button[@onclick='openConfirmationAlert()']")
    confirm_btn.click()

    alert = Alert(browser)
    alert.dismiss_alert()

    msg = Element(browser, By.ID, 'msg')
    assert msg.get_text() == "You pressed CANCEL!"

    confirm_btn.click()
    alert.accept_alert()
    assert msg.get_text() == "You pressed OK!"

    browser.shutdown()


def test_prompt_alert():
    browser = Browser(URL, "firefox")
    prompt_btn = Element(browser, By.XPATH, "//button[@onclick='openPrompt()']")
    prompt_btn.click()

    alert = Alert(browser)
    name = "James White"
    alert.type_and_accept(name)

    msg = "Hello {}! How are you today?".format("James White")
    prompt_msg = Element(browser, By.ID, 'demo')
    assert prompt_msg.get_text() == msg

    browser.shutdown()


def test_iframe():
    browser = Browser(URL)
    iframe_example = Element(browser, By.TAG_NAME, 'iframe')
    iframe = IFrame(browser)
    iframe.switch_to_iframe(iframe_example.get_element())

    Element(browser, By.XPATH, "//*[@class='logo__title']").wait_until_visible()
    iframe.default_content()

    browser.shutdown()


if __name__ == "__main__":
    test_simple_alert()
    test_confirmation_alert()
    test_prompt_alert()
    test_iframe()

from webelements.browser import Browser
from webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from webelements.alert import Alert
from webelements.iframe import IFrame
from utils.config_reader import ConfigReader

URL = "https://cleveronly.com/practice/"
#   2/4/2023 - V
#   Using Config Reader
configs = ConfigReader("config.ini")


def test_simple_alert():
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time(), configs.get_width(), configs.get_height())
    alert_btn = Element(browser, By.XPATH, "//button[@onclick='openAlert()']")
    alert_btn.click()

    alert = Alert(browser)
    alert.accept_alert()

    browser.shutdown()


def test_confirmation_alert():
    #   2/4/2023 - V
    #   Using Config Reader
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
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
    #   2/4/2023 - V
    #   Using Config Reader
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
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
    #   2/4/2023 - V
    #   Using Config Reader
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
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

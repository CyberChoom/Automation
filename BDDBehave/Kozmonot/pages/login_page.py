from BDDBehave.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        self.sign_in_menu = Element(browser, By.XPATH, "//b[contains(.,'Sign In')]")
        self.email_input = Element(browser, By.NAME, "username")
        self.password_input = Element(browser, By.NAME, "password")
        self.sign_in_button = Element(browser, By.XPATH, "//button[contains(.,'Sign In')]")
        self.success_login_message = Element(browser, By.XPATH, "//div[contains(.,'You are now logged in..')]")
        self.success_login_popup = Element(browser, By.CLASS_NAME, "success-message")

    def click_sign_in_menu(self):
        self.sign_in_menu.click()

    def enter_email(self, email):
        self.email_input.enter_text(email)

    def enter_password(self, password):
        self.password_input.enter_text(password)

    def sign_in(self):
        self.sign_in_button.click()

    def verify_login(self):
        self.success_login_message.wait_until_visible()
        assert self.success_login_popup.get_attribute('class') == 'success-message'

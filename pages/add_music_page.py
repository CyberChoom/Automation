from webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class MusicPage:
    def __init__(self, browser):
        self.sign_in_menu = Element(browser, By.XPATH, "//b[contains(.,'Sign In')]")
        self.email_input = Element(browser, By.NAME, "username")
        self.password_input = Element(browser, By.NAME, "password")
        self.sign_in_button = Element(browser, By.XPATH, "//button[contains(.,'Sign In')]")
        self.username = Element(browser, By.XPATH, "//span[contains(.,'Kozmonot User ')]")

    def click_sign_in_menu(self):
        self.sign_in_menu.click()

    def enter_email(self, email):
        self.email_input.enter_text(email)

    def enter_password(self, password):
        self.password_input.enter_text(password)

    def sign_in(self):
        self.sign_in_button.click()

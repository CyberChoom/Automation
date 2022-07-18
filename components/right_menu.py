from webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class RightMenu:
    def __init__(self, browser):
        self.login_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[1]")
        self.registration_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[2]")
        self.forgotten_password_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[3]")
        self.my_account_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[4]")

    def click_login(self):
        self.login_btn.click()

    def click_registration(self):
        self.registration_btn.click()

    def click_forgotten_btn(self):
        self.forgotten_password_btn.click()

    def click_my_account(self):
        self.my_account_btn.click()

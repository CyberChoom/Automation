from webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class MusicPage:
    def __init__(self, browser):
        self.sign_in_menu = Element(browser, By.XPATH, "//b[contains(.,'Sign In')]")
        self.email_input = Element(browser, By.NAME, "username")
        self.password_input = Element(browser, By.NAME, "password")
        self.sign_in_button = Element(browser, By.XPATH, "//button[contains(.,'Sign In')]")
        self.username = Element(browser, By.XPATH, "//span[contains(.,'Kozmonot User ')]")
        self.cargo_bay = Element(browser, By.XPATH, "//span[contains(.,' Cargo Bay')]")
        self.add_new_product = Element(browser, By.XPATH, "//button[contains(.,'Add New Product')]")
        self.media = Element(browser, By.XPATH, "//button[contains(.,'Media')]")
        self.music = Element(browser, By.XPATH, "//button[contains(.,'Music')]")
        self.artist_name = Element(browser, By.XPATH, "//input[@name='artistName']")

    def click_sign_in_menu(self):
        self.sign_in_menu.click()

    def enter_email(self, email):
        self.email_input.enter_text(email)

    def enter_password(self, password):
        self.password_input.enter_text(password)

    def sign_in(self):
        self.sign_in_button.click()

    def verify_username(self):
        assert self.username.get_text() == "Kozmonot User "

    def open_music_page(self):
        self.cargo_bay.click()
        self.add_new_product.click()
        self.media.click()
        self.music.click()

from BDDBehave.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from BDDBehave.webelements.dropdown import Dropdown
import time


class MusicPage:
    def __init__(self, browser):
        self.time = time
        self.cargo_bay = Element(browser, By.XPATH, "//span[contains(.,'Cargo Bay')]")
        self.add_new_product = Element(browser, By.XPATH, "//button[contains(.,'Add New Product')]")
        self.media = Element(browser, By.XPATH, "//button[contains(.,'Media')]")
        self.music = Element(browser, By.XPATH, "//button[contains(.,'Music')]")
        self.artist_name = Element(browser, By.XPATH, "//input[@name='artistName']")
        self.album_name = Element(browser, By.XPATH, "//input[@name='albumName']")
        self.music_format = Dropdown(browser, By.NAME, "productFormat")
        self.quantity = Element(browser, By.XPATH, "//input[@name='quantity']")
        self.media_condition = Dropdown(browser, By.NAME, "condition")
        self.sleeve_condition = Dropdown(browser, By.NAME, "sleeveCondition")
        self.opening_price = Element(browser, By.XPATH, "//input[@name='openingPrice']")
        self.asking_price = Element(browser, By.XPATH, "//input[@name='askingPrice']")
        self.add_product_button = Element(browser, By.XPATH, "//button[contains(.,'Add Product')]")
        self.success_message = Element(browser, By.XPATH, "//div[contains(.,'New music product was created..')]")
        self.success_message_popup = Element(browser, By.CLASS_NAME, "success-message")
        self.number_of_all_products = Element(browser, By.XPATH, "//div[4]/div/ul/li/a/span")
        self.error = Element(browser, By.XPATH, "//span[contains(.,'This field is required.')]")

    def open_music_page(self):
        self.cargo_bay.click()
        self.add_new_product.click()
        self.media.click()
        self.music.click()

    def add_artist_name(self, name):
        self.artist_name.enter_text(name)

    def add_album_name(self, album):
        self.album_name.enter_text(album)

    def select_format(self, m_format):
        self.music_format.select_by_text(m_format)

    def add_quantity(self, number):
        self.quantity.enter_text(number)

    def select_media_condition(self, condition):
        self.media_condition.select_by_text(condition)

    def select_sleeve_condition(self, sleeve_condition):
        self.sleeve_condition.select_by_text(sleeve_condition)

    def add_opening_price(self, open_price):
        self.opening_price.enter_text(open_price)

    def add_asking_price(self, ask_price):
        self.asking_price.enter_text(ask_price)

    def add_product(self):
        self.add_product_button.click()

    def verify_adding_product(self):
        self.success_message.wait_until_visible()
        assert self.success_message_popup.get_attribute('class') == 'success-message'

    def verify_error(self):
        self.error.wait_until_present()
        assert self.error.get_text() == 'This field is required.'

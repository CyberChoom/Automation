from BDDBehave.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from BDDBehave.webelements.dropdown import Dropdown


class MusicPage:
    def __init__(self, browser):
        self.cargo_bay = Element(browser, By.XPATH, "//span[contains(.,' Cargo Bay')]")
        self.add_new_product = Element(browser, By.XPATH, "//button[contains(.,'Add New Product')]")
        self.media = Element(browser, By.XPATH, "//button[contains(.,'Media')]")
        self.music = Element(browser, By.XPATH, "//button[contains(.,'Music')]")
        self.artist_name = Element(browser, By.XPATH, "//input[@name='artistName']")
        self.album_name = Element(browser, By.XPATH, "//input[@name='albumName']")
        self.music_format = Dropdown(browser, By.XPATH, "//select[@name='productFormat']")
        self.quantity = Element(browser, By.XPATH, "//input[@name='quantity']")
        self.media_condition = Dropdown(browser, By.XPATH, "//select[@name='condition']")
        self.sleeve_condition = Dropdown(browser, By.XPATH, "//select[@name='sleeveCondition']")
        self.opening_price = Element(browser, By.XPATH, "//input[@name='openingPrice']")
        self.asking_price = Element(browser, By.XPATH, "//input[@name='askingPrice']")
        self.add_product = Element(browser, By.XPATH, "//button[contains(.,'Add Product')]")

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
        self.add_product.click()

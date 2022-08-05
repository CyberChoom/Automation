from webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class Header:
    def __init__(self, browser):
        self.my_account_btn = Element(browser, By.XPATH, "//a[@title='My Account']")
        self.my_account_dropdown = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']")
        self.register_btn = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']/li[1]")
        self.login_btn = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']/li[2]")
        self.wish_list_btn = Element(browser, By.ID, "wishlist-total")
        self.shopping_list_btn = Element(browser, By.XPATH, "//a[@title='Shopping Cart']")
        self.checkout_btn = Element(browser, By.XPATH, "//a[@title='Checkout']")
        self.currency_btn = Element(browser, By.ID, "form-currency")
        self.currency_dropdown = Element(browser, By.XPATH, "//*[@class= 'dropdown-menu']")
        self.currency_EUR = Element(browser, By.XPATH, "//*[@name= 'EUR']")
        self.currency_GBP = Element(browser, By.XPATH, "//*[@name= 'GBP']")
        self.currency_USD = Element(browser, By.XPATH, "//*[@name= 'USD']")
        self.logo = Element(browser, By.ID, "logo")
        # self.search = Element(browser, By.ID, "search") - does not work. Used search_field instead
        self.search_field = Element(browser, By.XPATH, "//*[@class= 'form-control input-lg']")
        self.search_button = Element(browser, By.XPATH, "//*[@class= 'fa fa-search']")

    def verify_logo_is_visible(self):
        return self.logo.wait_until_visible()

    def open_registration_form(self):
        self.my_account_btn.click()
        self.my_account_dropdown.wait_until_visible()
        self.register_btn.click()

    def open_login_page(self):
        self.my_account_btn.click()
        self.my_account_dropdown.wait_until_visible()
        self.login_btn.click()

    def change_currency(self, new_currency):
        self.currency_btn.click()
        self.currency_dropdown.wait_until_visible()
        if new_currency.lower() == "eur":
            self.currency_EUR.click()
        elif new_currency.lower() == "gbp":
            self.currency_GBP.click()
        else:
            self.currency_USD.click()

    def open_wishlist(self):
        self.wish_list_btn.click()

    def search_for(self, text):
        self.search_field.enter_text(text)
        self.search_button.click()

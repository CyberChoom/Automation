from webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class Footer:
    def __init__(self, browser):
        self.about_us_btn = Element(browser, By.XPATH, "//footer//a[text()='About Us']")
        self.delivery_information_btn = Element(browser, By.XPATH, "//footer//a[text()='Delivery Information']")
        self.privacy_policy_btn = Element(browser, By.XPATH, "//footer//a[text()='Privacy Policy']")
        self.terms_and_conditions_btn = Element(browser, By.XPATH, "//footer//a[text()='Terms & Conditions']")
        self.contact_us_btn = Element(browser, By.XPATH, "//footer//a[text()='Contact Us']")
        self.returns_btn = Element(browser, By.XPATH, "//footer//a[text()='Returns']")
        self.site_map_btn = Element(browser, By.XPATH, "//footer//a[text()='Site Map']")
        self.brands_btn = Element(browser, By.XPATH, "//footer//a[text()='Brands']")
        self.gift_certificates_btn = Element(browser, By.XPATH, "//footer//a[text()='Gift Certificates']")
        self.affiliates_btn = Element(browser, By.XPATH, "//footer//a[text()='Affiliates']")
        self.specials_btn = Element(browser, By.XPATH, "//footer//a[text()='Specials']")
        self.my_account_btn = Element(browser, By.XPATH, "//footer//a[text()='My Account']")
        self.order_history_btn = Element(browser, By.XPATH, "//footer//a[text()='Order History']")
        self.wish_list_btn = Element(browser, By.XPATH, "//footer//a[text()='Wish List']")
        self.newsletter_btn = Element(browser, By.XPATH, "//footer//a[text()='Newsletter']")

    def click_about_us(self):
        self.about_us_btn.click()

    def click_delivery_information(self):
        self.delivery_information_btn.click()

    def click_privacy_policy(self):
        self.privacy_policy_btn.click()

    def click_terms_and_conditions(self):
        self.terms_and_conditions_btn.click()

    def click_contact_us(self):
        self.contact_us_btn.click()

    def click_returns(self):
        self.returns_btn.click()

    def click_site_map(self):
        self.site_map_btn.click()

    def click_brands(self):
        self.brands_btn.click()

    def click_gift_certificates(self):
        self.gift_certificates_btn.click()

    def click_affiliates(self):
        self.affiliates_btn.click()

    def click_specials(self):
        self.specials_btn.click()

    def click_my_account(self):
        self.my_account_btn.click()

    def click_order_history(self):
        self.order_history_btn.click()

    def click_wish_list(self):
        self.wish_list_btn.click()

    def click_newsletter(self):
        self.newsletter_btn.click()

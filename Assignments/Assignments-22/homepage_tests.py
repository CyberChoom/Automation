from pages.home_page import HomePage
from webelements.browser import Browser
from webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By

URL = "https://cleveronly.com/brainbucket"


def test_opening_pcs():
    browser = Browser(URL, "firefox")
    home_page = HomePage(browser)
    home_page.show_pcs()
    section_title = Element(browser, By.XPATH, "//*[@id='content']/h2").get_text()
    assert section_title == "PC"
    item_available = Element(browser, By.PARTIAL_LINK_TEXT,
                             "https://cleveronly.com/brainbucket/index.php?route=product/product&path=")

    if item_available:
        pass
    else:
        no_products = Element(browser, By.XPATH, "//p[contains(.,'There are no products to list in this category.')]")
        assert no_products.get_text() == \
               'There are no products to list in this category.'

    browser.shutdown()


def test_opening_macs():
    browser = Browser(URL, "firefox")
    home_page = HomePage(browser)
    home_page.show_mac_desktops()
    section_title = Element(browser, By.XPATH, "//*[@id='content']/h2").get_text()
    assert section_title == "Mac"
    amount_of_items = 0
    item_available = Element(browser, By.PARTIAL_LINK_TEXT,
                             "https://cleveronly.com/brainbucket/index.php?route=product/product&path=")
    if item_available:
        amount_of_items += 1

    home_page.show_mac_desktops_dropdown()
    mac_page = Element(browser, By.XPATH, "//nav[@id='menu']/div[2]/ul/li/div/div/ul/li[2]/a").get_text()
    assert mac_page == f"Mac ({str(amount_of_items)})"

    browser.shutdown()


def test_opening_all_desktops():
    browser = Browser(URL, "firefox")
    home_page = HomePage(browser)
    home_page.show_all_desktops()
    section_title = Element(browser, By.XPATH, "//*[@id='content']/h2").get_text()
    assert section_title == "Desktops"

    browser.shutdown()


if __name__ == "__main__":
    test_opening_pcs()
    test_opening_macs()
    test_opening_all_desktops()


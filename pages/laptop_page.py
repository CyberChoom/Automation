from components.navigation_bar import NavigationBar
from components.header import Header
from components.right_menu import RightMenu
from webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class LaptopPage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.navbar = NavigationBar(browser)
        self.right_menu = RightMenu(browser)

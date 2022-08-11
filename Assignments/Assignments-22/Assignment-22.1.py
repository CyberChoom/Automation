from webelements.actions import Actions
from selenium.webdriver.common.by import By
from webelements.browser import Browser
from webelements.UIElement import UIElement as Element


URL = "https://cleveronly.com/practice"
browser = Browser(URL, "firefox")
actions = Actions(browser)
driver = browser.get_driver()

# Changing background color
change_background = Element(browser, By.ID, "card")
actions.double_click(change_background)
assert change_background.get_attribute('style') == "background-color: rgb(255, 179, 128);"

# Interacting with the input field
input_field = Element(browser, By.ID, "key_practice")
actions.click(input_field)
actions.send_keys('\ue007')
assert input_field.get_text("You pressed the key!")

# Interacting with the context menu
context_menu = Element(browser, By.ID, "context_menu")
change_color = Element(browser, By.XPATH, "//li[@onclick='changeColor()']")
change_font = Element(browser, By.XPATH, "//li[@onclick='changeFont()']")
open_website = Element(browser, By.XPATH, "//a")

# Changing color
actions.right_click(context_menu)
actions.click(change_color)
# Changing font
actions.right_click(context_menu)
actions.click(change_font)
# Verifying that color and font attributes were changed successfully
assert context_menu.get_attribute('style') == "background-color: rgb(204, 255, 245); font-weight: bold;"
# Opening the link in the context menu
actions.right_click(context_menu)
open_website.click()
# Sending ESC key to the page
actions.right_click(context_menu)
actions.send_keys('\ue00c')

browser.shutdown()

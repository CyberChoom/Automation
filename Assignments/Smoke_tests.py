# 7-17-2022    V
# Removed WebDriver - it's stored in browser.py
from selenium.webdriver.support.color import Color

# 6-11-2022    V
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 6-12-2022    V
from selenium.webdriver.support.select import Select

# 7-5-2022    V
from webelements.browser import Browser
from webelements.UIElement import UIElement as Element

# 7-14-2022    V
# Opening the browser and the website to be tested
browser = Browser("https://cleveronly.com/brainbucket/index.php?route=account/login", "firefox")
driver = browser.get_driver()
driver.maximize_window()  # maximizing the browser window

# Inputting password
password_input = Element(browser, By.XPATH, "//input[@id='input-password']")
password_input.enter_text("PassworD")

# 7-17-2022    V
# Adding WebDriverWait from browser.py

wb_wait = browser.get_wd_wait()

# 6-11-2022    V
# Testing 'Login' and 'Continue' buttons.
# 7-17-2022    V
# Updated code to use new class UIElement in places instead of find_element_by*

login_button = Element(browser, By.XPATH, "//input[@value='Login']").click()
new_registrant_button = Element(browser, By.XPATH, "//a[contains(text(), 'Continue')]").click()
register_account_sign = Element(browser, By.XPATH, "//h1[contains(.,'Register Account')]").wait_until_visible()

# 5-8-2022    V
# Input fields
# 7-17-2022    V
# Updated code to use new class UIElement in places instead of find_element_by*

firstname_field_class = Element(browser, By.XPATH, "//fieldset[@id='account']/div[2]").get_attribute("class")
# firstname_field_class = driver.find_element_by_xpath("//fieldset[@id='account']/div[2]").get_attribute("class")
assert "required" in firstname_field_class
firstname_input = Element(browser, By.ID, "input-firstname")
# firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.enter_text("Arnold")

lastname_field_class = Element(browser, By.XPATH, "//fieldset[@id='account']/div[3]").get_attribute("class")
assert "required" in lastname_field_class
lastname_input = Element(browser, By.ID, "input-lastname")
lastname_input.enter_text("Schwarzenegger")

email_field_class = Element(browser, By.XPATH, "//fieldset[@id='account']/div[4]").get_attribute("class")
assert "required" in email_field_class
email_input = Element(browser, By.ID, "input-email")
email_input.enter_text("test@cleveronly.com")

phone_field_class = Element(browser, By.XPATH, "//fieldset[@id='account']/div[5]").get_attribute("class")
assert "required" in phone_field_class
phone_input = Element(browser, By.ID, "input-telephone")
phone_input.enter_text("123-456-7890")

address_1_field_class = Element(browser, By.XPATH, "//fieldset[@id='address']/div[2]").get_attribute("class")
assert "required" in address_1_field_class
address_1_input = Element(browser, By.ID, "input-address-1")
address_1_input.enter_text("1 Infinite Loop")

city_field_class = Element(browser, By.XPATH, "//fieldset[@id='address']/div[4]").get_attribute("class")
assert "required" in city_field_class
city_input = Element(browser, By.ID, "input-city")
city_input.enter_text("Seattle")

password_field_class = Element(browser, By.XPATH, "//fieldset[3]/div").get_attribute("class")
assert "required" in password_field_class
password_input = Element(browser, By.ID, "input-password")
password_input.enter_text("youllneverguess")

password_confirm_field_class = Element(browser, By.XPATH, "//fieldset[3]/div[2]").get_attribute("class")
assert "required" in password_confirm_field_class
password_confirm_input = Element(browser, By.ID, "input-confirm")
password_confirm_input.enter_text("youllneverguess")

# 6-12-2022    V
# Selecting region
region_dropdown = driver.find_element(By.ID, "input-zone")
region_dropdown_select = Select(region_dropdown)
region_dropdown_select.select_by_visible_text("Alabama")

# Checking 'Privacy policy' checkbox
privacy_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='1']")
if not privacy_checkbox.is_selected():
    privacy_checkbox.click()

# Newsletter subscription - 'No' radio button activation
subscription = driver.find_element(By.XPATH, "//input[@type='radio' and @value='0']")
if not subscription.is_selected():
    subscription.click()

# 6-11-2022    V
# Adding WebDriverWait to 'Continue' button
continue_button = wb_wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Continue']")))

# 5-8-2022    V
# Verifying background-color of 'Continue' button
background_color = continue_button.value_of_css_property("background-color")
converted_background_color = Color.from_string(background_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'
continue_button.click()

# 6-11-2022    V
# Verification of proper functionality of 'My Account' menu, 'Login' and 'Register' buttons
# 7-17-2022
# Updated code to use new class UIElement in places instead of find_element_by*
account_btn = Element(browser, By.XPATH, "//a[@title='My Account']").click()
login_option = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']/li[2]").click()

assert driver.current_url == "https://cleveronly.com/brainbucket/index.php?route=account/login"

account_btn_wait = wb_wait.until(EC.presence_of_element_located((By.XPATH, "//a[@title='My Account']"))).click()
register_option = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']/li[1]").click()

assert driver.current_url == "https://cleveronly.com/brainbucket/index.php?route=account/register"

browser.shutdown()

from selenium import webdriver
from selenium.webdriver.support.color import Color

driver = webdriver.Firefox(executable_path='drivers/geckodriver')
driver.get("https://techskillacademy.net/brainbucket/index.php?route=account/login")
driver.maximize_window()  # maximizing the browser window

login = driver.find_element_by_xpath("//a[contains(text(),'Login')]")
password_input = driver.find_element_by_xpath("//input[@id='input-password']")
password_input.send_keys("PassworD")
login_button = driver.find_element_by_xpath("//input[@value='Login']")
login_button.click()

new_registrant_button = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")
new_registrant_button.click()


# Input fields

firstname_field_class = driver.find_element_by_xpath("//fieldset[@id='account']/div[2]").get_attribute("class")
assert "required" in firstname_field_class
firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.send_keys("Arnold")

lastname_field_class = driver.find_element_by_xpath("//fieldset[@id='account']/div[3]").get_attribute("class")
assert "required" in lastname_field_class
lastname_input = driver.find_element_by_id("input-lastname")
lastname_input.send_keys("Schwarzenegger")

email_field_class = driver.find_element_by_xpath("//fieldset[@id='account']/div[4]").get_attribute("class")
assert "required" in email_field_class
email_input = driver.find_element_by_id("input-email")
email_input.send_keys("test@cleveronly.com")

phone_field_class = driver.find_element_by_xpath("//fieldset[@id='account']/div[5]").get_attribute("class")
assert "required" in phone_field_class
phone_input = driver.find_element_by_id("input-telephone")
phone_input.send_keys("123-456-7890")

address_1_field_class = driver.find_element_by_xpath("//fieldset[@id='address']/div[2]").get_attribute("class")
assert "required" in address_1_field_class
address_1_input = driver.find_element_by_id("input-address-1")
address_1_input.send_keys("1 Infinite Loop")

city_field_class = driver.find_element_by_xpath("//fieldset[@id='address']/div[4]").get_attribute("class")
assert "required" in city_field_class
city_input = driver.find_element_by_id("input-city")
city_input.send_keys("Seattle")

password_field_class = driver.find_element_by_xpath("//fieldset/div").get_attribute("class")
assert "required" in password_field_class
password_input = driver.find_element_by_id("input-password")
password_input.send_keys("youllneverguess")

password_confirm_field_class = driver.find_element_by_xpath("//fieldset/div").get_attribute("class")
assert "required" in password_confirm_field_class
password_confirm_input = driver.find_element_by_id("input-confirm")
password_confirm_input.send_keys("youllneverguess")


# Verifying background-color of Continue button

continue_button = driver.find_element_by_xpath("//input[@value='Continue']")
background_color = continue_button.value_of_css_property("background-color")
converted_background_color = Color.from_string(background_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'
continue_button.click()



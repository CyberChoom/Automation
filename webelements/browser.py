from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


class Browser:
    """
    This class is wrapper around Selenium driver
    """
    def __init__(self, url, browser_name=""):
        # Added exception handling
        try:
            if browser_name.lower() == "firefox":
                self.driver = webdriver.Firefox(executable_path='C:/Users/user/Desktop/Automation/drivers/geckodriver')
            else:
                self.driver = webdriver.Chrome(executable_path='C:/Users/user/Desktop/Automation/drivers/chromedriver')
        except WebDriverException:
            print("The executable path to the driver is incorrect.")
            raise

        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # by default 10, but we can add this like a parameter

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()

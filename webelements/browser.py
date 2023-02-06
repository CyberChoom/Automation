from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


class Browser:
    """
    This class is wrapper around Selenium driver
    """
    def __init__(self, url, browser_name="", time_wait=10, width="", height=""):
        # Added exception handling
        try:
            if browser_name.lower() == "firefox":
                options = webdriver.FirefoxOptions()
                options.add_argument(f"--width={width}")
                options.add_argument(f"--height={height}")

                firefox_profile = webdriver.FirefoxProfile()
                firefox_profile.set_preference("browser.urlbar.showPopup", True)

                self.driver = webdriver.Firefox(firefox_profile=firefox_profile,
                                                executable_path='C:/Users/user/Desktop/Automation/drivers/geckodriver',
                                                options=options)
                if width or height:
                    pass
                else:
                    self.driver.maximize_window()

            elif browser_name.lower() == "chrome":
                options = webdriver.ChromeOptions()
                options.add_argument(f"--window-size={width},{height}")
                options.add_argument("--disable-popup-blocking")
                options.add_experimental_option("excludeSwitches", ['enable-automation'])

                self.driver = webdriver.Chrome(executable_path='C:/Users/user/Desktop/Automation/drivers/chromedriver',
                                               options=options)
                if width or height:
                    pass
                else:
                    self.driver.maximize_window()
        except WebDriverException:
            print("The executable path to the driver is incorrect.")
            raise

        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        # self.driver.maximize_window()
        self.driver.implicitly_wait(time_wait)  # by default 10, but we can add this like a parameter

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()

class IFrame:
    def __init__(self, browser):
        self.driver = browser.get_driver()

    def switch_to_iframe(self, iframe):
        self.driver.switch_to.frame(iframe)

    def default_content(self):
        self.driver.switch_to.default_content()

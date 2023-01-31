import time


class Alert:
    def __init__(self, browser):
        self.driver = browser.get_driver()
        self.switch_to_alert = self.driver.switch_to.alert

    def accept_alert(self):
        time.sleep(1)
        self.switch_to_alert.accept()
        time.sleep(1)

    def dismiss_alert(self):
        time.sleep(1)
        self.switch_to_alert.dismiss()
        time.sleep(1)

    def type_and_accept(self, name):
        self.switch_to_alert.send_keys(name)
        self.accept_alert()

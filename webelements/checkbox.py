from webelements.UIElement import UIElement as Element


class Checkbox(Element):
    def __init__(self, browser, by, locator):
        super().__init__(browser, by, locator)
        self.check_b = self.get_element()

    def privacy_checkbox(self):
        if not self.check_b.is_selected():
            self.click()

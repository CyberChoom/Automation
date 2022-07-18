from webelements.UIElement import UIElement as Element


class Radiobutton(Element):
    def __init__(self, browser, by, locator):
        super().__init__(browser, by, locator)
        self.radio_b = self.get_element()

    def newsletter(self):
        if not self.radio_b.is_selected():
            self.click()

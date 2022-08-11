from components.navigation_bar import NavigationBar
from components.header import Header


class HomePage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.navbar = NavigationBar(browser)

    def show_all_desktops(self):
        self.navbar.show_all_desktops()

    def show_pcs(self):
        self.navbar.show_pcs()

    def show_mac_desktops(self):
        self.navbar.show_mac_desktops()

    def show_all_laptops(self):
        self.navbar.show_all_laptops()

    def show_windows_laptops(self):
        self.navbar.show_windows_laptops()

    def show_all_components(self):
        self.navbar.show_all_components()

    def show_mice(self):
        self.navbar.show_mice()

    def show_monitors(self):
        self.navbar.show_monitors()

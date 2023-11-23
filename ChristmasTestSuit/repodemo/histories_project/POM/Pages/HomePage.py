from selenium.webdriver.common.by import By

from ChristmasTestSuit.repodemo.histories_project.POM.lib.helpers import Helpers


class HomePage(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    christmas_start = (By.LINK_TEXT, 'How Did Christmas Start?')
    saturnalia_christmas = (By.LINK_TEXT, 'Saturnalia and Christmas')

    def click_on_christmas_start(self):
        self.find_and_click(self.christmas_start)

    def click_on_saturnalia_christmas(self):
        self.find_and_click(self.saturnalia_christmas)

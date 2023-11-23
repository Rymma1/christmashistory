from selenium.webdriver.common.by import By

from ChristmasTestSuit.repodemo.histories_project.POM.lib.helpers import Helpers


class SaturnaliaChristmas(Helpers):
    saturnalia_christmas_header = (By.ID, 'saturnalia-and-christmas')

    def assert_saturnalia_christmas_header(self, header_text='Saturnalia and Christmas '):
        actual_text = self.find(self.saturnalia_christmas_header, get_text=True)
        assert actual_text == header_text

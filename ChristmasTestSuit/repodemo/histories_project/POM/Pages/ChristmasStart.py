from selenium.webdriver.common.by import By

from ChristmasTestSuit.repodemo.histories_project.POM.lib.helpers import Helpers


class ChristmasStart(Helpers):
    christmas_start_header = (By.ID, 'how-did-christmas-start')

    def assert_christmas_start_header(self, header_text = 'How Did Christmas Start?'):
        actual_text = self.find(self.christmas_start_header, get_text=True)
        assert actual_text == header_text




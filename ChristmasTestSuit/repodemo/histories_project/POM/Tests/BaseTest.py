import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:
    def check_assert_christmas_headers(self):
        self.homepage.click_on_christmas_start()
        self.christmasstart.assert_christmas_start_header()
        self.helpers.driver_back()
        self.homepage.click_on_saturnalia_christmas()
        self.saturnaliachristmas.assert_saturnalia_christmas_header()

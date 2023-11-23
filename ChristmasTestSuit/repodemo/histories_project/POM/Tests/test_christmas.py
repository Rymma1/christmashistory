from ChristmasTestSuit.repodemo.histories_project.POM.Tests.BaseTest import BaseTest


class TestChristmas(BaseTest):
    def test_christmas_new(self):
        self.check_assert_christmas_headers()

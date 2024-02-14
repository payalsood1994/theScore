import pytest
import allure
from pages.android_pages.welcome_page import WelcomePage


@allure.title("Welcome Page Test")
@pytest.mark.usefixtures("setup")
class TestWelcomePage:

    @allure.step("test_welcome_page")
    @allure.description("Welcome Page Test")
    def test_welcome_page(self):
        welcomePage = WelcomePage(self.driver)
        welcomePage.check_welcome_page_elements()


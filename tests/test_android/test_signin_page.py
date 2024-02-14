import pytest
import allure
from pages.android_pages.signin_page import LoginPage
from pages.android_pages.welcome_page import WelcomePage
from utils.data import TestData


@allure.title("Login Page Test")
@pytest.mark.usefixtures("setup")
class TestLoginPage:

    @allure.step("test_login_page_ui")
    @allure.description("Login Page Test ui elements")
    def test_login_page_ui(self):
        welcomePage = WelcomePage(self.driver)
        loginPage = LoginPage(self.driver)
        welcomePage.click_sign_in_button()
        loginPage.check_login_page_elements()

    @allure.step("test_login")
    @allure.description("Verify the login functionality")
    def test_login(self):
        welcomePage = WelcomePage(self.driver)
        loginPage = LoginPage(self.driver)
        welcomePage.click_sign_in_button()
        loginPage.login_method(TestData.EMAIL, TestData.PASSWORD)





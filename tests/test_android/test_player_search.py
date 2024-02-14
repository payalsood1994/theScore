import pytest
import allure
from pages.android_pages.welcome_page import WelcomePage
from pages.android_pages.signin_page import LoginPage
from pages.android_pages.home_page import HomePage
from pages.android_pages.search_page import SearchPage
from pages.android_pages.player_page import PlayerPage
from utils import util
from utils.locators.android_locators import *


@allure.title("Player Search Text")
@pytest.mark.usefixtures("setup")
class TestPlayerSearch:

    @allure.step("test_player_search")
    @allure.description("Player Search Test")
    def test_player_search(self):
        welcomePage = WelcomePage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage = HomePage(self.driver)
        searchPage = SearchPage(self.driver)
        playersPage = PlayerPage(self.driver)
        welcomePage.click_sign_in_button()
        loginPage.login_method(TestData.EMAIL, TestData.PASSWORD)
        util.dismiss_model(self.driver)
        homePage.click_on_search_bar()
        searchPage.enter_text_on_search_bar(TestData.PLAYER_NAME)
        searchPage.click_on_sub_navigation_for_search("PLAYERS")
        searchPage.select_player(TestData.PLAYER_NAME)
        playersPage.verify_player_page()
        playersPage.click_on_info_sub_navigation()
        util.wait_for_element_and_click(self.driver, CommonLocator.NAVIGATE_UP_BUTTON, 10)
        searchPage.verify_search_page()
        util.wait_for_element_and_click(self.driver, CommonLocator.NAVIGATE_UP_BUTTON, 10)
        homePage.verify_home_page()





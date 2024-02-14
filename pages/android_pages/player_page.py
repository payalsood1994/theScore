import time
from utils import util
from seleniumpagefactory.Pagefactory import PageFactory
from appium.webdriver.common.touch_action import TouchAction
from utils.locators.android_locators import *


class PlayerPage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.player_page_locator = PlayersPageLocators

    def verify_player_page(self):
        """
        This method will verify the elements of player screen and also matches them with expected values
        :return:
        """

        assertion_failures = []
        util.is_element_present(self.driver, self.player_page_locator.PLAYER_IMAGE_ICON, 10)
        player_name = util.get_text_from_element(self.driver, self.player_page_locator.PLAYER_TEXT_NAME)
        if not player_name == TestData.PLAYER_NAME:
            assertion_failures.append(
                "Player Name %s in Players screen doesn't match searched player %s"
                % (player_name, TestData.PLAYER_NAME)
            )
        player_description = util.get_text_from_element(self.driver, self.player_page_locator.PLAYER_SUBTITLE)
        expected_player_description = "#" + str(TestData.PLAYER_RANK) + " / " + TestData.PLAYER_POSITION
        if not player_description == expected_player_description:
            assertion_failures.append(
                "Player Description %s in Players screen doesn't match searched player description %s"
                % (player_description, expected_player_description)
            )
        util.is_element_present(self.driver, self.player_page_locator.PLAYER_NEWS_SUBNAV, 10)
        util.is_element_present(self.driver, self.player_page_locator.PLAYER_INFO_SUBNAV, 10)

    def click_on_info_sub_navigation(self):
        """
        Click on Info sub Navigation on Players Screen
        :return:
        """
        util.wait_for_element_and_click(self.driver,self.player_page_locator.PLAYER_INFO_SUBNAV, 10)

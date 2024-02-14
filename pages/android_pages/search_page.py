from seleniumpagefactory.Pagefactory import PageFactory
from utils.locators.android_locators import *
from utils import util


class SearchPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.search_page_locator = SearchPageLocators

    def enter_text_on_search_bar(self, searchtext):
        """
        Enters text on search bar
        :param searchtext:
        :return:
        """
        util.wait_for_element_and_send_keys(self.driver,self.search_page_locator.SEARCH_TEXT, searchtext, 10)

    def click_on_sub_navigation_for_search(self, subNav):
        """
        This function will click on sub Navigation pages for the search
        :return:
        """
        if subNav == "All":
            util.wait_for_element_and_click(self.driver,self.search_page_locator.ALL_SUBNAV, 10)
        elif subNav == "TEAMS":
            util.wait_for_element_and_click(self.driver,self.search_page_locator.TEAMS_SUBNAV, 10)
        elif subNav == "PLAYERS":
            util.wait_for_element_and_click(self.driver,self.search_page_locator.PLAYER_SUBNAV, 10)
        elif subNav == "NEWS":
            util.wait_for_element_and_click(self.driver,self.search_page_locator.NEWS_SUBNAV, 10)

    def select_player(self, player_name):
        """
        This function will select the correct player from the search results
        :param player_name:
        :return:
        """
        util.wait_for_element_and_click(self.driver, self.search_page_locator.PLAYER_SEARCH_RESULT,10)

    def verify_search_page(self):
        """
        This function will verify the elements of search screen
        :return:
        """
        util.is_element_present(self.driver, self.search_page_locator.SEARCH_TEXT, 10)
        util.is_element_present(self.driver, self.search_page_locator.ALL_SUBNAV, 10)
        util.is_element_present(self.driver, self.search_page_locator.TEAMS_SUBNAV, 10)
        util.is_element_present(self.driver, self.search_page_locator.PLAYER_SUBNAV, 10)
        util.is_element_present(self.driver, self.search_page_locator.NEWS_SUBNAV, 10)




import time
from utils import util
from seleniumpagefactory.Pagefactory import PageFactory
from appium.webdriver.common.touch_action import TouchAction
from utils.locators.android_locators import *


class WelcomePage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.welcome_page_locator = WelcomePageLocator

    def check_welcome_page_elements(self):
        """
        This method checks if all the elements on the welcome page are visible
        :return:
        """
        time.sleep(10)
        util.is_element_present(self.driver, self.welcome_page_locator.SIGNIN_TEXT, 10)
        util.is_element_present(self.driver, self.welcome_page_locator.GET_STARTED_BUTTON, 10)
        util.is_element_present(self.driver, self.welcome_page_locator.SCORE_ICON, 10)
        util.is_element_present(self.driver, self.welcome_page_locator.WELCOME_TEXT, 10)
        util.is_element_present(self.driver, self.welcome_page_locator.APP_EXPERIENCE_TEXT, 10)
        util.is_element_present(self.driver, self.welcome_page_locator.TERMS_TEXT, 10)

    def click_sign_in_button(self):
        """
       This method will click on Login button on the score app
       :return:
       """
        time.sleep(10)
        ele = util.wait_for_element_present(self.driver,self.welcome_page_locator.SIGNIN_TEXT,30)
        y = ele.location
        x1 = y.get("x")
        y1 = y.get("y")
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        x2 = (width+x1)/2
        TouchAction(self.driver).tap(None, x2+5, y1+5, 1).perform()
        time.sleep((5))

    def click_get_started_button(self):
        """
       This method will click on GET STARTED button on the score app
       :return:
       """
        util.wait_for_element_and_click(self.driver, self.welcome_page_locator.GET_STARTED_BUTTON, 10)



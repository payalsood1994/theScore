import datetime
import inspect
import time
from pathlib import Path
from seleniumpagefactory.Pagefactory import PageFactory
from appium.webdriver.common.appiumby import AppiumBy
from utils import util
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.locators.android_locators import *
from utils.common import get_logger
from utils.data import TestData


class LoginPage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.login_page_locator = LoginPageLocator

    def check_login_page_elements(self):
        """
        This method checks if all the elements on the Log In Page are visible
        :return:
        """
        util.is_element_present(self.driver, LoginPageLocator.EMAIL_INPUT_FIELD, 10)
        util.is_element_present(self.driver, LoginPageLocator.PASSWORD_INPUT_FIELD, 10)
        util.is_element_present(self.driver, LoginPageLocator.PASSWORD_EYE_ICON, 10)
        util.is_element_present(self.driver, LoginPageLocator.LOGIN_BUTTON, 10)
        util.is_element_present(self.driver, LoginPageLocator.FORGOT_PASSWORD_LINK, 10)
        util.is_element_present(self.driver, LoginPageLocator.TERMS_OF_USE_TEXT, 10)

    def login_method(self, email, password):
        """
       This method will enter the email and password for login page
       :return:
       """
        util.wait_for_element_and_send_keys(self.driver, LoginPageLocator.EMAIL_INPUT_FIELD, email, 3)
        util.wait_for_element_and_send_keys(self.driver, LoginPageLocator.PASSWORD_INPUT_FIELD, password, 3)
        util.wait_for_element_and_click(self.driver, LoginPageLocator.LOGIN_BUTTON, 3)



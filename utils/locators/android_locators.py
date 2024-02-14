from selenium.webdriver.common.by import By
from utils.data import TestData


class CommonLocator(object):
    DISMISS_MODEL = "id:com.fivemobile.thescore:id/dismiss_modal"
    TITLE_TEXT_VIEW = "id:com.fivemobile.thescore:id/titleTextView"
    NAVIGATE_UP_BUTTON = "xpath://android.widget.ImageButton[@content-desc='Navigate up']"


class WelcomePageLocator(object):
    SIGNIN_TEXT = "id:com.fivemobile.thescore:id/txt_sign_in"
    GET_STARTED_BUTTON = "id:com.fivemobile.thescore:id/btn_primary"
    SCORE_ICON = "id:com.fivemobile.thescore:id/icon_welcome"
    WELCOME_TEXT = "id:com.fivemobile.thescore:id/txt_welcome"
    APP_EXPERIENCE_TEXT = "id:com.fivemobile.thescore:id/txt_app_exp"
    TERMS_TEXT = "id:com.fivemobile.thescore:id/txt_terms"


class LoginPageLocator(object):
    EMAIL_INPUT_FIELD = "id:com.fivemobile.thescore:id/email_input_edittext"
    PASSWORD_INPUT_FIELD = "id:com.fivemobile.thescore:id/password_input_edittext"
    PASSWORD_EYE_ICON = "id:com.fivemobile.thescore:id/text_input_end_icon"
    LOGIN_BUTTON = "id:com.fivemobile.thescore:id/login_button"
    FORGOT_PASSWORD_LINK = "id:om.fivemobile.thescore:id/forgot_password"
    TERMS_OF_USE_TEXT = "id:com.fivemobile.thescore:id/terms_of_use_privacy_policy"


class HomePageLocators(object):
    SEARCH_TEXT_VIEW = "id:com.fivemobile.thescore:id/search_bar_text_view"
    NEWS_NAV_PAGE = "id:com.fivemobile.thescore:id/navigation_news"
    SCORES_NAV_PAGE = "id:com.fivemobile.thescore:id/navigation_scores"
    FAVORITES_NAV_PAGE = "id:com.fivemobile.thescore:id/navigation_favorites"
    BET_NAV_PAGE = "id:com.fivemobile.thescore:id/navigation_discover"
    LEAGUES_NAV_PAGE = "id:com.fivemobile.thescore:id/navigation_leagues"


class SearchPageLocators(object):
    SEARCH_TEXT = "id:com.fivemobile.thescore:id/search_src_text"
    ALL_SUBNAV = "xpath://android.widget.LinearLayout[@content-desc='All']"
    TEAMS_SUBNAV ="xpath://android.widget.LinearLayout[@content-desc='Teams']"
    PLAYER_SUBNAV ="xpath://android.widget.LinearLayout[@content-desc='Players']"
    NEWS_SUBNAV ="xpath://android.widget.LinearLayout[@content-desc='News']"
    PLAYER_LEAGUE = TestData.PLAYER_LEAGUE
    PLAYER_NAME = TestData.PLAYER_NAME
    PLAYER_SEARCH_RESULT = "xpath://android.widget.TextView[@text='"+ PLAYER_NAME + " (" + PLAYER_LEAGUE + ")']"


class PlayersPageLocators(object):
    PLAYER_IMAGE_ICON = "id:com.fivemobile.thescore:id/player_headshot_image_view"
    PLAYER_TEXT_NAME = "id:com.fivemobile.thescore:id/txt_player_name"
    PLAYER_SUBTITLE = "id:com.fivemobile.thescore:id/detail_subtitle"
    PLAYER_NEWS_SUBNAV = "xpath://android.widget.LinearLayout[@content-desc='News']"
    PLAYER_INFO_SUBNAV = "xpath://android.widget.LinearLayout[@content-desc='Info']"



import pytest
from pages.login_page import LoginPage
from pages.login_dashboard_page import LoginDashboardPage

# Constants declaration
#Main test URL
URL = "https://demo.applitools.com/"


@pytest.fixture
def login_page(browser):
    browser.get(URL)    
    return LoginPage(browser)

@pytest.mark.BAT
def test_verify_icons(login_page, logger):
    
    assert login_page.get_element(login_page.locators.TWITTER_ICON).is_displayed()
    assert login_page.get_element(login_page.locators.INSTA_ICON).is_displayed()
    assert login_page.get_element(login_page.locators.FACEBOOK_ICON).is_displayed()

    logger.log(f"Test |{__name__}| passed")


@pytest.mark.BAT
def test_login(login_page, logger, browser):
    print(f'\n------{__name__}------')

    login_page.enter_username()
    login_page.enter_password()
    login_page.check_remember_box()
    login_page.click_sigin()

    login_dashboard_page = LoginDashboardPage(browser);
    assert login_dashboard_page.get_element(login_dashboard_page.locators.LOGGEDUSERNAME).text == "Jack Gomez"

    logger.log(f"Test |{__name__}| passed")

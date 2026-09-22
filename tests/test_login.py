from pages.login_page import LoginPage
# Constants declaration
#Main test URL
URL = "https://demo.applitools.com/"
#API test URL
API_URL = "https://api.duckduckgo.com/"

def test_login(browser):
    browser.get(URL)
    login_page = LoginPage(browser)

    login_page.enter_username()
    login_page.enter_password()
    login_page.click_sigin()

    assert login_page.get_page_title() == "ACME demo app"
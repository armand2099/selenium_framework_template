import time
import pytest_html
from common.common_functions import Common, Rest

# Constants declaration
#Main test URL
URL = "https://www.google.com"
#API test URL
API_URL = "https://api.duckduckgo.com/"

def test_navigate(browser, extras):
    browser.get(URL)
    common = Common(browser)
    

    print(f"Page title: {common.get_page_title()}")
    print(f"Page URL: {common.get_page_url()}")
    common.log("Page Opened", extras)
    #time.sleep(1)

def test_api(browser, extras):
    rest = Rest(API_URL)
    browser.get(API_URL)
    common = Common(browser)

    response = rest.rest_get("Selenium")

    common.log(f"Response: {response}", extras)
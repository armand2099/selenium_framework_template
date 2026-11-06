import tempfile

import pytest
import os
import json
from typing import Generator
from pathlib import Path
import datetime
from requests import options
from requests import options
from selenium import webdriver
from utils.logger import Loggin
from pages.google_acc_page import GoogleAccPage
import auth.google_creds as creds
from selenium.webdriver.remote.webdriver import WebDriver

#Variable declaration
HEADLESS = False
IMPLICIT_WAIT = 10
image_name = f"report_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
file_name = os.path.join(os.getcwd(), "Reports", "screenshots", image_name)


#-----------------------------------------Multiple browsers implementation-----------------------------------------

# Add custom command-line argument to selenium
def pytest_addoption(parser):
    '''Declares cli argument'''
    parser.addoption(
        "--browser-type", 
        action="store", 
        default="Chrome", 
        help="Browser type to run tests on: Chrome, Firefox"
    )

@pytest.fixture(scope="session")
def selected_browser_name(request) -> str:
    """Gets the browser type from the command line."""
    return request.config.getoption("--browser-type")

class BrowserFactory:
    @staticmethod
    def get_browser(browser_name: str) -> WebDriver:

        if browser_name == "Chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-blink-features=AutomationControlled")
            if HEADLESS:
                options.add_argument("--headless=new")
            return webdriver.Chrome(options=options)

        if browser_name == "Firefox":
            options = webdriver.FirefoxOptions()
            options.set_preference("layers.acceleration.disabled", True)
            options.set_preference("gfx.webrender.software", True)
            if HEADLESS:
                options.add_argument("--headless")            
            return webdriver.Firefox(options=options)

        raise ValueError(f"Unsupported browser type: '{browser_name}'")

@pytest.fixture(scope="session")
def browser(selected_browser_name) -> Generator[WebDriver, None, None]:

    # Use the Factory to get the correct browser dynamically
    b = BrowserFactory.get_browser(selected_browser_name)
    print(f"Browser: {selected_browser_name}")

    # Make its calls wait up 10 seconds for elements to appear
    b.implicitly_wait(IMPLICIT_WAIT)

    # Maximise Chrome window
    b.maximize_window()

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()

#-----------------------------------------Multiple browsers implementation-----------------------------------------

#-------------------------------------------Authentication state session-------------------------------------------

# Create the session-scoped authentication state
@pytest.fixture(scope="function")
def browser_auth(browser: WebDriver) -> Generator[WebDriver, None, None]:
    '''Authenticates and stores authentication state'''

    state_file = Path("auth/state.json").resolve()

    browser.get("https://accounts.google.com/")

    if state_file.is_file():
        with open(state_file, "r") as f:
            cookies = json.load(f)

        for cookie in cookies:
            try:
                browser.add_cookie(cookie)
            except Exception as e:
                print(f"Error adding cookie: {cookie}. Error: {e}")  

    browser.get("https://accounts.google.com/")
    google_acc_page = GoogleAccPage(browser)

    if browser.title == "Sign in - Google Accounts":
        google_acc_page.enter_email(creds.EMAIL)
        google_acc_page.click_next_button()
        google_acc_page.enter_password(creds.PASSWORD)
        google_acc_page.click_next_button()
    
        # Wait for navigation or a specific selector to confirm successful login
        print(f"Page title: {google_acc_page.get_page_title()}")
        
        # Save storage state to an in-memory dictionary (or a file string)
        state = browser.get_cookies()
        with open(state_file, "w") as f:
            json.dump(state, f, indent=2)

    yield state

    browser.close()

#-------------------------------------------Authentication state session-------------------------------------------

#-------------------------------------------Report Fixtures-------------------------------------------
#Logger fixture
@pytest.fixture(scope="function")
def logger(browser, extras):
    '''Logs messages and screenshots to html report'''
    return Loggin(browser, extras)

#Logger fixture for authenticated session
@pytest.fixture(scope="function")
def logger_auth(browser_auth, extras):
    '''Logs messages and screenshots to html report'''
    return Loggin(browser_auth, extras)


@pytest.hookimpl (hookwrapper=True)
def pytest_runtest_makereport (item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr (report, "extra", [])
    xfail = False
    if report.when == "call" or report.when == 'setup':
        xfail = hasattr(report, "wasxfail")
    if (report.skipped and xfail) or (report.failed and not xfail):
        # add the screenshots to the html report
        extra.append(pytest_html.extras.png(file_name))
    report.extra = extra
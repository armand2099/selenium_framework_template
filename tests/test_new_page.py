import pytest
from selenium.webdriver.common.by import By
from pages.new_window_page import NewWindowPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.window import WindowTypes
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

WINDOWS_URL = "https://demoqa.com/browser-windows"
WINDOWSTEXT = "Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization."

@pytest.fixture
def new_windows_page(browser):
    browser.get(WINDOWS_URL)    
    return NewWindowPage(browser)

@pytest.mark.TAB
def test_new_tab(new_windows_page: NewWindowPage, logger):
    new_tab = new_windows_page.new_page(new_windows_page.new_tab_button)
    new_tab_header = new_tab.find_element(By.CSS_SELECTOR, '#sampleHeading')
    assert new_tab_header.text == 'This is a sample page'
    logger.log(f"New Tab opened: {new_tab_header.text}")
    new_windows_page.close_window()

@pytest.mark.TAB
def test_new_window(new_windows_page: NewWindowPage, logger):
    new_window =  new_windows_page.new_page(new_windows_page.new_window_button)
    new_window_header =  new_window.find_element(By.CSS_SELECTOR,'#sampleHeading')
    assert new_window_header.text == 'This is a sample page'
    logger.log(f"New Window opened: {new_window_header.text}")
    new_windows_page.close_window()

@pytest.mark.TAB
def test_open_tabs_manually(browser, logger, new_windows_page):
    original_handles = browser.window_handles

    browser.switch_to.new_window(WindowTypes.TAB)
    WebDriverWait(browser, 10).until(EC.new_window_is_opened(original_handles))
    tab1 = next(handle for handle in browser.window_handles if handle not in original_handles)
    browser.get('https://google.com')
    logger.log(f"Page | {browser.title}  | Opened")

    original_handles = browser.window_handles

    browser.switch_to.new_window(WindowTypes.TAB)
    WebDriverWait(browser, 10).until(EC.new_window_is_opened(original_handles))
    tab2 = next(handle for handle in browser.window_handles if handle not in original_handles)
    browser.get('https://playwright.dev')
    logger.log(f"Page | { browser.title } | Opened")

    browser.switch_to.window(tab1)
    browser.find_element(By.NAME, "q").send_keys('Playwright')
    new_windows_page.random_wait()
    browser.find_element(By.NAME, "q").send_keys(Keys.RETURN)
    logger.log("Search completed")
    browser.close()

    browser.switch_to.window(tab2)
    assert browser.title == "Fast and reliable end-to-end testing for modern web apps | Playwright"
    logger.log("Title validated")
    browser.close()
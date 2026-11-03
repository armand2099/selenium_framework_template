from pages.base_page import BasePage
from pages.new_window_page_locators import PageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 10


class NewWindowPage(BasePage):
    '''
    NewWindowPage Page methods
    '''

    def __init__(self, browser):
        '''
        Initialize NewWindowPage class
        '''
        super().__init__(browser)
        self.browser = browser
        self.locators = PageLocators()

        self.new_tab_button = self.get_element(self.locators.new_tab_button)
        self.new_window_button = self.get_element(self.locators.new_window_button)
        self.new_window_msg_button = self.get_element(self.locators.new_window_msg_button)

    def new_page(self, page_button: WebElement) -> WebDriver:
        '''
        Clicks the required button, waits for a new browser window/tab to open,
        switches to it and returns the webdriver instance.
        '''
        original_handles = self.browser.window_handles

        self.browser.switch_to.window(original_handles[0])
        page_button.click()

        WebDriverWait(self.browser, TIMEOUT).until(
            lambda driver: len(self.browser.window_handles) > len(original_handles)
        )

        new_handle = next(
            handle for handle in self.browser.window_handles if handle not in original_handles
        )
        self.browser.switch_to.window(new_handle)
        WebDriverWait(self.browser, TIMEOUT).until(
                    EC.new_window_is_opened(original_handles)
                )
        '''
        WebDriverWait(self.browser, TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        '''

        return self.browser

    def close_window(self):
        '''
        Closes the current window and switches back to the original window.
        '''
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])
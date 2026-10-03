from utils.logging import Loggin
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    '''
    Class containing functions common to the whole project
    '''
    # Constants declaration

    def __init__(self, browser: Chrome):
        '''
        Initialize the browser and navigates to the project page
        The url parameter can be overide
        '''
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def get_page_title(self) -> str:
        '''
        Returns the current page tittle
        '''
        page_title = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "title")))
        page_title = self.browser.title

        return page_title

    def get_page_url(self) -> str:
        '''
        Returns the current page URL
        '''
        page_url = self.browser.current_url

        print(f"Current page URL: {page_url}")

        return page_url

    def test_explicit_waits(self) -> None:
        '''
        Explicit wait example
        '''
        try:
            element = Chrome(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.ID, "[Element]"))
            )
        finally:
            log.logging(element[0].text)

    def click_element(self, locator: tuple) -> None:
        '''
        Clicks on an element
        '''
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
import random
import time
from utils.logger import Loggin
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    '''
    Class containing functions common to the whole project
    '''
    # Constants declaration

    def __init__(self, browser: Chrome | Firefox, timeout: int = 10):
        '''
        Initialize the browser and navigates to the project page
        The url parameter can be overide
        '''
        self.browser = browser
        self.wait = WebDriverWait(self.browser, timeout)

    def get_element(self, locator: tuple) -> WebElement:
        '''
        Waits for an element to be available
        '''
        try:
            self.wait.until(EC.presence_of_all_elements_located(locator))            
            element =  self.browser.find_element(*locator)
            element.location_once_scrolled_into_view
            print(f"Element: {locator[1]} located")

            return element
        except Exception as e:
            print(f"Element: {locator[1]} not found", e)


    def get_page_title(self) -> str:
        '''
        Returns the current page tittle
        '''
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "title")))
        page_title = self.browser.title

        return page_title

    async def get_page_url(self) -> str:
        '''
        Returns the current page URL
        '''
        page_url = self.browser.current_url

        print(f"Current page URL: {page_url}")

        return page_url

    def click_element(self, locator: tuple) -> None:
        '''
        Clicks on an element
        '''
        element = self.get_element(locator)
        element.click()

    def fills_element(self, locator: tuple, text: str) -> None:
        '''
        Fills an element
        '''
        element = self.get_element(locator)
        element.send_keys(text)
        if element.get_property("value") == text:
            print(f"Text | {text} | entered in: {locator[1]}")
        else:
            print(f"Failed to enter | {text} | in: {locator[1]}")

    

    def check_element(self, locator: tuple, check: bool = True) -> None:
        '''
        Checks an element
        '''
        element = self.get_element(locator)

        if not element.is_selected():
            element.click()
            print(f"Element {locator[1]} cheked")
        else:
            print(f"Element {locator[1]} is already cheked")

    def random_wait(self) -> int:
        '''
        Random wait between 300ms and 3000ms to simulate human behavior
        '''
        delay_ms = random.randint(300, 3000)
        time.sleep(delay_ms / 1000)
        return delay_ms
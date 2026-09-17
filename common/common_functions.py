"""
This modules contains project common methods
"""
import os
import time
import random
import logging
import datetime
import requests
import pytest_html
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Common:
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

    def take_screenshot(self) -> str:
        '''
        Takes a page screenshot
        '''
        #ss_path = f"{os.getcwd()}\Reports\screenshots\{__name__}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        ss_name = f"{__name__}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        ss_path = os.path.join(os.getcwd(), "Reports", "screenshots", ss_name)
        self.browser.get_screenshot_as_file(ss_path)
        return ss_path

    def log(self, message: str, extras=None) -> None:
        '''
        Sends message to the report file and console.
        Takes an screenshot of the current actual browser
        '''
        logger = logging.getLogger(__name__)
        
        logger.info(message, stacklevel=2)
        print(message)
        
        if extras is not None:
            extras.append(
                pytest_html.extras.image(
                    #self.browser.get_screenshot_as_base64(),
                    self.take_screenshot(),
                    mime_type="image/png",
                    name="Screenshot",
                )
            )

    def get_page_title(self) -> str:
        '''
        Returns the current page tittle
        '''
        page_title = self.browser.title

        return page_title

    def get_page_url(self) -> str:
        '''
        Returns the current page URL
        '''
        page_url = self.browser.current_url

        return page_url

    def test_explicit_waits(self, browser, extras) -> None:
        '''
        Explicit wait example
        '''
        try:
            element = Chrome(browser, 10).until(
                EC.presence_of_all_elements_located((By.ID, "[Element]", extras))
            )
        finally:
            self.log(element[0].text)

    
class Rest:
    '''
    Class containing REST functions common to the whole project
    '''
    # Constants declaration
    #API headers
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
    }

    def __init__(self, API_URL: str):
        self.API_URL = API_URL
        

    def rest_get (self, body: str) -> list:
                    
        '''
        Makes a REST GET call
        '''
        time.sleep(random.uniform(1.5, 3.0))

        params = {'q': body, 'format': 'json'}
        response = requests.get(self.API_URL, params=params, timeout=10, headers=self.HEADERS)
        print(f"REST GET call executed:\n{response}")
        
        return response
    
    def rest_find(self, body: list, phrase: str):
        '''
        Searches a phrase in the rest response
        '''
        response = body.json() ['Heading'].lower()
        assert phrase.lower() == response

    def rest_response_code(self, body: list, code: int):
        '''
        Validates response status code
        '''
        assert body.status_code == code
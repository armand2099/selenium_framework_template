import os
import logging
import datetime
import pytest_html
from selenium.webdriver import Chrome


class Loggin:
    '''
    Sends logs to report
    '''

    def __init__(self, browser: Chrome, extras=None):
        self.extras = extras
        self.browser = browser

    def take_screenshot(self) -> str:
            '''
            Takes a page screenshot
            '''
            #ss_path = f"{os.getcwd()}\Reports\screenshots\{__name__}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
            ss_name = f"report_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
            ss_path = os.path.join(os.getcwd(), "Reports", "screenshots", ss_name)
            self.browser.get_screenshot_as_file(ss_path)
            return ss_path
    
    def log(self, message: str) -> None:
        '''
        Sends message to the report file and console.
        Takes an screenshot of the current actual browser
        '''
        logger = logging.getLogger(__name__)
        
        logger.info(message, stacklevel=2)
        print(message)
        
        if self.extras is not None:
            self.extras.append(
                pytest_html.extras.image(
                    #self.browser.get_screenshot_as_base64(),
                    self.take_screenshot(),
                    mime_type="image/png",
                    name="Screenshot",
                )
            )
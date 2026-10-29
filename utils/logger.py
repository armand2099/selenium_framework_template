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
        Takes a screenshot of the current browser when report extras are enabled.
        '''
        logger = logging.getLogger(__name__)

        # pytest captures this logger for both the report and console output.
        logger.info(message, stacklevel=2)

        if self.extras is not None:
            try:
                screenshot = self.take_screenshot()
            except Exception as error:
                logger.warning(f"Unable to attach screenshot: {error}", stacklevel=2)
            else:
                self.extras.append(
                    pytest_html.extras.image(
                        screenshot,
                        mime_type="image/png",
                        name="Screenshot",
                    )
                )

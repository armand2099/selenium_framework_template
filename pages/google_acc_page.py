from selenium.webdriver import Chrome
from pages.base_page import BasePage
from pages.google_acc_page_locators import PageLocators


class GoogleAccPage(BasePage):
    '''
    Google account Page methods
    '''

    USERNAME = "Jack"
    PASSWORD = "password"

    def __init__(self, browser: Chrome):
        '''
        Initialize LoginPage class
        '''
        #Initialize parent class
        super().__init__(browser)
        #Get driver fixture
        self.browser = browser
        #Initialize Login PageLocators class
        self.locators = PageLocators()
        

    def enter_email(self, email: str):
        '''
        Fills email textbox
        '''
        self.browser.find_element(*self.locators.EMAIL).send_keys(email)

    def enter_password(self, password: str):
        '''
        Fills Password textbox
        '''
        self.browser.find_element(*self.locators.PASSWORD).send_keys(password)

    def click_next_button(self):
        #Click next button
        self.browser.find_element(*self.locators.NEXT_BTN).click()
from selenium.webdriver import Chrome
from tests.base_page import BasePage
from pages.login_page_locators import PageLocators


class LoginPage(BasePage):
    '''
    Login Page methods
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
        

    def enter_username(self, username = USERNAME):
        '''
        Fills Login page Username textbox
        '''
        self.browser.find_element(*self.locators.USERNAME).send_keys(username)

    def enter_password(self, password = PASSWORD):
        '''
        Fills Login page Password textbox
        '''
        self.browser.find_element(*self.locators.PASSWORD).send_keys(password)

    def check_remember_box(self):
        '''
        Checks the Remember Me Box
        '''
        remember_box = self.browser.find_element(*self.locators.REMEMBER_BOX)

        if not remember_box.is_selected():
            remember_box.click()

        print(f"Checkbox {remember_box.accessible_name} checked")

    def click_sigin(self):
        '''
        Clicks the Singn In button
        '''
        self.click_element(self.locators.SIGNIN_BTN)

    def login(self, username = USERNAME, password = PASSWORD):
        '''
        Does the entire SignIn process
        '''
        self.enter_username(username)
        self.enter_password(password)
        self.click_sigin()
        assert self.get_page_title == "ACME demo app"
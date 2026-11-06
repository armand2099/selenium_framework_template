from pages.base_page import BasePage
from pages.login_page_locators import PageLocators


class LoginPage(BasePage):
    '''
    Login Page methods
    '''

    USERNAME = "Jack"
    PASSWORD = "password"

    def __init__(self, browser):
        '''
        Initialize LoginPage class
        '''
        #Initialize parent class
        super().__init__(browser)
        #Get driver fixture
        self.browser = browser
        #Initialize Login PageLocators class
        self.locators = PageLocators()

        #Page elements
        self.form_name = self.get_element(self.locators.FORM_NAME)
        self.username = self.get_element(self.locators.USERNAME)
        self.password = self.get_element(self.locators.PASSWORD)
        self.signin_btn = self.get_element(self.locators.SIGNIN_BTN)
        self.remember_box = self.get_element(self.locators.REMEMBER_BOX)
        self.twitter_icon = self.get_element(self.locators.TWITTER_ICON)
        self.facebook_icon = self.get_element(self.locators.FACEBOOK_ICON)
        self.insta_icon = self.get_element(self.locators.INSTA_ICON)


    def enter_username(self, username = USERNAME):
        '''
        Fills Login page Username textbox
        '''
        self.fills_element(self.username, username)

    def enter_password(self, password = PASSWORD):
        '''
        Fills Login page Password textbox
        '''
        self.fills_element(self.password, password)

    def check_remember_box(self):
        '''
        Checks the Remember Me Box
        '''
        self.check_element(self.remember_box)

    def click_sigin(self):
        '''
        Clicks the Singn In button
        '''
        self.click_element(self.signin_btn)

    def login(self, username = USERNAME, password = PASSWORD):
        '''
        Does the entire SignIn process
        '''
        self.enter_username(username)
        self.enter_password(password)
        self.click_sigin()
        assert self.get_page_title() == "ACME demo app"
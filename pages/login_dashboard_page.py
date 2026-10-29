from tests.base_page import BasePage
from pages.login_dashboard_page_locators import PageLocators


class LoginDashboardPage(BasePage):
    '''
    Login Dashboard Page methods
    '''

    def __init__(self, browser):
        '''
        Initialize LoginDashboardPage class
        '''
        #Initialize parent class
        super().__init__(browser)
        #Get driver fixture
        self.browser = browser
        #Initialize Login PageLocators class
        self.locators = PageLocators()
from selenium.webdriver.common.by import By


class PageLocators():
    '''
    Login Dashboard page locators
    '''

    def __init__(self):

        #Page elements
        self.LOGGEDUSERNAME =  (By.CSS_SELECTOR, "div.logged-user-name")
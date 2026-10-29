from selenium.webdriver.common.by import By


class PageLocators():
    '''
    Google accounts page locators
    '''

    def __init__(self):

        #Page elements
        self.EMAIL =  (By.ID  ,"identifierId")
        self.NEXT_BTN = (By.XPATH, "//span[@jsname='V67aGc' and text()='Next']")
        self.PASSWORD = (By.NAME, "Passwd")
from selenium.webdriver.common.by import By


class PageLocators():
    '''
    Login page locators
    '''

    def __init__(self):

        #Page elements
        self.alert_button = (By.ID, "alertexamples")
        self.alert_text = (By.ID, "alertexplanation")
        self.confirm_button = (By.ID, "confirmexample")
        self.confirm_text = (By.ID, "confirmexplanation")
        self.confirm_return = (By.ID, "confirmreturn")
        self.promp_box_button = (By.ID, "promptexample")
        self.promp_return = (By.ID, "promptreturn")
        self.prompt_text = (By.ID, "promptexplanation")
from selenium.webdriver.common.by import By


class PageLocators:
    '''
    New Window page locators
    '''

    def __init__(self):
        self.new_tab_button = (By.ID, "tabButton")
        self.new_window_button = (By.ID, "windowButton")
        self.new_window_msg_button = (By.ID, "messageWindowButton")

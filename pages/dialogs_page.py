from pages.base_page import BasePage
from pages.dialogs_page_locators import PageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 10

class DialogsPage(BasePage):
    '''
    Dialogs Page methods
    '''

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
        self.alert_button = self.get_element(self.locators.alert_button)
        self.alert_text = self.get_element(self.locators.alert_text)
        self.confirm_button = self.get_element(self.locators.confirm_button)
        self.confirm_text = self.get_element(self.locators.confirm_text)
        self.confirm_return = self.get_element(self.locators.confirm_return)
        self.promp_box_button = self.get_element(self.locators.promp_box_button)
        self.promp_return = self.get_element(self.locators.promp_return)
        self.prompt_text = self.get_element(self.locators.prompt_text)

    def dialog_handler(self):
        WebDriverWait(self.browser, TIMEOUT).until(EC.alert_is_present())
        dialog = self.browser.switch_to.alert
        return dialog
    
    def on_dialog(self, prompt_text: str = '', accept: bool = True):
        #Accepts a browser dialog, enters text when required.   
        dialog = self.dialog_handler()     
        dialog_text = dialog.text
        print(f'Dialog {dialog_text} Opened')
        
        if prompt_text:
            dialog.send_keys(prompt_text)
            print(f'Dialog {dialog_text} Text Entered: {prompt_text}')

        if accept:
            dialog.accept()
            print(f'Dialog {dialog_text} Accepted')
        else:
            dialog.dismiss()
            print(f'Dialog {dialog_text} Dismissed')

        WebDriverWait(self.browser, TIMEOUT).until_not(EC.alert_is_present())    
from selenium.webdriver.common.by import By


class PageLocators():

    def __init__(self):

        #Page elements
        self.FORM_NAME =  (By.CSS_SELECTOR, "h4.auth-header")
        self.USERNAME = (By.ID, "username")
        self.PASSWORD = (By.ID, "password")
        self.SIGNIN_BTN = (By.ID, "log-in")
        self.REMEMBER_BOX = (By.CSS_SELECTOR, "input.form-check-input")
        self.TWITTER_ICON = (By.CSS_SELECTOR, 'img[src="img/social-icons/twitter.png"]')
        self.FACEBOOK_ICON = (By.CSS_SELECTOR, 'img[src="img/social-icons/facebook.png"]')
        self.INSTA_ICON = (By.CSS_SELECTOR, 'img[src="img/social-icons/linkedin.png"')
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class Loginpage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def getLoginLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._login_link)

    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_field)

    def getPassWord(self):
        return self.driver.find_element(By.ID, self._password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.NAME, self._login_button)

    def clickLoginLink(self):
        self.getLoginLink().click()

    def enterEmail(self, email):
        self.getEmailField().send_keys(email)

    def enterPassWord(self, password):
        self.getPassWord().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassWord(password)
        self.clickLoginButton()


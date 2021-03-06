import utilities.custom_logger as cl
from pages.navigation.navigation_page import NavigationPage
import logging
from base.basepage import BasePage


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(self.driver)

    # Locator
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    # _user_setting_icon = "//div[@id='navbar']//span[text()='Test User']"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")
        self.wait(waitMilliseconds=1000)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassWord(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassWord(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//div[@id='navbar']//li[@class='dropdown'] ", locatorType="xpath")
        # //*[@id='navbar']//span[text()='Test User']
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(), 'Invalid email or password.')]", locatorType="xpath")
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def verifyTitle(self):
        return self.verifyPageTitle("Let's Kode It")

    def wait(self, waitMilliseconds):
        self.driver.implicitly_wait(waitMilliseconds)

    def logout(self):
        self.nav.navigateToUseSetting()
        logoutLinkElement = self.waitForElement(locator="//div[@id='navbar']//a[@href='/sign_out']",
                                                locatorType="xpath", pollFrequency=1)
        self.elementClick(element=logoutLinkElement)



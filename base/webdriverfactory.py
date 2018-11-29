"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        base_url = "https://letskodeit.teachable.com/"
        if self.browser == "edge":
            # Set ie driver
            driver = webdriver.Edge()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
            driver.set_window_size(1440, 900)
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(base_url)
        return driver


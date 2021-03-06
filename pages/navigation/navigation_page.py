import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator
    _my_courses = "My Courses"
    _all_course = "All Courses"
    _practice = "Practice"
    _user_settings_icon = "//div[@id='navbar']//li[@class='dropdown']"

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigateToAllCourse(self):
        self.elementClick(locator=self._all_course, locatorType="link")

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType="link")

    def navigateToUseSetting(self):
        # userSettingsElement = self.waitForElement(locator=self._user_settings_icon,
        # locatorType="xpath", pollFrequency=1)
        # self.elementClick(element=userSettingsElement)
        self.elementClick(locator=self._user_settings_icon, locatorType="xpath")


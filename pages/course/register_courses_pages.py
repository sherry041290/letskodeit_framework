import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class RegisterCoursePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _search_box = "search-courses"
    _search_course_icon = "search-course-button"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _all_courses = "All Courses"  # link text
    _enroll_button = "enroll-button-top"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "exp-date"  # name
    _cc_cvv = "cvc"   # name
    _zip = "postal"   # name
    _agree_to_terms_checkbox = "agreed_to_terms_checkbox"
    _submit_enroll = "//button[@id='confirm-purchase']/parent::div"

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box)
        self.elementClick(locator=self._search_course_icon)

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locatorType="xpath", locator=self._course.format(fullCourseName))

    def clickEnrollButton(self):
        self.elementClick(locator=self._enroll_button)

    def enterCardNumber(self, num):
        self.switchToFrame("__privateStripeFrame4")
        self.sendKeys(num, locator=self._cc_num, locatorType="xpath")
        self.driver.switch_to.default_content()

    def enterCardExp(self, exp):
        self.switchToFrame("__privateStripeFrame5")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
        self.driver.switch_to.default_content()

    def enterCardCVV(self, cvv):
        self.switchToFrame("__privateStripeFrame6")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
        self.driver.switch_to.default_content()

    def enterZipCode(self, postal_code):
        self.switchToFrame("__privateStripeFrame7")
        self.sendKeys(postal_code, locator=self._zip, locatorType="name")
        self.driver.switch_to.default_content()

    def clickAgreeCheckbox(self):
        self.elementClick(self._agree_to_terms_checkbox)

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll)

    def enterCardInfo(self, num, exp, cvv, zip):
        self.wait(2)
        self.enterCardNumber(num)
        self.wait(2)
        self.enterCardExp(exp)
        self.wait(2)
        self.enterCardCVV(cvv)
        self.wait(2)
        self.enterZipCode(zip)

    def enrollCourse(self, num="", exp="", cvv="", zip=""):
        self.clickEnrollButton()
        self.webScroll("down")
        self.enterCardInfo(num, exp, cvv, zip)
        self.clickAgreeCheckbox()

    def verifyEnrollFailed(self):
        result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath",
                                info="Enroll Button")
        return not result

    def allCourse(self):
        self.elementClick(self._all_courses, "link")







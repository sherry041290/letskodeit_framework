from pages.course.register_courses_pages import RegisterCoursePage
from pages.navigation.navigation_page import NavigationPage
from utilities.result_status import ResultStatus
import pytest
import unittest
from ddt import data, unpack, ddt
from utilities.read_data import getCSVData
import time


@pytest.mark.usefixture("oneTimeSetUp", "setUp")
@ddt
class EnrollMultiTest(unittest.TestCase):

    @pytest.fixture(autouse=2)
    def objectSetUp(self, oneTimeSetUp):
        self.courses = RegisterCoursePage(self.driver)
        self.test_status = ResultStatus(self.driver)
        self.navigate = NavigationPage(self.driver)

    def setUp(self):
        self.navigate.navigateToAllCourse()

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:/Users/lenovo/PycharmProjects/letskodeit/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, course_name, cc_num, cc_exp, cc_cvv, zip_code):
        self.courses.enterCourseName(course_name)
        time.sleep(1)
        self.courses.selectCourseToEnroll(course_name)
        time.sleep(1)
        self.courses.enrollCourse(num=cc_num, exp=cc_exp, cvv=cc_cvv, zip=zip_code)
        result = self.courses.verifyEnrollFailed()
        self.test_status.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")
        time.sleep(1)
        self.driver.back()
        time.sleep(1)


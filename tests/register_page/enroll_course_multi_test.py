from pages.course.register_courses_pages import RegisterCoursePage
from utilities.result_status import ResultStatus
import pytest
import unittest
from ddt import data, unpack, ddt

@pytest.mark.usefixture("oneTimeSetUp", "setUp")
@ddt
class EnrollMultiTest(unittest.TestCase):

    @pytest.fixture(autouse=2)
    def classSetUp(self, oneTimeSetUp):
        self.courses = RegisterCoursePage(self.driver)
        self.test_status = ResultStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "1234 5678 9012 3456", "1220", "444", "12345"), ("Learn Python 3 from scratch", "2220 8584 9909 2134", "1222", "209", "789890"))
    @unpack
    def test_invalidEnrollment(self, course_name, cc_num, cc_exp, cc_cvv, zip_code):
        self.courses.enterCourseName(course_name)
        self.courses.selectCourseToEnroll(course_name)
        self.courses.enrollCourse(num=cc_num, exp=cc_exp, cvv=cc_cvv, zip=zip_code)
        result = self.courses.verifyEnrollFailed()
        self.test_status.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")
        self.driver.back()
        self.courses.allCourse()


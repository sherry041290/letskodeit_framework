from pages.course.register_courses_pages import RegisterCoursePage
from utilities.result_status import ResultStatus
import pytest
import unittest

@pytest.mark.usefixture("oneTimeSetUp", "setUp")
class ResgisterTest(unittest.TestCase):

    @pytest.fixture(autouse=2)
    def classSetUp(self, oneTimeSetUp):
        self.courses = RegisterCoursePage(self.driver)
        self.test_status = ResultStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.enrollCourse(num="1234 5678 9012 3456", exp="1220", cvv="444", zip="12345")
        result = self.courses.verifyEnrollFailed()
        self.test_status.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")


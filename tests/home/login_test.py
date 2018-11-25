from pages.home.login_page import Loginpage
from utilities.result_status import ResultStatus
import unittest
import pytest


@pytest.mark.usefixture("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=2)
    def classSetUp(self, oneTimeSetUp):
        self.lg = Loginpage(self.driver)
        self.test_status = ResultStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lg.login("test@email.com", "abcabc")
        # result1 = self.lg.verifyTitle()
        # self.test_status.mark(result1, "Title Verified")
        self.lg.clearFields()
        result2 = self.lg.verifyLoginSuccessful()
        # self.test_status.markFinal("test_validLogin", result2, "Login was successful")
        assert result2 == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lg.login("test@email.com", "abcabccc")
        result = self.lg.verifyLoginFailed()
        assert result == True

